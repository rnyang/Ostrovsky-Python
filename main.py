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

def main():
	print "======================================================================================== \n OSTROVSKY \n========================================================================================"
	ostrovsky_ex1()

main()