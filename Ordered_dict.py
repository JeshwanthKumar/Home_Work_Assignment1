from collections import OrderedDict
N = int(input())
items = OrderedDict()
for i in range(N):
   item_name = input().rsplit(' ')
   net_price = int(input().split()[-1])
   if item_name in items.keys():
    items[item_name] += net_price
   else:
    items[item_name] = net_price
# for i, j in items.keys() :
#     print(i, j) 
print([i, j] for i in items.keys() for j in items.values())
