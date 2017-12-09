import itertools as ittools
import math

# Get a list of all transport numbers: [2, 7, 10, ...].
def get_all_transport_numbers(stations):
	transport_nbs = []
	for st_name, st_transports in stations.items():
		transport_nbs += st_transports.keys()
	return sorted(list(set(transport_nbs)))

# For the given transports: {nb1: [t11, t12, ...], nb2: [t21, t22, ...]}
# return a sorted list of their time arivals.
def get_time_arivals(tranports):
	return sorted(list(ittools.chain.from_iterable(
		[time_arivals for _, time_arivals in tranports.items()])
	))

# For the given list of time arivals (list of ints), get another list with the
# intervals between these times.
def get_intervals(time_arivals):
	result = []
	for i in range(len(time_arivals) - 1):
		result.append(time_arivals[i + 1] - time_arivals[i])
	return result

# Get the sum of squared intervals.
def sum_squared_intervals(time_arivals):
	return sum(map(lambda x: x**2, get_intervals(time_arivals)))

# Get the sum of squared intervals, in every station.
def sum_of_sqrintervals_in_all_stations(stations):
	total = 0
	for st_name, st_transports in stations.items():
		total += sum_squared_intervals(get_time_arivals(st_transports))
	return total

# Add the given time, to the time arivals of the given transports for the
# given transport_nb.
def add_time_for_transport(transport_nb, transports, time):
	transports[transport_nb] = [t + time for t in transports[transport_nb]]

# Add time for all transports of transport_nb in all given stations.
def add_time_for_all_transport(transport_nb, stations, time):
	for station_name, tranports in stations.items():
		if transport_nb in tranports:
			add_time_for_transport(transport_nb, tranports, time)

# Get the transport numbers between 2 stations stored in a list.
def transports_between_stations(stations, station_name1, station_name2):
	transports1 = list(stations[station_name1].keys())
	transports2 = list(stations[station_name2].keys())
	return list(set(transports1) & set(transports2))

# transport_count: {nb1: count1, nb2: count2...}
# Check if the given transport_count list fulfills the given trafic_load.
def transport_count_is_valid(
	stations, traffic_load, transport_count, transport_capacity
):
	for station_connection, load in traffic_load.items():
		st1, st2 = station_connection.split(" -> ")
		transport_nbs = transports_between_stations(stations, st1, st2)

		for nb in transport_nbs:
			load -= transport_count[nb] * transport_capacity

		if load > 0:
			return False

	return True

def get_delta_time(initial_stations, updated_stations):
	transport_nbs = get_all_transport_numbers(updated_stations)
	tr_deltas = dict((nb, -1) for nb in transport_nbs)

	for st_name, transports in updated_stations.items():
		for nb, times in transports.items():
			tr_deltas[nb] = abs(times[0] - initial_stations[st_name][nb][0])
	return tr_deltas