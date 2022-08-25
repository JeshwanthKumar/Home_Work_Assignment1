# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
for i in range(T):
    n = int(input())
    side_length = list(map(int, input().split()))
    copy = []
    for i in range(n):
        if side_length[0] >= side_length[-1]:
            copy += [side_length.pop(0)]
        else:
            copy += [side_length.pop()]
    if copy == sorted(copy, reverse = True):
        print("Yes")
    else:
        print("No")
    