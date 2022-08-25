# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
n = int(input())
dictionary = OrderedDict()
for i in range(n):
    words = input()
    if words in dictionary.keys():
        dictionary[words] += 1
    else:
        dictionary[words] = 1
print(len(dictionary.keys()))
for i in dictionary.values():
    print(i, end = " ")
