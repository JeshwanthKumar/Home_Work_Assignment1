if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    # Without using sort function
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    arr = set(arr)
    arr.remove(max(arr))
    print(max(arr))
    
    # With using sort function
    # arr.sort()
    # arr = set(arr)
    # arr.remove(max(arr))
    # print(max(arr)) 