import os
import re

# {station_name: {nb: [t1, t2 ...]}}
# Read from the given directory all stations.
def read_stations(stations_dir):
	stations = dict()

	for station_file_name in os.listdir(stations_dir):
		file = open(stations_dir + station_file_name, 'r')

		station_name = re.search(r"(.*)\.txt", station_file_name).group(1)
		stations[station_name] = dict()

		for line in file:
			nb = int(re.search("[0-9]+", line).group())

			stations[station_name][nb] = []
			for time_str in re.findall(r'\d\d:\d\d', line):
				hh, mm = time_str.split(":")
				stations[station_name][nb].append(int(hh) * 60 + int(mm))
		stations[station_name][nb].sort()
		file.close()

	return stations
