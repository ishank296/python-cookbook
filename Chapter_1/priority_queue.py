"""
Priority Queue Implementation with heap

 the queue consists of tuples of the form (-priority, index, item). 
 The priority value is negated to get the queue to sort items from highest priority to lowest priority. 
 This is opposite of the normal heap ordering, which sorts from lowest to highest value.
 
 The role of the index variable is to properly order items with the same priority level. 
 By keeping a constantly increasing index, the items will be sorted according to the order in which they were inserted. 
"""

import heapq

class PriorityQueue:
	
	def __init__(self):
		self._queue=[]
		self._index=0
		
	def push(self,item,priority):
		heapq.heappush(self._queue,(-priority,self._index,item))
		self._index += 1
	
	def pop(self):
		return heapq.heappop(self._queue)[-1]
		

		
class Item:
	def __init__(self,name):
		self.name = name
	def __repr__(self):
		return 'Item({!r})'.format(self.name)
		
		
		
q = PriorityQueue()
q.push(Item('foo'),1)
q.push(Item('bar'),5)
q.push(Item('spam'),8)
q.push(Item('grok'),9)
q.push(Item('geek'),1)

print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
#print(q.pop())		

#the index also serves an important role in making the comparison operations work for items that have the same priority level.
a = Item('foo')
b = Item('bar')
# print(a < b) # Error Unsupported operand '<' for type Item

a = (1,Item('foo'))
b = (2,Item('bar'))
c = (1,Item('grok'))
print(a < b)
print(a < c)