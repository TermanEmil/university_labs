import math

def MinSpanTreePrim(tree):
	nodeNames = list(set([i[0] for i in tree] + [i[1] for i in tree]))
	heapMap = dict((nodeName, math.inf) for nodeName in nodeNames)
	heapMap[tree[0][0]] = 0

	treeDict = dict()
	for start, end, length in tree:
		setKey = frozenset(sorted([start, end]))
		if setKey in treeDict:
			if length < treeDict[setKey]:
				treeDict[setKey] = length
		else:
			treeDict[setKey] = length

	vertsAndEdges = dict()
	while len(heapMap) != 0:
		minElement = min(heapMap, key=heapMap.get)
		del heapMap[minElement]

		for node in heapMap.keys():
			setKey = frozenset(sorted([node, minElement]))
			if setKey in treeDict and treeDict[setKey] < heapMap[node]:
				heapMap[node] = treeDict[setKey]
				vertsAndEdges[node] = [minElement, node, treeDict[setKey]]

	return sorted(list(vertsAndEdges.values()), key=lambda x: x[2])