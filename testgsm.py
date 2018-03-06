import pygsm
import time 
#import re
gsm = pygsm.GsmModem(port = "/dev/ttyUSB0").boot()
def delsms():
    for i in range (1,5):
        gsm.command("AT+CMGD={0}".format(i))
        print 'deleting...',i
        time.sleep(1)



a = gsm.wait_for_network()
#gsm.send_sms("9922968553","hello")

while True:
    a = "<pygsm.IncomingMessage from +919922968553: 'Dada'>"
    b = a[a.find("'")+1:a.rfind("'")]
    #b = a.find("'")
    print b
    time.sleep(2)
while True:
    message =gsm.next_message()
    if message != None:
        print message
        time.sleep(2)
