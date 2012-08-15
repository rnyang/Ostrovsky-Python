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

		self.arrows = arrows

	# Downstream arrows only
	def minPreNetwork(self):
		arrows = range(1, len(self.arrows), 2)
		pn = Prenetwork(self, arrows)
		return pn

	# Upstream arrows only
	def maxPreNetwork(self):
		arrows = range(0, len(self.arrows), 2)
		pn = Prenetwork(self, arrows)
		return pn

class Prenetwork:
	def __init__(self, system, arrowIds):
		self.system = system
		self.arrowIds = arrowIds

	def T_iterate(self):

		print "Calling Iteration of T-Algorithm"
		print "Initial Arrows: ", self.arrowIds

		arrows = []

		# For each agent in the system

		for agent in self.system.agents:
			print "Checking Agent ", agent.id
			contracts = [] # [Contract]

			# Get all contracts that correspond to 
			# arrows pointing at the agent
			for arrow in self.arrowIds:
				if self.system.arrows[arrow].targetId == agent.id:
					contracts.append(self.system.arrows[arrow].contractId)

			print "Contracts pointing at Agent ", agent.id, " are ", contracts

			# Create corresponding contract list to pass to choice function
			contractList = []
			for contract in contracts:
				contractList.append(self.system.contracts[contract])

			# For each contract, try adding it
			for contract in self.system.contracts:
				print "Testing Contract: ", contract.id
				added_one = False

				if contract.id not in contracts:
					contracts.append(contract.id)
					contractList.append(self.system.contracts[contract.id])
					added_one = True

				# Find the choice set of contracts
				choiceContracts = agent.choice(contractList)
				
				print 'choice contract set from ', contracts, ' = ',
				for c in choiceContracts:
					print c.id,
				print ""
				
				# Get list of choice contract id's
				choiceContractIds = []
				for c in choiceContracts:
					choiceContractIds.append(c.id)

				# Add the arrow from the choice set
				if contract.id in choiceContractIds:
					for arrow in self.system.arrows:
						if arrow.contractId == contract.id and arrow.originId == agent.id and arrow.id not in arrows:
							#print "Adding arrows: ", arrow.id
							arrows.append(arrow.id)

				#print 'choice contract ids: ', choiceContractIds

				# Pop the added contract
				if added_one:
					contracts.pop()
					contractList.pop()

			#print "arrows so far: ", arrows

		print "Final Arrows:   ", arrows

		return arrows

	def F_map(self):
		print "Applying F-map Algorithm"
		contracts = []

		for arrow in self.arrowIds:
			for arrow2 in self.arrowIds:
				if self.system.arrows[arrow].contractId == self.system.arrows[arrow2].contractId \
			    and self.system.arrows[arrow].originId == self.system.arrows[arrow2].targetId \
				and self.system.arrows[arrow].targetId == self.system.arrows[arrow2].originId \
				and self.system.arrows[arrow].contractId not in contracts:
					contracts.append(self.system.arrows[arrow].contractId)
		print "Final Contracts: ", contracts
		return contracts

	def T_algorithm(self):

		print "Running T-Algorithm"

		newArrows = self.T_iterate()
		newArrows.sort()
		self.arrowIds.sort()

		"""

		# Iterate to a fixed point
		
		while newArrows != self.arrowIds:
			self.arrowIds = newArrows
			newArrows = self.T_iterate()

			newArrows.sort()
			self.arrowIds.sort()

		print "Fixed Point Reached"
		
		"""

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
		
		print "choosing from: ",
		for c in contracts:
			print c.id,
		print ""
		

		# Generate power set of possible contracts

		allContractSets = util.powerset(contracts)
		maxU = 0
		maxContractSet = []

		for contractSet in allContractSets:
			u = self.utility(self,contractSet)

			if u > maxU:
				maxU = u
				maxContractSet = contractSet

		return maxContractSet