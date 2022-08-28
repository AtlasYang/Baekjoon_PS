#https://www.acmicpc.net/problem/6087
#2022.08.28.
#Timeout Code

from collections import deque
import sys, copy

W, H = tuple(map(int, sys.stdin.readline().strip().split()))

board = []
for _ in range(H):
    board.append(list(sys.stdin.readline().strip()))

C_pos = []
for i in range(H):
    for j in range(W):
        if board[i][j] == 'C':
            C_pos.append([i, j])

pos = C_pos[0]
board[pos[0]][pos[1]] = 'c'

m_num = 100000
m_num_list = []

dirlist = [[-1, 0], [0, 1], [1, 0], [0, -1]]
#direction: 0, 1, 2, 3 = up, right, down, left

def search(present, visited, mirror, d):
    global m_num
    
    if mirror >= m_num:
        return
    
    t = present[:]
    v = copy.copy(visited)
    ipos = t[:]

    if (t[0] not in range(H)) or (t[1] not in range(W)) or (t in v):
        return
    
    char = board[t[0]][t[1]]
    
    if char == '*':
        return
    elif char == 'C':
        m_num_list.append(mirror)
        if mirror < m_num:
            m_num = mirror
        return
    else:
        t[0] += dirlist[d][0]
        t[1] += dirlist[d][1]
        v.append(ipos[:])
        
        search(t, v, mirror + 1, (d + 1) % 4)
        search(t, v, mirror + 1, (d - 1) % 4)
        search(t, v, mirror, d)
        return


visit = deque()
for i in range(4):
    search(pos, visit, 0, i)
    
print(m_num)

