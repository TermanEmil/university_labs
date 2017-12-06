import time
import math
import matplotlib.pyplot as plt

from MinSpanTreeKruskal import *
from MinSpanTreePrim import *
from GenerateTree import *

def GetExecutionTime(f, data):
	startTime = time.time()
	f(data)
	endTime = time.time()
	return endTime - startTime

def GetExecutionDiagram(startTreeSize, deltaSize, pointsCount):
	diagram = dict()
	size = startTreeSize
	for i in range(pointsCount):
		tree = GenerateTree(size, 3)
		kruskalTime = GetExecutionTime(MinSpanTreeKruskal, tree)
		primTime = GetExecutionTime(MinSpanTreePrim, tree)
		diagram[size] = {
			'kruskalTime': kruskalTime,
			'primTime': primTime,
			'nodesCount': size,
			'vertsCount': size * 3
		}
		size += deltaSize

	return diagram

def DrawTimeDiagram(diagram):
	x = diagram.keys()
	values = diagram.values()

	yKruskal = [x['kruskalTime'] for x in values]
	yPrim = [x['primTime'] for x in values]
	# nodesCount = [x['nodesCount'] for x in values]
	# vertsCount = [x['vertsCount'] for x in values]

	plt.plot(x, yKruskal, label='Kruskal')
	plt.plot(x, yPrim, label='Prim')

	# actualPlot = [v * math.log(n, 2) for n, v in zip(nodesCount, vertsCount)]

	# plt.plot(x, [i * yKruskal[-1] / actualPlot[-1] for i in actualPlot])
	# plt.plot(x, [i * yPrim[-1] / actualPlot[-1] for i in actualPlot])

	plt.xlabel('x')
	plt.ylabel('time(x)')

	plt.legend()
	plt.show()

DrawTimeDiagram(GetExecutionDiagram(100, 1, 200))

# tree = GenerateTree(10, 3)
# print(MinSpanTreeKruskal(tree))
# print(MinSpanTreePrim(tree))
# print(GetExecutionTime(MinSpanTreeKruskal, tree))