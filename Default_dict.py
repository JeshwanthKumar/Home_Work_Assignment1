# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
n, m = map(int, input().split())
A = defaultdict(list)
for i in range(1, n+1):
    A[input()].append(i)
    # print(A)
# for i in A.values():
#     print (*i)
keys = A.keys()
# print(keys)
for j in range(m):
    B = input()
    if B in keys:
        print(*A[B])
    else:
        print("-1")

# for k in B:
#     if k in A.keys():
#         print(A[i])
