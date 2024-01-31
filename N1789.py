def sumToN(n):
    return n * (n + 1) // 2

def main():
    n = int(input())
    i = 1
    while True:
        if sumToN(i) == n:
            print(i)
            break
        elif sumToN(i) > n:
            print(i - 1)
            break
        i += 1

if __name__ == '__main__':
    main()