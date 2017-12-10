def print_floyd_matrix(my_matrix):
	nodes = list(my_matrix.keys())
	for i in nodes:
		for j in nodes:
			print("\t" + str(my_matrix[i][j]), end="")
		print("")

def get_all_nodes(tree):
	return list(set(i[0] for i in tree))

def get_initial_dist_matrix(tree):
	dist_matrix = dict()
	node_names = get_all_nodes(tree)
	for i in node_names:
		dist_matrix[i] = dict()
		for j in node_names:
			dist_matrix[i][j] = 0 if i == j else 100000

	for start, end, length in tree:
		dist_matrix[start][end] = length

	return dist_matrix

def get_initial_path_matrix(tree):
	path_matrix = dict()
	node_names = get_all_nodes(tree)

	for i in node_names:
		path_matrix[i] = dict()
		for j in node_names:
			path_matrix[i][j] = None

	for start, end, length in tree:
		path_matrix[start][end] = start

	return path_matrix

def shortest_path_floyd(tree):
	size = len(get_all_nodes(tree))
	node_names = get_all_nodes(tree)
	dist_matrix = get_initial_dist_matrix(tree)
	path_matrix = get_initial_path_matrix(tree)

	for k in node_names:
		for i in node_names:
			for j in node_names:
				if dist_matrix[i][j] > dist_matrix[i][k] + dist_matrix[k][j]:
					dist_matrix[i][j] = dist_matrix[i][k] + dist_matrix[k][j]
					path_matrix[i][j] = path_matrix[k][j]
	return dist_matrix, path_matrix
