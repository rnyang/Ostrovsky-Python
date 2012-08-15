#!/bin/python

from ostrovsky import *

def toy_utility(agent, contracts):
	return 1

def toy_main():
	sys = System()
	agent0 = Agent(sys, utility, 0, 0)
	agent1 = Agent(sys, utility, 1, 1)
	agent2 = Agent(sys, utility, 2, 2)
	agents = [agent0, agent1, agent2]

	contract0 = Contract(sys, 1, 1, 0, 1, 0)
	contract1 = Contract(sys, 1, 1, 1, 2, 1)
	contracts = [contract0, contract1]

	sys.seed(agents, contracts)
	sys.generateArrows()

	pn = sys.minPreNetwork()
	print pn.arrowIds 

	n = pn.T_algorithm()
	print n.contractIds

def u0(agent, contracts):
	capacity = 1
	utility = 0
	for contract in contracts:
		if contract == ():
			continue

		if contract.originId == agent.id:
			capacity -= 1

		if contract.originId == agent.id and contract.targetId == 2:
			utility = 2

		if contract.originId == agent.id and contract.targetId == 3:
			utility = 1

	if capacity < 0:
		return -1
	else:
		return utility

def u1(agent, contracts):
	capacity = 1
	utility = 0

	for contract in contracts:
		if contract.originId == agent.id:
			capacity -= 1

		if contract.originId == agent.id and contract.targetId == 2:
			utility = 1

		if contract.originId == agent.id and contract.targetId == 3:
			utility = 2

	if capacity < 0:
		return -1
	else:
		return utility

def u2(agent, contracts):
	inputs = 0
	output = 0
	utility = 0

	for contract in contracts:
		#print contract.originId,

		if contract.originId == agent.id:
			output += 1
			if contract.targetId == 4:
				utility += 2
			else:
				utility += 1
		if contract.targetId == agent.id:
			inputs += 1
			if contract.targetId == 1:
				utility += 2
			else:
				utility += 1

	#print ""
	if inputs > 1 or output > 1 or inputs != output:
		return -1
	
	return utility

def u3(agent, contracts):
	inputs = 0
	output = 0
	utility = 0

	for contract in contracts:
		if contract.originId == agent.id:
			output += 1
			if contract.targetId == 5:
				utility += 2
			else:
				utility += 1
		if contract.targetId == agent.id:
			inputs += 1
			if contract.targetId == 0:
				utility += 2
			else:
				utility += 1

	if inputs > 1 or output > 1 or inputs != output:
		return -1
	
	return utility

def u4(agent, contracts):
	capacity = 1
	utility = 0

	for contract in contracts:
		if contract.targetId == agent.id:
			capacity -= 1

		if contract.targetId == agent.id and contract.originId == 3:
			utility = 2

		if contract.targetId == agent.id and contract.originId == 2:
			utility = 1

	if capacity < 0:
		return -1
	else:
		return utility

def u5(agent, contracts):
	capacity = 1
	utility = 0

	for contract in contracts:
		if contract.targetId == agent.id:
			capacity -= 1

		if contract.targetId == agent.id and contract.originId == 3:
			utility = 1

		if contract.targetId == agent.id and contract.originId == 2:
			utility = 2

	if capacity < 0:
		return -1
	else:
		return utility
    
def ostrovsky_ex1():
	sys = System()

	agents = []
	agents.append(Agent(sys, u0, 0, 0))
	agents.append(Agent(sys, u1, 0, 1))
	agents.append(Agent(sys, u2, 1, 2))
	agents.append(Agent(sys, u3, 1, 3))
	agents.append(Agent(sys, u4, 2, 4))
	agents.append(Agent(sys, u5, 2, 5))

	contracts = []
	contracts.append(Contract(sys, 1, 1, 0, 2, 0))
	contracts.append(Contract(sys, 1, 1, 0, 3, 1))
	contracts.append(Contract(sys, 1, 1, 1, 2, 2))
	contracts.append(Contract(sys, 1, 1, 1, 3, 3))

	contracts.append(Contract(sys, 1, 1, 2, 4, 4))
	contracts.append(Contract(sys, 1, 1, 2, 5, 5))
	contracts.append(Contract(sys, 1, 1, 3, 4, 6))
	contracts.append(Contract(sys, 1, 1, 3, 5, 7))

	sys.seed(agents, contracts)
	sys.generateArrows()

	pn = sys.minPreNetwork()
	n = pn.T_algorithm()

def uSup1(agent, contracts):
	capacity = 3
	revenue = 0
	cost = 0

	for contract in contracts:
		if contract.originId == agent.id:
			capacity -= 1
			revenue += contract.price * contract.qty

			# Transport costs
			if contract.targetId == 2:
				tcost = 1
			elif contract.targetId == 3:
				tcost = 3
			elif contract.targetId == 4:
				tcost = 2

			cost += tcost / 2.0

	if capacity < 0:
		return -100 # Impossible

	# Production Costs
	units = 3 - capacity
	if units == 3:
		cost += 45
	elif units == 2:
		cost += 20
	elif units == 1:
		cost += 5
	else:
		cost += 0

	# Calculate Profit
	profit = revenue - cost
	return profit

