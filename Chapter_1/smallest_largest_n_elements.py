import heapq

nums=[6,8,9,23,45,7,81,87,34,44]
print(heapq.nlargest(3,nums))
print(heapq.nsmallest(3,nums))

portfolio=[
{'name':"IBM",'shares':23,'price':10.0},
{'name':"APPLE",'shares':45,'price':35},
{'name':"MICROSOFT",'shares':48,'price':34.0},
{'name':"ACME",'shares':67,'price':27.98},
{'name':"YAHOO",'shares':56,'price':12.77}
]

print(heapq.nlargest(3,portfolio,key=lambda s: s['price']))
print(heapq.nsmallest(3,portfolio,key=lambda s: s['price']))


"""
Creating heap from list
"""
nums=[1,8,7,5,3,9,3,12,56,78]
heap=list(nums)
heapq.heapify(heap)
print(heap)
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heap)