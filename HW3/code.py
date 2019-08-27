from makeNetwork import *
import numpy as np
import matplotlib.pyplot as plt

def getB(network):
	m, tuples = network
	B = np.zeros(m)
	B[0] = -1
	return B

def applyA(network, v):
	m, tuples = network
	Av = np.zeros(m)
	Av[0] += v[0]
	Av[m-1] += v[m-1]
	for val in tuples:
		i, j, Rij = val
		Av[i] += (v[i] - v[j]) / Rij
		Av[j] += (v[j] - v[i]) / Rij
	return Av

def cg(Afun, b, tolerance):
	m = len(b)
	x = np.zeros(m)
	r = b.copy()
	p = r.copy()
	hisResNorm = []
	temp = (np.linalg.norm(r, ord = 2))/(np.linalg.norm(b, ord = 2))
	hisResNorm.append(temp)
	while temp > tolerance:
		Ap = Afun(p)
		alpha = np.dot(r, r) / np.dot(p, Ap)
		x_new = x + alpha * p
		r_new = r - alpha * Ap
		beta = np.dot(r_new,r_new) / np.dot(r, r)
		p_new = r_new + beta * p
		r = r_new
		x = x_new
		p = p_new
		temp = (np.linalg.norm(r, ord = 2))/(np.linalg.norm(b, ord = 2))
		hisResNorm.append(temp)
	return x, hisResNorm

def getDiag(network):
	m, tuples = network
	A = np.zeros(m)
	for val in tuples:
		i, j, Rij = val
		A[i] += 1/Rij
		A[j] += 1/Rij
	return A

def pcg(Afun, b, d, tolerance):
	M = d.copy()
	C = np.sqrt(M)
	Cin = 1/C
	y, hisResNorm2 = cg(lambda v: Cin*(Afun(Cin*v)), Cin*b, 10e-6)
	x = Cin * y
	return x, hisResNorm2

# random.seed(13)
# network = makeNetwork('wheatstone')
# network = makeNetwork('random1', 1000)
# network = makeNetwork('random2', 1000)
# x, hisResNorm = cg(lambda v: applyA(network, v), -getB(network), 10e-6)
# y, hisResNorm2 = pcg(lambda v: applyA(network, v), -getB(network), getDiag(network), 10e-6)

# plt.plot(np.log(hisResNorm), label='cg')
# plt.plot(np.log(hisResNorm2), label='pcg')
# plt.legend()
# plt.show()