def uSup2(agent, contracts):
	capacity = 3
	revenue = 0
	cost = 0

	for contract in contracts:
		if contract.originId == agent.id:
			capacity -= 1
			revenue += contract.price * contract.qty

			# Transport costs
			if contract.targetId == 2:
				tcost = 2
			elif contract.targetId == 3:
				tcost = 3
			elif contract.targetId == 4:
				tcost = 4

			cost += tcost / 2.0

	if capacity < 0:
		return -100 # Impossible

	# Production Costs
	units = 3 - capacity
	if units == 3:
		cost += 45
	elif units == 2:
		cost += 20
	elif units == 1:
		cost += 5
	else:
		cost += 0

	# Calculate Profit
	profit = revenue - cost
	return profit

def uInt(agent, contracts):
	utility = 0
	revenue = 0
	cost = 0

	ustream = 0
	dstream = 0

	for contract in contracts:
		if contract.targetId == agent.id:
			ustream += 1.0
			cost += contract.price * contract.qty

			# Transport Costs
			if contract.originId == 0:
				tcost = 1
			elif contract.originId == 1:
				tcost = 2

			cost += tcost / 2.0

		if contract.originId == agent.id:
			dstream += 1
			revenue += contract.price * contract.qty

			# Transport Costs
			if contract.targetId == 3:
				tcost = 2
			elif contract.targetId == 4:
				tcost = 1

			cost += tcost / 2.0

	if ustream > 3 or dstream > 3 or dstream > ustream:
		return -100 # Impossible

	# Production Costs
	if dstream == 3:
		cost += 30
	elif dstream == 2:
		cost += 15
	elif dstream == 1:
		cost += 5

	profit = revenue - cost
	return profit

def uCons1(agent, contracts):
	utility = 0
	revenue = 0
	cost = 0

	for contract in contracts:
		if contract.targetId == agent.id:
			capacity -= 1

			# Price of Contract
			cost -= contract.price * contract.qty

			# Transport costs
			if contract.originId == 0:
				tcost = 3
			elif contract.originId == 1:
				tcost = 4
			elif contract.originId == 2:
				tcost = 2

			# Home Production costs
			if contract.originId == 0 or contract.originId == 1:
				hpcost = 11

			cost += tcost / 2.0
			cost += hpcost

	if capacity < 0:
		return -100 # Impossible

	# Utility from consumption
	units = 3 - capacity
	if units == 3:
		utility += 135
	elif units == 2:
		utility += 100
	elif units == 1:
		utility += 55

	# Calculate profit
	profit = utility - cost

	return profit

def uCons2(agent, contracts):
	utility = 0
	revenue = 0
	cost = 0

	for contract in contracts:
		if contract.targetId == agent.id:
			capacity -= 1

			# Price of Contract
			cost -= contract.price * contract.qty

			# Transport costs
			if contract.originId == 0:
				tcost = 2
			elif contract.originId == 1:
				tcost = 3
			elif contract.originId == 2:
				tcost = 1

			# Home Production costs
			if contract.originId == 0 or contract.originId == 1:
				hpcost = 11

			cost += tcost / 2.0
			cost += hpcost

	if capacity < 0:
		return -100 # Impossible

	# Utility from consumption
	units = 3 - capacity
	if units == 3:
		utility += 135
	elif units == 2:
		utility += 100
	elif units == 1:
		utility += 55

	# Calculate profit
	profit = utility - cost

	return profit

def ostrovsky_ex2():
	sys = System()

	agents = []
	agents.append(Agent(sys, uSup1, 0, 0))
	agents.append(Agent(sys, uSup2, 0, 1))
	agents.append(Agent(sys, uInt, 1, 2))
	agents.append(Agent(sys, uCons1, 2, 3))
	agents.append(Agent(sys, uCons1, 2, 4))

	contracts = []
	cid = 0
	for i in range(1,4):
		for j in range(0, 60, 10):
			contracts.append(Contract(sys, j, i, 0, 2, cid))
			cid += 1
			contracts.append(Contract(sys, j, i, 0, 3, cid))
			cid += 1
			contracts.append(Contract(sys, j, i, 0, 4, cid))
			cid +=1

			contracts.append(Contract(sys, j, i, 1, 2, cid))
			cid += 1
			contracts.append(Contract(sys, j, i, 1, 3, cid))
			cid += 1
			contracts.append(Contract(sys, j, i, 1, 3, cid))
			cid += 1

			contracts.append(Contract(sys, j, i, 2, 3, cid))
			cid += 1
			contracts.append(Contract(sys, j, i, 2, 4, cid))
			cid += 1

	sys.seed(agents, contracts)
	sys.generateArrows()
	pn = sys.minPreNetwork()
	n = pn.T_algorithm()

def main():
	print "======================================================================================== \n OSTROVSKY \n========================================================================================"
	ostrovsky_ex2()

main()