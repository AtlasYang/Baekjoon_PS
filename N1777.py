#https://www.acmicpc.net/problem/1777
#2022.08.27.
#Timeout Code

import sys

N = int(input())
inv = list(map(int, sys.stdin.readline().strip().split()))
seq = [0 for _ in range(N)]

idx = list(range(-1, -N - 1, -1))

for i in range(N - 1, -1, -1):
    num = i + 1
    cnt = inv[num - 1]
    for j in idx:
        if cnt == 0:
            seq[j] = num
            idx.remove(j)
            break
        else:
            cnt -= 1

print(*seq)
