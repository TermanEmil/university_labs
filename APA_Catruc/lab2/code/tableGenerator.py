import pickle
from random import randint
import sys
import threading

class myThread (threading.Thread):
	def __init__(self, size):
		threading.Thread.__init__(self)
		self.size = size

	def run(self):
		makeFile(self.size)

def generateRandomTab(size):
	return [randint(-sys.maxsize, sys.maxsize) for _ in range(size)]

def makeFile(size):
	print(size)
	with open("randomNumbers/" + str(size), 'wb') as f:
		tab = generateRandomTab(size)
		pickle.dump(tab, f)

step = 1000
pointsLen = 10
lowerLimit = 10000
points = [lowerLimit + step * i for i in range(pointsLen)]

threads = []

for size in points:
	theardTmp = myThread(size)
	threads.append(theardTmp)

for thread in threads:
	thread.start()

for thread in threads:
	thread.join()