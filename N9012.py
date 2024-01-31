def cal(data):
    stack = []
    for i in data:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                return False
    if stack:
        return False
    else:
        return True

def main():
    n = int(input())
    li = []
    for _ in range(n):
        li.append(list(input()))
    for i in li:
        if cal(i):
            print('YES')
        else:
            print('NO')

if __name__ == '__main__':
    main()