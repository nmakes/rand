from random import random

def rand(upperlim): #generate random number from 0 to upperlim-1
	n = int(upperlim)
	r = random()
	while n>=1:
		r = r*10
		n = int(n/10)
	r = int(r)
	r = r % (int (upperlim))
	return r

def randl(low, high): #generate random number from low to high-1
	c = rand(high)
	c = c % int(high-low)
	c += low
	return c

def randbitstr(size): #generate random bit string of length size
	bitstr = ""
	for i in range(size):
		bitstr += str(randl(0,2))
	return bitstr


def randbits(size):
	alphabet = [False, True]
	bits = []
	for i in range(size):
		bits.append(alphabet[rand(2)])
	return bits
