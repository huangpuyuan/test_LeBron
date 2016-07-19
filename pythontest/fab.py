#!/usr/bin/python

def fib(n):
	a,b=0,1
	while a < n:
		print a,
		a , b = b , a+b       #(a=b,b=a+b)
	print
fib(1000)


def fab(n):
	if n==1:
		return 1
	if n==0:	
		return 0
	else:
		return fab(n-1) + fab(n-2)

for i in range(30):
	print fab(i),

