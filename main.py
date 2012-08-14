#!/bin/python

import ostrovsky

def utility(agent, contracts):
	return 1

def main():
	sys = ostrovsky.System()
	agent0 = ostrovsky.Agent(sys, utility, 0, 0)
	agent1 = ostrovsky.Agent(sys, utility, 1, 1)
	agent2 = ostrovsky.Agent(sys, utility, 2, 2)
	agents = [agent0, agent1, agent2]

	contract0 = ostrovsky.Contract(sys, 1, 1, 0, 1, 0)
	contract1 = ostrovsky.Contract(sys, 1, 1, 1, 2, 1)
	contracts = [contract0, contract1]

	sys.seed(agents, contracts)
	sys.generateArrows()


main()