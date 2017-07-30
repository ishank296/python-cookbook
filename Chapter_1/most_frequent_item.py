# Determining most frequently Occuring item in a sequence
from collections import Counter

words = [
   'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
   'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
   'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
   'my', 'eyes', "you're", 'under'
]
#As input, Counter objects can be fed any sequence of hashable input items. 
#Under the covers, a Counter is a dictionary that maps the items to the number of occurrences.
word_count = Counter(words)
# print top three most common words in list
print(word_count.most_common(3))
print(word_count)