#https://www.acmicpc.net/problem/14340
#2022.04.10.

def f(n, k, t = 0):
	if t == 0:
		t = [list(range(1, n + 1)), ]
		
	tp = []
	h = [0 for _ in range(len(t))]
	
	for j in range(len(t)):
		r = t[j]
		for i in range(len(r) - 1):
			if r[i] + 1 == r[i + 1]:
				h[j] = 1
				tp.append(r[:i] + [0, 0] + r[i + 2:])
				
	for i in range(len(t)):
		if h[i] == 0:
			tp.append(t[i])
			
	if len(tp) == len(t):
		kcnt = 0
		for c in tp:
			if k not in c:
				kcnt += 1
		return len(t), kcnt
		
	else:
		return f(n, k, tp)
