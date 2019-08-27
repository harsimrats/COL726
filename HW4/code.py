import numpy as np
import matplotlib.pyplot as plt
from fcontour import *

class Conic:
	a, b, c, p, q, r = None,None,None,None,None,None
	def __init__(self, a, b, c, p, q, r):
		self.a = a
		self.b = b
		self.c = c
		self.p = p
		self.q = q
		self.r = r

	def evaluate(self, x):
		x1 = x[0]
		x2 = x[1]
		return (self.a * (x1**2) + self.b * x1 * x2 + self.c * (x2**2) + self.p * x1 + self.q * x2 + self.r)

	def jacobian(self, x):
		x1 = x[0]
		x2 = x[1]
		return (np.array([2 * self.a * x1 + self.b * x2 + self.p , 2 * self.c * x2 + self.b * x1 + self.q]))

	def linearize(self, x):
		def ftelda(y):
			x1,y1 = np.array(x), np.array(y)
			return (self.evaluate(x1) + np.dot(self.jacobian(x1), (y1-x1)))
		return ftelda

def newtonStep(conic1, conic2, x):
	s = np.linalg.solve(np.array([conic1.jacobian(x), conic2.jacobian(x)]), np.array([-1 * conic1.evaluate(x), -1 * conic2.evaluate(x)]))
	print([conic1.jacobian(x), conic2.jacobian(x)]), np.array([-1 * conic1.evaluate(x), -1 * conic2.evaluate(x)])
	return (s+x)
	