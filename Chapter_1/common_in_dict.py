#commonalites in Dictionary

a={
'x':3,
'y':4,
'z':5
}

b={
'w':6,
'x':4,
'y':5
}


#Find the keys in common
print(a.keys() & b.keys())

#Find in Keys in first dict but not in second dict

print(a.keys() - b.keys())
#Find key,values pairs in common
print(a.items() & b.items())

# Make a new dictionary with certain keys removed
c = {key:a[key] for key in a.keys() - {'z', 'w'}}
print(c)