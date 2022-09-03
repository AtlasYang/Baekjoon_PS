#https://www.acmicpc.net/problem/3392
#2022.09.03.

import sys

maxlen = 30001

N = int(input())
M = [[0, 0, 0, 0] for _ in range(N * 2)]
for i in range(0, N * 2, 2):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())
    M[i][0], M[i][1], M[i][2], M[i][3] = x1, y1, y2 - 1, 1 #start line
    M[i + 1][0], M[i + 1][1], M[i + 1][2], M[i + 1][3] = x2, y1, y2 - 1, -1 #end line
M.sort(key = lambda x: x[0])

ST_cnt = [0 for _ in range(8 * maxlen)]
ST = [0 for _ in range(8 * maxlen)]

def ST_update(node, start, end, left, right, val):
    if end < left or start > right:
        return
    elif left <= start and end <= right:
        ST_cnt[node] += val
    else:
        mid = (start + end) //2
        ST_update(node * 2, start, mid, left, right, val)
        ST_update(node * 2 + 1, mid + 1, end, left, right, val)
    
    if ST_cnt[node] > 0:
        ST[node] = end - start + 1
    else:
        ST[node] = ST[node * 2] + ST[node * 2 + 1]

res = 0
ST_update(1, 0, maxlen - 1, M[0][1], M[0][2], M[0][3])
for i in range(1, N * 2):
    dx = M[i][0] - M[i - 1][0]
    res += dx * ST[1]
    ST_update(1, 0, maxlen - 1, M[i][1], M[i][2], M[i][3])
print(res)
