"""
Initializing Dict/ multi-value Dictionary
"""

d = {
'a':[1,2,3],
'b':[4,5]
}

e={
'a':[56,'df',67],
'b':[7,9,43]
}

print (d)
print (e['b'][2])

#A feature of defaultdict is that it automatically initializes the first value so you can simply focus on adding items
from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['a'].append(5)

print (d['a'])

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['a'].add(1)
print(d)