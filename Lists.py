if __name__ == '__main__':
    N = int(input())
    list = []
    for i in range(1,N+1):
        operations = input().split()
        if operations[0] == 'insert':
            list.insert(int(operations[1]), int(operations[2]))
        elif operations[0] == 'print':
            print(list)
        elif operations[0] == 'remove':
            list.remove(int(operations[1]))
        elif operations[0] == 'append':
            list.append(int(operations[1]))
        elif operations[0] == 'sort':
            list.sort()
        elif operations[0] == 'pop':
            list.pop()
        elif operations[0] == 'reverse':
            list = list[::-1]