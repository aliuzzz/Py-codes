#斐波那契数列
#递归法
def fib(n):
	assert n >= 0,"n>0"
	if n <=1:
		return n 
	return fib(n-1)+fib(n-2)

for i in range(1,20):
	print(fib(i), end = '')
	
#递推法
def fib_loop(n):
	a,b = 0,1
	for i in range(n+1):
	a,b = b,b+a
	return a 
for i in range(20):
	print(fib_loop(i), end = '')
	
#插入排序：
def insert_sort(ilist):
	for i in range(len(ilist)):
		for j in range(j):
			if ilist[i]<ilist[j]
				ilist.insert(j,list.pop(i))
				break
	return ilist