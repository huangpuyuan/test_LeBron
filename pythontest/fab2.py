#!/usr/bin/python

def fib(n):
	a,b=0,1
	while a < n:
		print a,
		a , b = b , a+b       #(a=b,b=a+b)
	print
fib(1000)

import datetime



def fib1(n):
	if n==1:
		return 1
	if n==0:	
		return 0
	else:
		return fib1(n-1) + fib1(n-2)

known = {0:0,1:1}

def fib2(n):
	if n in known:
		return known[n]
	res=fib2(n-1)+ fib2(n-2)
	known[n]=res
	return res

n=40
print(datetime.date.now())
print('fib1(%d)=%d' % (n,fib1(n)))
print(datetime.date.now())
print('fib2(%d)=%d' % (n,fib2(n)))
print(datetime.date.now())

