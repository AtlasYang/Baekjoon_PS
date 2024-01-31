def cal(val):
    a, b = val
    if a == b:
        print(a * 10)
        return

    aLevel, bLevel = 0, 0
    for i in range(10):
        if a >= 2 ** i:
            aLevel = i
        if b >= 2 ** i:
            bLevel = i

    if aLevel > bLevel:
        cal([a // 2, b])
    elif aLevel < bLevel:
        cal([a, b // 2])
    else:
        cal([a // 2, b // 2])
    


def main():
    num = int(input())
    inputList = []
    for i in range(num):
        inputList.append(list(map(int, input().split())))
    
    for val in inputList:
        cal(val)

if __name__ == '__main__':
    main()