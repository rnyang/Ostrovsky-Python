#!/bin/python

import itertools
import util

# Wrapper around entire model
class System:

	# id's to be passed correspond 
	# to location in these lists

	def __init__(self):
		self.agents = []
		self.contracts = []

	def seed(self, agents, contracts):
		self.agents = agents # [Agent]
		self.contracts = contracts # [Contract]
		self.arrows = []

	def generateArrows(self):
		arrows = []
		n = 0

		for contractId in range(len(self.contracts)):
			downArrow = Arrow(self, contractId, self.contracts[contractId].originId, self.contracts[contractId].targetId, n)
			arrows.append(downArrow)
			n += 1
			upArrow = Arrow(self, contractId, self.contracts[contractId].targetId, self.contracts[contractId].originId, n)
			arrows.append(upArrow)
			n += 1

	# Downstream arrows only
	def minPreNetwork(self):
		arrows = range(0, len(self.arrows), 2)
		pn = PreNetwork(self, arrows)
		return pn

	# Upstream arrows only
	def maxPreNetwork(self):
		arrows = range(1, len(self.arrows), 2)
		pn = PreNetwork(self, arrows)
		return pn

class Prenetwork:
	def __init__(self, system, arrowIds):
		self.system = system
		self.arrowIds = arrowIds

	def T_iterate(self):

		arrows = []

		# For each agent in the system

		for agent in self.system.agents:
			contracts = []

			# Get all contracts that correspond to 
			# arrows pointing at the agent
			for arrow in self.arrows:
				if system.arrows[arrow].originId == agent.id:
					contracts.append(arrow.contractId)

			# For each contract, try adding it
			for contract in self.system.contracts:
				added_one = False

				if contract.id not in contracts:
					contracts.append(contract.id)
					added_one = True

				# Find the choice set of contracts
				choiceContracts = agent.choice(contracts)

				# Add those arrows from the origin among the choice set
				for arrow in self.system.arrows:
					if arrow.contractId in choiceContracts and arrow.originId == agent.id:
						if arrow.id not in arrows:
							arrows.append(arrow.id)

				# Pop the added contract
				if added_one:
					contracts.pop()

		return arrows

		# Check if we have a fixed point
		arrows.sort()
		self.arrowIds.sort()
		if arrows == self.arrowIds:
			self.arrowIds = arrows
			return true
		else:
			self.arrowIds = arrows
			return false

	def F_map(self):
		contracts = []

		for arrow in self.arrowIds:
			for arrow2 in self.arrowIds:
				if self.system.arrows[arrow].contractId == self.system.arrows[arrow2].contractId \
			    and self.system.arrows[arrow].originId == self.system.arrows[arrow2].targetId \
				and self.system.arrows[arrow].targetId == self.system.arrows[arrow2].originId:
					contracts.append(self.system.arrows[arrow].contractId)
		return contracts

	def T_algorithm(self):

		newArrows = self.T_iterate(self.arrowIds)
		newArrows.sort()
		self.arrowIds.sort()

		# Iterate to a fixed point
		while newArrows != self.arrowIds:
			self.arrowIds = newArrows
			newArrows = self.T_iterate(self.arrowIds)

			newArrows.sort()
			self.arrowIds.sort()

		# Apply F-map algorithm

		contracts = self.F_map()

		network = Network(self.system, contracts)

		return network

class Network:
	def __init__(self, system, contractIds):
		self.system = system
		self.contractIds = contractIds

class Arrow:
	def __init__(self, system, contractId, originId, targetId, id_):
		self.system = system
		self.contractId = contractId
		self.originId = originId
		self.targetId = targetId
		self.id = id_

class Contract:
	def __init__(self, system, price, qty, originId, targetId, id_):
		self.system = system
		self.price = price
		self.qty = qty
		self.originId = originId
		self.targetId = targetId
		self.id = id_

class Agent:
	def __init__(self, system, utility, level, id_):
		self.system = system
		self.utility = utility # [Contracts] -> Double
		self.level = level
		self.id = id_

	# Generates choice set of contracts
	def choice(self, contracts):

		# Generate power set of possible contracts

		allContractSets = util.powerset(contracts)
		maxU = 0

		for contractSet in allContractSets:
			u = self.utility(contractSet)
			if u > maxU:
				maxU = u
				maxContractSet = contractSet

		return contracts