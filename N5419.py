#https://www.acmicpc.net/problem/5419
#

import math, sys

class SegTree:
    def __init__(self, arr):
        self.arr = arr[:]
        self.arrlen = len(arr)
        self.tree = [0 for _ in range(2 ** (int(math.log(self.arrlen, 2)) + 2))]
        self.init(1, 0, self.arrlen - 1)

    def init(self, node, start, end):
        if start == end:
            self.tree[node] = self.arr[start]
            return self.arr[start]
        else:
            mid = int((start + end) / 2)
            self.tree[node] = self.init(node * 2, start, mid) + self.init(node * 2 + 1, mid + 1, end)
            return self.tree[node]


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
