def partA():
	visualizeObs()
	x = np.zeros(2)
	xx = []
	yy = []
	for k in range(0,20):
		x = gradientDescentStep(fObs, gObs, x)
		xx.append(x[0])
		yy.append(x[1])

	plt.scatter(xx, yy, s=10, color='darkred')
	plt.show()

def partB():
	visualizeObs()
	y = np.zeros(11)
	xx = []
	yy = []
	norm = []
	for k in range(0,20):
		y = gradientDescentStep(f, g, y)
		norm.append(np.linalg.norm(g(y)))

	xx.append(-1.5)
	yy.append(0)
	for i in range(1, 12):
		xx.append(-1.5 + 0.25*i)
		yy.append(y[i-1])
	xx.append(1.5)
	yy.append(0)

	plt.scatter(xx, yy, s=10, color='darkred')
	plt.show()

	plt.plot(norm)
	plt.yscale('log')
	plt.show()

def partC():
	visualizeObs()
	y = np.zeros(11)
	xx = []
	yy = []
	norm = []
	for k in range(0,20):
		y = steepestDescentStep(f, g, Htilde(), y)
		norm.append(np.linalg.norm(g(y)))

	xx.append(-1.5)
	yy.append(0)
	for i in range(1, 12):
		xx.append(-1.5 + 0.25*i)
		yy.append(y[i-1])
	xx.append(1.5)
	yy.append(0)

	plt.scatter(xx, yy, s=10, color='darkred')
	plt.show()

	plt.plot(norm)
	plt.yscale('log')
	plt.show()

partC()