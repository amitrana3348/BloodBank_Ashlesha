import tinydb
from tinydb import where, Query
db = tinydb.TinyDB('ashlesha.json')
myquery = Query()

#db.purge()
#db.all()
def save_to_database(record):
    ab = record.split(',')
    if ab[0] == 'N':
        print ab
        db.insert({'name': ab[1], 'gender': ab[2], 'address': ab[3], 'blood': ab[4], 'number': ab[5]})

def search_blood(grp):
    response = db.search(myquery.blood == grp)
    #res2 = response.split(',')
    #print res2[0]
    mylen = len(response)
    print mylen
    if mylen > 0:
        for i in range (0,mylen):
            print "this is response no "+str(i)
            print response[0]
            print "\n\n"
        
    

#save_to_database('N,pranita,female,zone5,b+,99229')
#save_to_database('N,sujit,male,zone1,b+,12345')

search_blood('b+')
#db.search(myquery.name == 'amit')
