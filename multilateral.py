#!/bin/python

"""
	PROBLEM: Solving the Multilateral Matching problem will require a optimization routine to maximize aggregate utility over venture allocations.
	Such a routine would be 
"""

class System:
	def __init__(agents, ventures):
		self.agents = agents # [Agent]
		self.ventures = ventures # [Venture]

	def efficient():
		# Maximize sum of utility of agents

class Agent:
	def __init__(sys, utility, id_):
		self.sys = sys
		self.utility = utility # Valuation Function: [Double] -> Double
		self.id = id_

class Venture:
	def __init__(sys, r_max, id_):
		self.sys = sys
		self.r_max = r_max # Maximum Participation in Venture
		self.id = id_

def main():
	print 'whee'

main()