from cmath import *
from numpy import *
import scipy.misc as smp
import imageio
import sys

g_maxAllowedEscVel = 1000

def		EscVel(z0, c, N):
	z = z0
	for n in range(N):
		if abs(z) > 2:
			break
		z = z ** 2 + c
	return n

def		JuliaSet(zMax, c, N, width, height):
	matrix = [[EscVel(complex(x, y), c, N)
		for x in linspace(-zMax, zMax, width)]
			for y in linspace(-zMax , zMax, height)]
	return matrix

def		_getColor(escVelMatrix):
	gradient = escVelMatrix / double(g_maxAllowedEscVel)
	
	if gradient == 1:
		color = [0, 0, 0]
	else:
		color = [250 * gradient, 250 * gradient, min(5 * gradient * 255, 80)]
	return color

def		DrawFractal(escVelMatrix, width, height):
	data = zeros((width, height, 3), dtype = uint8)

	for i in range(height):
		for j in range(width):
			if escVelMatrix[i][j] != 0:
				color = _getColor(escVelMatrix[i][j])
				data[i][j] = color
	img = smp.toimage(data)
	return img

def		_MakeGifLinespace(nb, delta, n):
	tab = linspace(nb - delta, nb + delta, n)
	return append(tab, linspace(nb + delta, nb - delta, n))


def		MakeFractalGif(zMax, N, c, width, height, nImgs, r, zMaxDelta):
	a = linspace(0, 2 * pi, nImgs)
	zMaxLin = _MakeGifLinespace(zMax, zMaxDelta, nImgs / 2)
	images = []

	for i in range(nImgs):
		sys.stdout.write("\rDone: " + str(float(i) / nImgs) + "%   ")
		sys.stdout.flush()

		_c = complex(r * cos(a[i]), r * sin(a[i])) + c
		img = DrawFractal(JuliaSet(zMaxLin[i], _c, N, width, height), width, height)

		fileName = 'images/img_' + str(i) + '.png'
		smp.imsave(fileName, img)
		images.append(imageio.imread(fileName))

	imageio.mimsave('fractal.gif', images)
	print("\rDone: 100%    ")

width =  50
height = 50
zMax = 1

r = 0.81
c = 0

print("Making a gif. It may take a while")
MakeFractalGif(zMax, g_maxAllowedEscVel, c, width, height, 100, r, -0)
print("Check out the gif")