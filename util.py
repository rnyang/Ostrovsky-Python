#!/bin/python

import itertools

def powerset(s):
	pset = []
	for i in range(len(s)+1):
		combs = itertools.combinations(s,i)
		pset.append(list(combs))

	return pset