#Problem text at : https://www.hackerrank.com/challenges/finding-the-percentage

#!/bin/python

def average(a) :

	return ( a[0]+a[1]+a[2] )/3

N = int(raw_input())
dictionary = {} 

for i in range(N) :

	in_put = raw_input().split()

	name = in_put[0]
	a = in_put[1:]
	a = map(float,a)

	dictionary[name] = a 

name = raw_input()

print format(average(dictionary[name]),'.2f')
