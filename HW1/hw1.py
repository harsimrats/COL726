import numpy as np

def var1(A):
	n = len(A)
	sumOfSquares = 0
	sumOfA = 0
	for i in range(0, len(A)):
		sumOfSquares += A[i]**2
		sumOfA += A[i]
	v1 = (sumOfSquares / float(n)) - (sumOfA / (float(n)))**2
	return v1

def var2(A):
	n = len(A)
	mean = 0
	for i in range(0, len(A)):
		mean += A[i]
	mean = mean / float(n)
	sumOfdiff = 0
	for i in range(0, len(A)):
		sumOfdiff += (A[i] - mean)**2
	v2 = sumOfdiff / float(n)
	return v2

def data1():
	A = [10e10 - 0.01, 10e10 + 0.00, 10e10 + 0.01]
	return A

A = [10e10 - 0.01, 10e10 + 0.00, 10e10 + 0.01]
# A = [-0.01, 0.00, 0.01]

v1 = var1(A)
v2 = var2(A)
print(v1, v2)