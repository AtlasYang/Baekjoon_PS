#https://www.acmicpc.net/problem/2174
#2022.08.28.

import sys

def main():
    
    #dir: 0, 1, 2, 3 = up, right, down, left
    card = {'N': 0, 'E': 1, 'S': 2, 'W': 3}
    mov = {'F': 0, 'R': 1, 'L': -1}
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    A, B = list(map(int, sys.stdin.readline().strip().split()))
    board = [[[0, 0] for _ in range(A)] for _ in range(B)]

    N, M = list(map(int, sys.stdin.readline().strip().split()))
    robots = []
    for i in range(N):
        p, q, r = sys.stdin.readline().strip().split()
        robots.append([int(p), int(q), card[r]])

    orders = []
    for _ in range(M):
        n, a, i = sys.stdin.readline().strip().split()
        orders.append((int(n) - 1, mov[a], int(i)))


    for order in orders:
        for _ in range(order[2]):
            if order[1] == 0:
                idx = robots[order[0]][2]
                robots[order[0]][0] += dx[idx]
                robots[order[0]][1] += dy[idx]
                if (robots[order[0]][0] not in range(1, A + 1)) or (robots[order[0]][1] not in range(1, B + 1)):
                    print(f'Robot {order[0] + 1} crashes into the wall')
                    return

                for i in range(N):
                    if (order[0] != i) and (robots[order[0]][:2] == robots[i][:2]):
                        print(f'Robot {order[0] + 1} crashes into robot {i + 1}')
                        return
                    
            else:
                robots[order[0]][2] = (robots[order[0]][2] + order[1]) % 4
                continue
                
    print('OK')
    return


if __name__ == '__main__':
    main()


