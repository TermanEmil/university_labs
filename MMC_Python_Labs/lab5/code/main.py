import copy
from read_stations import *
from utils import *

# Ex02
# Return the optimized version of the given stations.
# last_sqr_sum is the last sum of squared intervals. It's used to keep track if
# the new sum of squared intervals is bigger than the last one, if it is, then
# stop.
# At each iteration, for each transport, add a minute in all stations and
# calculate sum of sqruared intervals, then extract that minute. The sums are
# stored inside the dictionary sqr_intervals.
# For the transport the sum was the loswest, add back that minute.
def optimize_stations(stations, verbose = False):
	transport_nbs = get_all_transport_numbers(stations)
	last_sqr_sum = sum_of_sqrintervals_in_all_stations(stations)

	while True:
		sqr_intervals = dict()

		for tr_nb in transport_nbs:
			add_time_for_all_transport(tr_nb, stations, 1)
			sqr_intervals[tr_nb] = sum_of_sqrintervals_in_all_stations(stations)
			add_time_for_all_transport(tr_nb, stations, -1)

		best_transport_option = min(sqr_intervals, key=sqr_intervals.get)

		if sqr_intervals[best_transport_option] > last_sqr_sum:
			break
		else:
			last_sqr_sum = sqr_intervals[best_transport_option]
		add_time_for_all_transport(best_transport_option, stations, 1)

		if verbose:
			print("All squared intervals:", last_sqr_sum, best_transport_option)

	return stations

# Ex03
# First, each transport starts with an excesive number (starting_count).
# Then, for each transport, extract 1 while possible.
def find_optimal_transport_count(
	stations, traffic_load, transport_capacity, starting_count = 50
):
	transport_nbs = get_all_transport_numbers(stations)
	transport_count = dict((nb, starting_count) for nb in transport_nbs)

	for nb in transport_nbs:
		args = stations, traffic_load, transport_count, transport_capacity
		while transport_count_is_valid(*args):
			transport_count[nb] -= 1
			if transport_count[nb] < 0:
				break
		transport_count[nb] += 1
	return transport_count

stations = read_stations("./aux/stations/")
initial_stations = copy.deepcopy(stations)

traffic_load = \
{
	"eminescu -> kogalniceanu": 2370,
	"kogalniceanu -> puskin": 490,
	"kogalniceanu -> casa_presei": 1890,
	"casa_presei -> mihai_eminescu_theatre": 630,
	"casa_presei -> stefan_cel_mare": 1260,
	"licurici -> stefan_cel_mare": 980,
	"stefan_cel_mare -> asem": 2240,
	"asem -> circul": 2100,
	"circul -> vladimirescu": 300,
	"circul -> central_typography": 520,
	"circul -> kiev": 1300
}

print("\n Ex01 delta time in minutes:")
ex01_stations = \
{
	"stefan_cel_mare": stations["stefan_cel_mare"],
	"asem": stations["asem"],
	"circul": stations["circul"]
}
optimize_stations(ex01_stations)
print(get_delta_time(initial_stations, ex01_stations))

print("\n Ex02 delta time in minutes:")
optimize_stations(stations)
print(get_delta_time(initial_stations, stations))

print("\n Ex03 required number of transports:")
print(find_optimal_transport_count(stations, traffic_load, 70, 50))
