#https://www.acmicpc.net/problem/5419
#

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
        self.tree[idx] += value
        if start == end:
            return
        else:
            mid = (start + end) // 2
            self._update(idx, value, start, mid, node * 2)
            self._update(idx, value, mid + 1, end, node * 2 + 1)
    def update(self, idx, value):
        return self._update(idx, value, 0, self.arrlen - 1, 1)


def main():
    n = int(input())
    pos = []
    for _ in range(n):
        pos.append(tuple(map(int, sys.stdin.readline().strip().split())))
        
    cnt = 0
    
    return cnt


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        main()
