from collections import deque

def search(lines,pattern,history=5):
	previous_lines = deque(maxlen=history)
	for line in lines:
		if pattern in line:
			yield line,previous_lines
		previous_lines.append(line)
		
		

"""Using deque(maxlen=N) creates a fixed-sized queue. When new items are added and the queue is full, the oldest item is automatically removed"""
q = deque(maxlen=3)
q.append(3)
q.append(1)
q.append(2)
print(q)

q.append(4)
q.append(5)
print(q)
q.appendleft(7)
print(q)	
q.popleft()
print(q)	
q.pop()
print(q)
q.extend('werwe')
print(q)	
q.rotate(1)
print(q)
q.rotate(2)
print(q)	
		
if __name__=='__main__':
	with open('test.txt') as f:
		for line,previous_lines in search(f,' is ',5):
			for pline in previous_lines:
				print(pline,end='')
			print(line,end='')
			print('-'*20)