if __name__ == '__main__':
    object = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        object[name] = score
    s_list = sorted(set(object.values()))
    result = sorted(key for key, value in object.items() if value == s_list[1])
    print(*result, sep='\n')