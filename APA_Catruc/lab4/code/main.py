import matplotlib.pyplot as plt
import time

from tree_generator import *
from shortest_path_floyd import shortest_path_floyd, print_floyd_matrix
from shortest_path_dijkstra import shortest_path_dijkstra

def get_execution_time(f, data):
	startTime = time.time()
	f(data)
	endTime = time.time()
	return endTime - startTime

def get_execution_diagram(start_tree_size, delta_size, trees_count):
	diagram = dict()
	size = start_tree_size

	for i in range(trees_count):
		tree = tree_generator(size, 3)
		dijkstra_time = get_execution_time(shortest_path_dijkstra, tree)
		floyd_time = get_execution_time(shortest_path_floyd, tree)

		diagram[size] = {
			'dijkstra': dijkstra_time,
			'floyd': floyd_time,
			'size': size
		}
		size += delta_size
	return diagram

def draw_time_diagram(diagram):
	x = diagram.keys()
	values = diagram.values()

	y_dijkstra = [x['dijkstra'] for x in values]
	y_floyd = [x['floyd'] for x in values]

	plt.plot(x, y_dijkstra, "ro", label="Dijkstra")
	# plt.plot(x, y_floyd, 'bo', label="Floyd")

	plt.xlabel("nodes count")
	plt.ylabel("time (s)")

	plt.legend()
	plt.show()

def demonstrate_dijkstra():
	tree = \
	[
		['A', 'B', 5],
		['A', 'E', 2],
		['A', 'D', 9],
		['B', 'C', 2],
		['C', 'D', 3],
		['D', 'F', 2],
		['E', 'F', 3],
		['F', 'D', 2],
	]
	print(shortest_path_dijkstra(tree))

def demonstrate_floyd():
	tree = \
	[
		[0, 3, 15],
		[0, 1, 3],
		[0, 2, 6],
		[1, 2, -2],
		[2, 3, 2],
		[3, 0, 1]

	]

	d, p = shortest_path_floyd(tree_floyd)
	print_floyd_matrix(d)
	print("")
	print_floyd_matrix(p)

# demonstrate_dijkstra()
# demonstrate_floyd()

draw_time_diagram(get_execution_diagram(30, 1, 100))