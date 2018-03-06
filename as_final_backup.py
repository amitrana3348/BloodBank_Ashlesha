
import serial
import os, time
import pygsm
import tinydb
from tinydb import where, Query			# Comment :THIS WILL IMPORT THE tinydb database
db = tinydb.TinyDB('ashlesha.json')		# Comment : name the database as ashlesha.json
myquery = Query()

#db.purge()
#db.all()
###############################################################################
################################ GSM RELATED CODES HERE #######################

gsm = pygsm.GsmModem(port = "/dev/ttyUSB0").boot()
a = gsm.wait_for_network()
def delsms():
    for i in range (1,5):
        gsm.command("AT+CMGD={0}".format(i))
        print 'deleting...',i
        time.sleep(1)

#port = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=1)	#port number information to be put here, in case of raspberry pi, it'll be ttyUSB0
#port.write("\x1A") # Enable to send SMS

sms = " "

 


################################################################################
######################################## GSM ENDS ##############################




# Comment : this function will save the records to the database
def save_to_database(record):
    ab = record.split(',')
    if ab[0] == 'N':
        print ab
        db.insert({'name': ab[1], 'gender': ab[2], 'address': ab[4], 'blood': ab[3], 'number': ab[5]})

# Comment : below function will search for the blood group from database
def search_blood(grp):
    global sms
    print "\n***************** here in the search function *******************\n"
    response = db.search(myquery.blood == grp)
    #res2 = response.split(',')
    #print res2[0]
    mylen = len(response)
    print response
    print mylen
    #sendSms(response)
    if mylen > 0:
        for ab in range (0,mylen):
            print "this is response no "+str(ab)
            abc = response[ab]
            sms = str(abc)
            sms = sms.replace('u','')
            sms = sms.replace("'",'')
            print sms
            gsm.send_sms("9922968553",sms)
            time.sleep(5)
            print "\n\n"
        
    

#save_to_database('N,pranita,female,zone5,b+,99229')
#save_to_database('N,sujit,male,zone1,b+,12345')

#search_blood('b+')

#while True:
    #sms = "hello world"
    #sendSms()
    #time.sleep(20)
    
while True:
    print "Checking for New Msg..."
    message = gsm.next_message()
    time.sleep(2)
    #print message
    if message != None:
        print message
        a = str(message)
        #message = message.replace('<','')
        msg = a[a.find("'")+1:a.rfind("'")]
        print 'msg is here'
        print msg
        print 'message printing done'
        time.sleep(2)
        
        print "This is received " + msg
        gsm.command("AT+CMGDA=\"DEL ALL\"\r")
        #delsms()
        time.sleep(1)
        mymsg = msg.split(',')
        print mymsg
        if mymsg[0] == 'query':
            print "Searching for Blood Group"
            print mymsg[1]
            search_blood(mymsg[1])
            mymsg[0] = ""

        if mymsg[0] == 'N':
            print "Adding to database"
            save_str = msg[2]
            save_str = 'N,' + mymsg[1] +','+mymsg[2] + ','+mymsg[3] + ','+mymsg[4] + ','+mymsg[5]
            print save_str
            print '\n\n\n\n'
            mymsg[0] = ""
            #save_to_database('N,pranita,female,zone5,b+,99229')
            save_to_database(save_str)

        if mymsg[0]=='purge':
            db.purge()
            db.all()
        msg = ""
            
            
#db.search(myquery.name == 'amit')
