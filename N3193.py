#https://acmicpc.net/problem/3193
#2022.08.28.
#Timeout Code

import sys

N, K = map(int, input().split())
brd, rot = [], []
for _ in range(N):
    brd.append(list(sys.stdin.readline().strip()))
for _ in range(K):
    rot.append(sys.stdin.readline().strip())

ball = []
for i in range(N):
    for j in range(N):
        if brd[i][j] == 'L':
            ball = [i, j]

def printbrd(b):
    for line in b:
        print(*line, sep='')
    return

def rotate(mat, ballpos):
    N = len(mat)
    t = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            t[j][N - 1 - i] = mat[i][j]
    for i in range(N):
        for j in range(N):
            mat[i][j] = t[i][j]
    x = ballpos[1]
    y = N - 1 - ballpos[0]
    ballpos[0] = x
    ballpos[1] = y
    return

def grav(mat, ballpos):
    maxlen = len(mat) - ballpos[0] - 1
    brd[ballpos[0]][ballpos[1]] = '.'
    for i in range(maxlen):
        x = ballpos[0] + 1
        y = ballpos[1]
        if brd[x][y] == 'X' or x >= len(mat):
            brd[x - 1][y] = 'L'
            return
        else:
            ballpos[0] = x
            ballpos[1] = y
            brd[x - 1][y] = '.'
            brd[x][y] = 'L'
            continue
    return

for cmd in rot:
    if cmd == 'D':
        rotate(brd, ball)
        grav(brd, ball)
        
    else:
        for _ in range(3):
            rotate(brd, ball)
        grav(brd, ball)

printbrd(brd)
        
