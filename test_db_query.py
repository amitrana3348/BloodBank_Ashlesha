
import serial
import os, time

import tinydb
from tinydb import where, Query			# Comment :THIS WILL IMPORT THE tinydb database
db = tinydb.TinyDB('ashlesha.json')		# Comment : name the database as ashlesha.json
myquery = Query()


def save_to_database(record):
    ab = record.split(',')
    if ab[0] == 'N':
        print ab
        db.insert({'name': ab[1], 'gender': ab[2], 'address': ab[3], 'blood': ab[4], 'number': ab[5]})

save_to_database('N,sachin,male,zone1,b+,999')
save_to_database('N,sachin2,male,zone2,b+,589')
print "\n***************** here in the search function *******************\n"
grp = 'b+'
response = db.search(myquery.blood == grp)
#res2 = response.split(',')
#print res2[0]
mylen = len(response)
print response
print mylen
for ab in range (0,mylen):
    print "\nthis is response no "+str(ab)
    sms = response[ab]
    print sms
    #sendSms()
    time.sleep(2)
    print "\n\n"
