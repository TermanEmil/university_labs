# A tree is composed of a list of tuples of size 3, where the last element
# in the tuple represents the length: ['A', 'B', 20]
def MinSpanTreeKruskal(tree):
	tree = sorted(tree, key=lambda i: i[2])

	nodeNames = list(set([i[0] for i in tree] + [i[1] for i in tree]))
	nodeGroups = [[i] for i in nodeNames]

	result = []
	for start, end, length in tree:
		startGroup = next(group for group in nodeGroups if start in group)
		endGroup = next(group for group in nodeGroups if end in group)

		if startGroup != endGroup:
			newGroup = startGroup + endGroup
			startGroup.extend(endGroup)
			nodeGroups.remove(endGroup)
			result.append((start, end, length))

		if len(nodeGroups) == 1:
			break

	return result
