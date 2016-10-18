from rand import *

'''
#---

class genome(object):
	cells = []
	origin = []

	def __init__(self, cells):
		self.cells = cells

	def generate(self,size):
		for i in range(size):
			self.origin.append(self.cells[rand(len(self.cells))])
		return self.origin

	def __str__(self):
		retstr = ""
		for w in self.origin:
			retstr+=str(w)
		return retstr


#---

dna = genome(['-','A','T','C','G'])
print dna.cells
print dna.origin
t = dna.generate(30)
print dna

'''