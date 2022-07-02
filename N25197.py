#https://www.acmicpc.net/problem/25197
#2022.07.02.
#Timeout Code

from math import factorial
import sys

sys.setrecursionlimit(10 ** 6)

def C(a, b):
  if a == 1:
    if b == 1:
      return 1
    else:
      return 0
  else:
    return int(factorial(a) / (factorial(b) * factorial(a - b)))


def P(a, b):
  if b == 2:
    res = []
    for i in range(1, a):
      res.append([i, a - i])
    return res
  else:
    res = []
    for i in range(1, a - b + 2):
      pre = P(a - i, b - 1)
      for case in pre:
        res.append([i, ] + case)
    return res


def V(a, b):
  if b == 1:
    return C(a, 2)
  else:
    res = 0
    tlist = P(a, b)
    for case in tlist:
      temp1 = 1
      temp2 = 0
      ta = a
      for num in case:
        temp1 *= C(ta, num)
        temp2 += C(num, 2)
        ta -= num  
      res += temp1 * temp2
    return V(a, b - 1) * b + res
    
n, k = list(map(int, input().split()))
ans = V(n, k) / (k ** n)
print(ans)
