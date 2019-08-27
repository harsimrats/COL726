import numpy as np
from scipy import linalg
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import math

def split(img, n):
	h = len(img)
	w = len(img[0])
	C = []
	w1 = w//n
	h1 = h//n
	for indi in range(0, h1):
		for indj in range(0, w1):
			col = img[n*indi: n*(indi+1), n*indj: n*(indj+1), 0:3].flatten()
			C.append(col)
	return (np.array(C).transpose())

def join(C, n, w, h):
	orImg = np.zeros((h,w,3))
	jjj = 0
	jj = 0
	for j in range(0, len(C[0])):
		for i in range(0, len(C), 3):
			ii = i//3
			ind1 = ii%n
			ind2 = ii//n
			if jjj*n + ind1 == w:
				jj += 1
				jjj = 0
			for k in range(0, 3):
				temp = C[i+k][j]
				orImg[n*jj + ind2][jjj*n + ind1][k] = temp
		jjj += 1
	return orImg

def compress(C, r):
	U, S, Vh = linalg.svd(C, full_matrices = False)

	r = min(r, len(S))
	s = np.zeros((r,r))
	for i in range(0, r):
		s[i][i] = S[i]
	A = U[:,0:r] @ s
	B = Vh[0:r]

	errorRel = math.sqrt(np.sum((S[r:])**2)) / float(math.sqrt(np.sum(S**2)))
	return A, B, errorRel

def relError(img, img2):
	relE = np.linalg.norm(img - img2)/float(np.linalg.norm(img))
	return relE

# img = mpimg.imread('2.png')
# h = len(img)
# w = len(img[0])
# print(w,h)

# n = 16
# C = split(img, n)
# # print(np.array_equal(x,img))

# A, B, errorRel = compress(C, 16)
# cImg = join(A @ B, 16, w, h)

# imgplot = plt.imshow(cImg)
# plt.show()