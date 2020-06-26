#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import nested_scopes, generators, division, absolute_import, with_statement, print_function, unicode_literals
import random

SCORE_EMOJI=['😡', '🤮', '🤒', '🤕', '🖐', '💪', '👌', '😀', '😁', '😆', '🤣']

def plus(a, b):
	return a + b

def minus(a, b):
	return a - b

def times(a, b):
	return a * b

operations = [('+', plus, 0, 100), ('-', minus, 0, 100), ('x', times, 0, 10)]
score = 0


def print_problem(operator, a, b):
	problem_format = "{:>5}\n{}{:>4}\n-----"
	print(problem_format.format(a, operator, b))

def print_score(score):
	print("{} [Score: {}]".format(SCORE_EMOJI[score], score))

for _i in range(10):
	operator, funct, minimum, maximum = operations[random.randint(0,2)]
	a = random.randint(minimum, maximum)
	b = random.randint(minimum, maximum)
	while True:
		try:
			print_score(score)
			print_problem(operator, a, b)
			answer = int(raw_input().strip())
			break
		except ValueError:
			print("What? Please put in a number!")
	if answer == funct(a, b):
		print("😀 Correct\t:-)")
		score += 1
	else:
		print("😥 Sorry \t:-(")
	print("\n")

print_score(score)



