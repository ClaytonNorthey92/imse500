import matplotlib.pyplot as plt

X_AXIS = range(-10, 10)
Y_AXIS = X_AXIS

if __name__=='__main__':
	line_tmp = [[] for x in range(4)]
	print line_tmp
	print line_tmp[0]
	for x in X_AXIS:
		line_tmp[0].append((x-3)*(0-1))
		line_tmp[1].append(float(x)/4.0 + 2)
		line_tmp[2].append(5*x + 1)
		line_tmp[3].append(-2*x + 5)
	for line in line_tmp:
		plt.plot(X_AXIS, line)
	plt.plot([-10, 0,0.8, 10], [-10*2.75, 0, 2.2, 10*2.75], 'b--')
	plt.ylim(X_AXIS[0], X_AXIS[-1])
	plt.grid(True)
	plt.show()