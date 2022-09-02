#https://www.acmicpc.net/problem/5419
#2022.09.02.

#Without SegTree Class: Not Completed
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
        tree[node] = seg_sum(tree, node * 2, start, end, s, mid) + seg_sum(tree, node * 2 + 1, start, end, mid + 1, e)
        return tree[node]


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

    pos.sort(key = lambda x: x[0] * (10 ** 9) - x[1])
    
    cnt = 0
    for i in range(len(pos)):
        cnt += seg_sum(tree, 1, pos[i][1], tlen - 1, 0, plen - 1)
        seg_inc(tree, pos[i][1], 1, 0, plen - 1)
    print(cnt)




#Orginal Timeout Code
import math, sys

class SegTree:
    def __init__(self, arr):
        self.arr = arr[:]
        self.arrlen = len(arr)
        self.tree = [0 for _ in range(2 ** (int(math.log(self.arrlen, 2)) + 2))]
        self.idxlist = arr[:]
        self._init(1, 0, self.arrlen - 1)
        self.treelen = max(self.idxlist)

    def _init(self, node, start, end):
        if start == end:
            self.tree[node] = self.arr[start]
            self.idxlist[start] = node
            return self.arr[start]
        else:
            mid = int((start + end) / 2)
            self.tree[node] = self._init(node * 2, start, mid) + self._init(node * 2 + 1, mid + 1, end)
            return self.tree[node]

    def _sum(self, start, end, node, s, e):
        if end < s or e < start:
            return 0
        elif start <= s and e <= end:
            return self.tree[node]
        else:
            mid = (s + e) // 2
            return self._sum(start, end, node * 2, s, mid) + self._sum(start, end, node * 2 + 1, mid + 1, e)
    def sum(self, start, end):
        return self._sum(start, end, 1, 0, self.arrlen - 1)

    def _update(self, idx, value, start, end, node):
        if idx < start or idx > end:
            return
        self.tree[node] += value
        if start == end:
            return
        else:
            mid = (start + end) // 2
            self._update(idx, value, start, mid, node * 2)
            self._update(idx, value, mid + 1, end, node * 2 + 1)
    def update(self, idx, value):
        return self._update(idx, value, 0, self.arrlen - 1, 1)


def main():
    n = int(sys.stdin.readline().strip())
    pos = []
    for _ in range(n):
        pos.append(list(map(int, sys.stdin.readline().strip().split())))

    pos.sort(key = lambda x: x[1])
    temp = 0
    ty = []
    for i in range(len(pos)):
        if i > 0 and pos[i][1] != pos[i - 1][1]:
            temp += 1
        ty.append(temp)
    for i in range(len(pos)):
        pos[i][1] = ty[i]
        
    pos.sort(key = lambda x: x[0] * (10 ** 9) - x[1])

    #seg = SegTree([0 for _ in range(75000)])
    seg = SegTree([0 for _ in range(len(pos))])
    
    cnt = 0
    for i in range(len(pos)):
        cnt += seg.sum(pos[i][1], seg.treelen - 1)
        seg.update(pos[i][1], 1)
    return cnt


if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        print(main())
        
        
