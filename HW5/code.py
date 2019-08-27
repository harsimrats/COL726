import numpy as np
import matplotlib.pyplot as plt
from hw5 import *

def gradientDescentStep(f, g, x):
	delta_x = -g(x)
	t = 1.0
	alpha = 0.3
	beta = 0.5
	while (f(x + t * delta_x) > f(x) + alpha * t * np.dot(g(x), delta_x)):
		t = beta * t
	x_new = x + t * delta_x
	return x_new

def f(y):
	x = np.arange(-1.25, 1.5, 0.25)
	k_vel = 10.0
	k_obs = 0.1
	y1 = [0]+list(y)+[0]
	sumOfDiff = 0.0
	for i in range(1, 13):
	 	sumOfDiff += (y1[i] - y1[i-1])**2

	sumfObs = 0.0
	for i in range(1, 12):
	 	sumfObs += fObs([x[i-1], y1[i]])

	res = (k_vel * sumOfDiff / 2) + (k_obs * sumfObs)
	return res

def g(y):
	x = np.arange(-1.25, 1.5, 0.25)
	k_vel = 10
	k_obs = 0.1
	y1 = [0]+list(y)+[0]
	res = np.zeros(11)
	for i in range(1,12):
		res[i-1] = k_vel * (-1 * y1[i-1] + 2 * y1[i] - y1[i+1]) + k_obs * (gObs([x[i-1], y1[i]]))[1]
		
	return res

def Htilde():
	k_vel = 10
	H = np.zeros((11,11))
	for i in range(0, 11):
		if i == 10:
			H[i][i] = 2
		else:
			H[i][i] = 2
			H[i][i+1] = -1
			H[i+1][i] = -1
	return k_vel *  H

def steepestDescentStep(f, g, P, x):
	delta_x = - np.linalg.inv(P) @ g(x)
	t = 1.0
	alpha = 0.3
	beta = 0.5
	while (f(x + t * delta_x) > f(x) + alpha * t * np.dot(g(x), delta_x)):
		t = beta * t
	x_new = x + t * delta_x
	return x_new

