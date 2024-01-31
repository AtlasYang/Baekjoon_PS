def main():
    n = int(input())
    inputList = []
    for _ in range(n):
        inputList.append(list(input()))
    
    for cmd in inputList:
        x, y = 0, 0
        xUpper, yUpper = 0, 0
        xLower, yLower = 0, 0
        dir = 0 # 0: N, 1: E, 2: S, 3: W
        for c in cmd:
            if c == 'F':
                if dir == 0:
                    y += 1
                elif dir == 1:
                    x += 1
                elif dir == 2:
                    y -= 1
                elif dir == 3:
                    x -= 1
            elif c == 'B':
                if dir == 0:
                    y -= 1
                elif dir == 1:
                    x -= 1
                elif dir == 2:
                    y += 1
                elif dir == 3:
                    x += 1
            elif c == 'L':
                dir = (dir - 1) % 4
            elif c == 'R':
                dir = (dir + 1) % 4
            xUpper = max(xUpper, x)
            yUpper = max(yUpper, y)
            xLower = min(xLower, x)
            yLower = min(yLower, y)
        x = xUpper - xLower
        y = yUpper - yLower
        print(abs(x * y))

if __name__ == '__main__':
    main()