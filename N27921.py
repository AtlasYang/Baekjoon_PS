def main():
    a, b = [], []
    h1, w1 = map(int, input().split())
    for i in range(h1):
        a.append(list(input()))
    h2, w2 = map(int, input().split())
    for i in range(h2):
        b.append(list(input()))
    
    num = 0
    for row in a:
        num += row.count('O')

    
    overlapCnt = []
    for i in range(w1 + w2 - 1):
        for j in range(h1 + h2 - 1):
            cnt = 0
            for k in range(h2):
                for l in range(w2):
                    aRow = k + j
                    aCol = l + i
                    if aRow < h1 and aCol < w1:
                        print(aRow, aCol)
                        print(a[aRow][aCol], b[k][l])
                        print(a[aRow][aCol] == 'O' and b[k][l] == 'O')
                        print()
                        if a[aRow][aCol] == 'O' and b[k][l] == 'O':
                            cnt += 1
                    
            overlapCnt.append(cnt)
    print('num: ', num)
    print('overlapCnt: ', overlapCnt)
    print(num - max(overlapCnt))


if __name__ == '__main__':
    main()