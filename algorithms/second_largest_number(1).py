#!/bin/python

N = int(raw_input())
numbers = raw_input().split()

numbers = map(int,numbers)

last = max(numbers)

while max(numbers) == last :

	numbers.remove(last)

print max(numbers)

