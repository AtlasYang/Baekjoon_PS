def main():
    n = int(input())
    li = list(map(int, input().split()))
    li.sort()
    res = []
    for i in range(len(li)):
        res.append(li[i] + li[-i-1])
    print(min(res))

if __name__ == '__main__':
    main()