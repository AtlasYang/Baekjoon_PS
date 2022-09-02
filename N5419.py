#https://www.acmicpc.net/problem/5419
#2022.09.02.
#Timeout Code

import math, sys

def seg_inc(tree, idx, node, start, end):
    if idx < start or idx > end:
        return
    
    tree[node] += 1
    
    if start == end:
        return
    else:
        mid = (start + end) // 2
        seg_inc(tree, idx, node * 2, start, mid)
        seg_inc(tree, idx, node * 2 + 1, mid + 1, end)

def seg_sum(tree, node, start, end, s, e):
    if end < s or e < start:
        return 0
    elif start <= s and e <= end:
        return tree[node]
    else:
        mid = (s + e) // 2
        return seg_sum(tree, node * 2, start, end, s, mid) + seg_sum(tree, node * 2 + 1, start, end, mid + 1, e)


T = int(sys.stdin.readline().strip())

for _ in range(T):
    n = int(sys.stdin.readline().strip())
    pos = []
    for _ in range(n):
        pos.append(list(map(int, sys.stdin.readline().strip().split())))
        
    plen = len(pos)
    tree = [0 for _ in range(2 ** (int(math.log(plen, 2)) + 2))]
    tlen = len(tree)
    
    pos.sort(key = lambda x: x[1])
    
    temp = 0
    ty = []
    for i in range(len(pos)):
        if i > 0 and pos[i][1] != pos[i - 1][1]:
            temp += 1
        ty.append(temp)
    for i in range(len(pos)):
        pos[i][1] = ty[i]

    pos.sort(key = lambda x: (x[0], - x[1]))
    
    cnt = 0
    for i in range(plen):
        cnt += seg_sum(tree, 1, pos[i][1], plen - 1, 0, plen - 1)
        seg_inc(tree, pos[i][1], 1, 0, plen - 1)
    print(cnt)
    
