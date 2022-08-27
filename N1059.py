#https://www.acmicpc.net/problem/1059
#2022.08.27.

from math import comb

def main():
    L = int(input())
    S = sorted(list(map(int, input().split())))
    n = int(input())
    
    if n in S:
        print(0)
        return
    
    low, up = 1, S[0] - 1
    for i in range(len(S) - 1):
        if n > S[i]:
            low = S[i] + 1
            up = S[i + 1] - 1

    p = comb(up - low + 1, 2)
    q = comb(n - low, 2)
    r = comb(up - n, 2)
    print(p - q - r)
    return
    
main()
