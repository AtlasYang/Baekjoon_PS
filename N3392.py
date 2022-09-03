import sys

maxlen = 30001

N = int(input())
M = [[0, 0, 0, 0] for _ in range(N)]
for i in range(N):
    M[i][0], M[i][1], M[i][2], M[i][3] = map(int, sys.stdin.readline().rstrip().split())

ST = [0 for _ in range(4 * maxlen)]
