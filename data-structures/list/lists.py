#!/bin/python

n = int(raw_input())
a = []

for i in range(n) :

	inp_ut = raw_input().split()

	cmd = inp_ut[0]

	if cmd == 'print' :

		print a

	elif cmd == 'insert' :

		i = int(inp_ut[1])
		e = int(inp_ut[2])
		a.insert(i,e)

	elif cmd == 'remove' :

		e = int(inp_ut[1])
		a.remove(e)

	elif cmd == 'append' :

		e = int(inp_ut[1])
		a.append(e)

	elif cmd == 'sort' :

		a.sort()

	elif cmd == 'pop' :

		a.pop()

	elif cmd == 'reverse' :

		a.reverse()
