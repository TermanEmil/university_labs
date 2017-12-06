import random

def GenerateTree(size, nodeConnections):
	nodes = [x for x in range(size)]

	tree = []
	for node in nodes:
		for i in range(nodeConnections):
			start = node
			end = random.choice([x for x in nodes if x != node])
			length = random.randint(0, 100)
			tree.append([start, end, length])
	return tree