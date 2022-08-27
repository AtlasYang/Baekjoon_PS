#https://www.acmicpc.net/problem/2252
#2022.08.27.
#Timeout Code

import sys

N, M = list(map(int, sys.stdin.readline().split()))

seq = []
numlist = [i + 1 for i in range(N)]

for _ in range(M):
    seq.append(tuple(map(int, sys.stdin.readline().split())))


stack = [seq[0][0], seq[0][1]]
numlist.remove(seq[0][0])
numlist.remove(seq[0][1])
del seq[0]

res = []


epoch = 0
while True:
    flag = False
    for i in range(len(seq)):
        if seq[i][0] == stack[-1]:
            if seq[i][1] in numlist:
                flag = True
                stack.append(seq[i][1])
                numlist.remove(seq[i][1])
                tr = seq.pop(i)
                break

    
    if numlist == []:
        res = stack + res
        break
    else:
        if seq == []:
            res = numlist + stack + res
            break
        else:
            if flag:
                continue
            t = stack.pop(-1)
            res = [t, ] + res
            if stack == []:
                stack.append(numlist[0])
                numlist.pop(0)
            continue

print(*res)

