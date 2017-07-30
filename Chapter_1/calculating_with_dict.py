#Calculating with dictionaries

prices = {
   'ACME': 45.23,
   'AAPL': 612.78,
   'IBM': 205.55,
   'HPQ': 37.20,
   'FB': 10.75
}

print(zip(prices.keys(),prices.values()))

for elem in zip(prices.keys(),prices.values()):
	print(elem)

min_price = min(zip(prices.values(),prices.keys()))
print("Min Price: ",min_price)
max_price = max(zip(prices.values(),prices.keys()))
print("Max Price: ",max_price)

#If you try to perform common data reductions on a dictionary, you’ll find that they only process the keys, not the values
print(min(prices))
print(max(prices))

#You can get the key corresponding to the min or max value if you supply a key function to min() and max(). 
print(min(prices,key=lambda k : prices[k]))
print(max(prices,key=lambda k : prices[k]))

#TO get min,max value we have to perform extra lookup step
print(prices[min(prices,key=lambda k : prices[k])])
print(prices[max(prices,key=lambda k : prices[k])])