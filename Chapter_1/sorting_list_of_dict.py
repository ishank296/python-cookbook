#sorting list of dictionaries

rows=[
  {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

from operator import itemgetter

rows_by_fname= sorted(rows,key=itemgetter('fname'))
rows_by_uid= sorted(rows,key=itemgetter('uid'))

print(rows_by_fname)
print(rows_by_uid)

#The functionality of itemgetter() is sometimes replaced by lambda expressions
print(sorted(rows,key=lambda x : x['fname']))
print(sorted(rows,key=lambda x : x['uid']))

#sorting objects
from operator import attrgetter
class User:
	def __init__(self,user_id):
		self.user_id=user_id
		
	def __repr__(self):
		return "User({})".format(self.user_id)
		
users= [User('Jaimin'),User('Ishank297'),User('Logn')]
users_sorted= sorted(users,key=attrgetter('user_id'))
print(users_sorted)