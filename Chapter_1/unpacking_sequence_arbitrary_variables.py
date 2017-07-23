
#problem : to get average of all elements excep first and last

def drop_first_last(lis_grades):
    first,*middle,last = lis_grades
    return middle

print(drop_first_last([1,2,5,7,8,4,9]))


record = ('Dave','dave@example.com','777-234-983','565-322-098')
name,email,*phone=record
print(name)
print(email)
print(phone)


*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print(trailing)
print(current)


records=[
('foo',1,2),
('bar','hello'),
('foo',45,46)
]

def do_foo(x,y):
	print('foo',x,y)
	
def do_bar(s):
	print('bar',s)
	

for tag,*args in records:
	if tag=='foo':
		do_foo(*args)
	elif tag=='bar':
		do_bar(*args)
		
		
line = 'nobody:*-2:-2:Unprivileged User:/var/tmp/:/user/bin'.split(':')
uname,*fields,homedir,sh = line
print(uname)
print(fields)
print(sh)

record = ('ACME',50,123.45,(12.18,2012))
name,*_,(*_,year) = record
print(name)
print(year)

def sum(items):
	head,*tail= items
	return head + sum(tail) if tail else head
	
print(sum([4,6,9,5,3,2]))
		
		
		
