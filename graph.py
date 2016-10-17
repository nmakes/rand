""" 
	Programming Experiment
	Course: Algorithms on Graphs
	Citation: October 2016, Coursera, UC San Diego

	Copyright (c) 2016 Naveen Venkat
"""

class dinode(object):
	
	# Ourward and Inward edges
	# outlist: list of node indices to which self points
	# inlist: list of all node indices which point to self

	# - TODO: Optimize Mem. and make efficient

	def __init__(self, ind):
		self.index = ind
		self.outlist = []
		self.inlist = []

	def join(self, node2): #one way connection
		if node2.index not in self.outlist:
			self.outlist.append(node2.index)
			node2.inlist.append(self.index)

	def bond(self, node2): #two way connection
		if node2.index not in self.outlist:
			self.outlist.append(node2.index)
			node2.inlist.append(self.index)
		if self.index not in node2.outlist:
			node2.outlist.append(self.index)
			self.inlist.append(node2.index)

	def unjoin(self, node2): #one way break
		if node2.index in self.outlist:
			self.outlist.remove(node2.index)
			node2.inlist.remove(self.index)

	def unbond(self, node2): #two way break. No way to traceback
		if node2.index in self.outlist:
			self.outlist.remove(node2.index)
			node2.inlist.remove(self.index)		
		if self.index in node2.outlist:
			node2.outlist.remove(self.index)
			self.inlist.remove(node2.index)

	def __str__(self):
		retstr = '['+str(self.index)+']' + ' -> '
		for i in self.outlist:
			retstr = retstr + str(i) + ' '
		retstr += '\n'
		for k in self.inlist:
			retstr = retstr + str(k) + ' '
		retstr = retstr + '-> ' + '['+str(self.index)+']'

	def show(self):
		print '['+str(self.index)+']' + ' ->',
		for i in self.outlist:
			print i,
		print
		for j in self.inlist:
			print j,
		print '-> ' + '['+str(self.index)+']'
		print


# TODO: Make digraph using multiple dinode

class digraph(object):

	def __init__(self):
		self.nodes = []

	def addnode(self, index):
		a = dinode(index)
		if a not in self.nodes:
			self.nodes.append(dinode(index))

	def delnode(self, index):
		for i in self.nodes:
			if index == i.index:
				self.nodes.remove(i)

	def getSCC(self):
		for i in self.nodes:


	def show(self):
		print '[',
		for i in self.nodes:
			print str(i.index),
		print ']'

""" -------------------------------- """

# g = digraph()

# g.addnode(1)
# g.addnode(2)
# g.addnode(3)
# g.addnode(4)

# g.show()

# g.delnode(3)

# g.show()