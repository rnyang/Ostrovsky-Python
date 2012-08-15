#!/bin/python

import itertools

def powerset(s):
	pset = []
	for i in range(len(s)+1):
		combs = itertools.combinations(s,i)
		for c in list(combs):
			pset.append(c)
	return pset

def main():
	s = [1,2,3]
	p = powerset(s)

