//Problem text at : https://www.hackerrank.com/challenges/swap-case

#!/bin/python

s = raw_input()
new_s = ''

for i in s :

	if i.islower() :

		new_s += i.upper()

	elif i.isupper() :

		new_s += i.lower()

	else :

		new_s += i

print new_s
