#Ordered Dictionary
'''
An OrderedDict internally maintains a doubly linked list that orders the keys according to insertion order. 
When a new item is first inserted, it is placed at the end of this list. Subsequent reassignment of an existing key doesn’t change the order.
'''
from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

for k in d:
	print(k,d[k])
