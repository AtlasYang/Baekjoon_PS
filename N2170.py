#https://www.acmicpc.net/problem/2170
#2022.01.03.

import sys

N = int(sys.stdin.readline())
data = []
for _ in range(N):
    data.append(list(map(int, sys.stdin.readline().split())))

data = sorted(data, key = lambda i: i[0])


start = data[0][0]
end = data[0][1]
length = end - start
for i in range(1, N):
    x = data[i][0]
    y = data[i][1]
    if x < end:
        if y < end:
            continue
        else:
            length += y - end
            end = y
            continue
    else:
        length += y - x
    end = y

print(length)
