import tinydb
from tinydb import where
#db = tinydb.TinyDB("tiny.db")
db = tinydb.TinyDB('ashlesha.json')
db.insert({'Name': 'amit', 'gender': 'male', 'address': 'zone1', 'blood': 'b+', 'number': '9922968553'})
db.insert({'Name': 'sujit', 'gender': 'male', 'address': 'zone1', 'blood': 'b+', 'number': '9922968553'})
db.insert({'Name': 'sidhant', 'gender': 'male', 'address': 'zone2', 'blood': 'ab+', 'number': '9922968553'})
db.insert({'Name': 'sachin', 'gender': 'male', 'address': 'zone2', 'blood': 'ab+', 'number': '9922968553'})
db.insert({'Name': 'pratiksha', 'gender': 'female', 'address': 'zone3', 'blood': 'o+', 'number': '9922968553'})
db.insert({'Name': 'pranita', 'gender': 'female', 'address': 'zone3', 'blood': 'o+', 'number': '9922968553'})
db.insert({'Name': 'swati', 'gender': 'female', 'address': 'zone4', 'blood': 'a+', 'number': '9922968553'})
db.insert({'Name': 'maitreyee', 'gender': 'female', 'address': 'zone4', 'blood': 'a+', 'number': '9922968553'})
