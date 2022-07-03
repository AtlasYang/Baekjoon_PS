#https://www.acmicpc.net/problem/5620
#2022.07.03.
#Timeout Code

import sys

n = int(sys.stdin.readline())
crd = []

for _ in range(n):
  crd.append(list(map(int, sys.stdin.readline().split())))

def dist(a, b):
  return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

def dist_list(a, b):
  if len(a) == 1 and len(b) == 1:
    return dist(a[0], b[0])
  else:
    mv = dist(a[0], b[0])
    for m in a:
      for n in b:
        t = dist(m, n)
        if t < mv:
          mv = t
    return mv

crd.sort(key = lambda x: x[0])
crdlist = []

p, f = 0, 1
for i in range(n - 1):
  if crd[i][0] == crd[i + 1][0]:
    f += 1
  else:
    crdlist.append(crd[p:f])
    p = f
    f += 1
crdlist.append(crd[p:f + 1])

res = dist_list(crdlist[0], crdlist[1])
for i in range(1, len(crdlist) - 1):
  t = dist_list(crdlist[i], crdlist[i + 1])
  if t < res:
    res = t

print(res)
