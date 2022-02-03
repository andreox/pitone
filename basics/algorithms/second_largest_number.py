#!/bin/python

N = int(raw_input())
numbers = raw_input().split()

numbers = map(int,numbers)

numbers.sort()
last = numbers[len(numbers)-1]

while numbers[len(numbers)-1] == last :

	numbers.pop()

print numbers[len(numbers)-1]

