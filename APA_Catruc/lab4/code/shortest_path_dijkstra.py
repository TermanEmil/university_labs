import math

# Transforms from [[start_node_1, end_node_1, len], ...] to
# {(start_node_1, end_node_1): len, ...} choosing the smallest length.
def tree_to_dict(tree):
	tree_dict = dict()
	for start, end, length in tree:
		dict_key = (start, end)
		if dict_key in tree_dict:
			if length < tree_dict[dict_key]:
				tree_dict[dict_key] = length
		else:
			tree_dict[dict_key] = length
	return tree_dict

def shortest_path_dijkstra(tree):
	node_names = list(set(i[0] for i in tree))
	heap_map = dict((node_name, math.inf) for node_name in node_names)
	starting_node = tree[0][0]
	heap_map[starting_node] = 0
	tree = tree_to_dict(tree)

	dist_to_all_nodes = {starting_node: 0}
	best_connections = dict((node_name, None) for node_name in node_names)

	while len(heap_map) != 0:
		min_element = min(heap_map, key=heap_map.get)
		dist_to_all_nodes[min_element] = heap_map[min_element]
		dist_to_here = dist_to_all_nodes[min_element]
		del heap_map[min_element]

		for node in heap_map.keys():
			tree_key = tuple(sorted((node, min_element)))
			if tree_key in tree and tree[tree_key] + dist_to_here < heap_map[node]:
				heap_map[node] = dist_to_here + tree[tree_key]
				best_connections[node] = min_element

	return dist_to_all_nodes, best_connections
