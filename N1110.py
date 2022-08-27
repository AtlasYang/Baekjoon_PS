#https://www.acmicpc.net/problem/1110
#2022.08.27.

n = int(input())

def func(num):
    if num < 10:
        return '0' + str(num)
    else:
        return str(num)

s = func(n)

res = None
cnt = 0
while res != n:
    res = int(s[0]) + int(s[1])
    s = s[1] + str(res)[-1]
    res = int(s)
    cnt += 1
    
print(cnt)
