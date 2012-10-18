#!/bin/python

"""
	PROBLEM: Solving the Multilateral Matching problem will require a optimization routine to maximize aggregate utility over venture allocations.
"""

""" 
	Subgradient Method for Solving Multilateral Matching problem
"""

# Finds the gradient at current point
# ( [Float] -> Float ) -> [Float] -> [Float]

# func : function to be minimized
# x0    : current point to find gradient
def gradient(func, x0):
	dx = .01
	x1 = x0[:]

	grad = []

	for i in range(len(x0)):
		# Shift by marginal amount
		x1[i] += dx

		# Calculate gradient
		dy = func(x1) - func(x0)
		grad.append(dy / dx)

		# Shift back
		x1[i] -= dx

	return grad

# Finds the gradient at current point, multiplies it by the step size, and adds to current best guess
# [Float] -> ( [Float] -> [Float] ) -> [Float]

# func : function to be minimized
# x0    : current step to be iterated
def subgradient_iterate(func, x0):
	step_size = 0.1

	grad = gradient(func, x0)
	step = []

	for i in range(len(grad)):
		step.append(step_size * grad[i])

	x1 = []

	for i in range(len(x0)):
		x1.append(x0[i] - step[i])

	#x1 = [(x0[i] + step[i]) for i in range(len(x0)]
	return x1

# Solves for minimal point using subgradient method
# ( [Float] -> [Float] ) -> [Float] -> [Float]

# func : function to be minimized
# x0    : initial guess
def subgradient_minimize(func, x0):
	curr = x0
	guesses = [x0]

	cc = 0

	while cc < 100:
		next = subgradient_iterate(func, curr)
		guesses += [next]
		curr = next

		print "Curr: ",curr
		print "F(Curr): ", func(curr)

		cc = cc + 1

	f_guesses = map(func, guesses)
	best = min(f_guesses)

	return guesses[f_guesses.index(best)]

"""
	End Subgradient Method
"""

def f_ex(x):
	#print x
	return (x[0] - 1)**2 + (x[1] - 2)**2

def subg_test():
	x0 = [0.5,0.5]
	f = f_ex

	grad = gradient(f, x0)
	print "Gradient = ", grad

	min = subgradient_minimize(f,x0)
	print "Min at: ",min

"""
	OLD STUFF
"""

class System:
	def __init__(agents, ventures):
		self.agents = agents # [Agent]
		self.ventures = ventures # [Venture]

	def max_utility():
		return


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
	subg_test()

main()