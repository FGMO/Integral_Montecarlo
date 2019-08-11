from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as pp
from matplotlib import cm
import numpy as np
import random
import math

class Montecarlo:
		
	def f_xy(self, rndX, rndY, a, b, c, d):
		x = (b - a) * rndX + a
		y = (d - c) * rndY + c
		z = self.f_eval(x, y)
		return z
	
	def f_eval(self, x, y):
		return (4 * x * y - np.log(abs(x**2 - y**2)) * np.sin(x) * np.cos(y) + np.sqrt(x * y)) / (np.cos(x) * np.sin(y))
	
	def integral(self, a, b, c, d, n):
		suma = 0
		suma_aux = 0
		rndX = 0
		rndY = 0
		for i in range(n):
			rndX = random.random()
			rndY = random.random()
			aux = self.f_xy(rndX, rndY, a, b, c, d)
			suma += aux
			suma_aux += aux**2
		error = ((b - a) * (d - c) / n) * suma
		error_aux = (1 / n) * suma_aux
		
		return error, error_aux
	
	def graficar(self):
		fig = pp.figure()
		ax = fig.gca(projection='3d')
		x = np.arange(a, b, 0.1)
		y = np.arange(c, d, 0.1)
		x, y = np.meshgrid(x, y)
		f_xy = self.f_eval(x,y)
		surf = ax.plot_surface(x, y, f_xy, cmap=cm.coolwarm, linewidth=0, antialiased=False)
		ax.zaxis.set_major_locator(LinearLocator(10))
		ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
		ax.view_init(60, 40)

		for x_i in np.arange(a, b, 0.1):
			for y_i in np.arange(c, d, 0.1):
				f_xy_i =  self.f_eval(x_i, y_i)
				for i in np.arange(0, int(f_xy_i), 0.1):
					ax.scatter(x_i, y_i, i, marker="o", color="green",alpha=0.5)
		fig.colorbar(surf, shrink=0.5, aspect=5)
		pp.show()
		

if __name__ == '__main__':
	m = Montecarlo()
	a = 0
	b = 1
	c = 1
	d = 2
	
	n = 1
	error_esperado = 0.01
	error_real = 100
	
	while error_real > error_esperado:
		r1, r2 = m.integral(a, b, c, d, n)
		
		if (r2 - r1) > 0:
			error_real =  (b - a) * (d - c) * math.sqrt((r2-r1)/n)
			print('Resultado:', "{0:.4f}".format(r1), '\tError real:', "{0:.4f}".format(error_real),\
			 '\tError esperado:', "{0:.4f}".format(error_esperado), '\tN:', n)
		
		if error_real > error_esperado:
			n *= 10
			
	m.graficar()
	
