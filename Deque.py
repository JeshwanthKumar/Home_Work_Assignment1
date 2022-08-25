# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
N = int(input())
que = deque()
for i in range(N):
    operations = input().split()
    if operations[0] == "append":
        que.append(operations[1])
    elif operations[0] == "pop":
        que.pop()
    elif operations[0] == "popleft":
        que.popleft()
    elif operations[0] == "appendleft":
        que.appendleft(operations[1])
print(*que)
