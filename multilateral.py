#!/bin/python

"""
	PROBLEM: Solving the Multilateral Matching problem will require a optimization routine to maximize aggregate utility over venture allocations.
	Such a routine would be 
"""

class System:
	def __init__(agents, ventures):
		self.agents = agents # [Agent]
		self.ventures = ventures # [Venture]

	def max_utility():
		continue


	# [Double] -> Double
	# Allocation = [r_omega, r_psi]
	def utility(allocation):
		utility = 0
		for agent in self.agents:
			utility += agent.utility(allocation)

		return utility

class Agent:
	def __init__(sys, utility, id_):
		self.sys = sys
		self.utility = utility # Valuation Function: [Double] -> Double
		self.id = id_

"""
# Sample Utility Function
# from Multilateral Matching pg. 7

def utility_buyer(allocation):
	utility = 32 * min(allocation[1], 50)
	return utility

"""

class Venture:
	def __init__(sys, r_max, id_):
		self.sys = sys
		self.r_max = r_max # Maximum Participation in Venture : Double
		self.id = id_ # Int

def main():
	print 'whee'

main()