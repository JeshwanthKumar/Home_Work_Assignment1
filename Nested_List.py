if __name__ == '__main__':
    object = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        object[name] = score
    s_list = set(object.values())
    s_list = sorted(s_list)
    result = (key for key, value in object.items() if value == s_list[1])
    result = sorted(result)
    print(*result, sep='\n')
