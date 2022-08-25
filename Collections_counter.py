# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
total = 0
X = int(input())
shoe_size = Counter(map(int, input().split()))
N = int(input())
for i in range(N):
    size, price = map(int, input().split())
    if(shoe_size[size]):
        total+=price
        shoe_size[size] -=1
        
print(total)
