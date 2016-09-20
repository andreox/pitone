#!/bin/python

def isLeap(yr) :

	cnd = False
	if yr % 4 == 0 :

		cnd = True

		if yr % 100 == 0 and yr % 400 != 0 :

			cnd = False

	return cnd

year = int(raw_input()) 
print isLeap(year)
