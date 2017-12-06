import os
import re

class Transport:
	def __init__(self, nb):
		self.nb = nb
		self.timetable = []

	# StationName is recieved with the '.txt' extension, so it is removed.
	# The time is transformed in a single number representing minutes.
	def appendStationTimes(self, stationName, timeArivalsStr):
		stationName = re.search(r"(.*)\.txt", stationName).group(1)

		for timeStr in re.findall(r'\d\d:\d\d', timeArivalsStr):
			hh, mm = timeStr.split(":")
			self.timetable.append([int(hh) * 60 + int(mm), stationName])

	def getAllStations(self):
		return list(set([stationName for time, stationName in self.timetable]))

	# Order the timetable.
	def order(self):
		self.timetable.sort(key=lambda x: x[0])

	def __str__(self):
		return "{" + self.nb + ": " + str(self.timetable) + "}"

def readTransports(stationsDir):
	transports = []

	for stationFileName in os.listdir(stationsDir):
		file = open(stationsDir + stationFileName, "r")

		for line in file:
			# Extract the transport number from a given line.
			nb = re.compile("[0-9]+").search(line).group()

			# Create a new transport if there isn't one with this nb.
			targetTransport = None
			for transport in transports:
				if transport.nb == nb:
					targetTransport = transport

			if targetTransport == None:
				targetTransport = Transport(nb)
				transports.append(targetTransport)

			targetTransport.appendStationTimes(stationFileName, line)

		file.close()
	return transports

transports = readTransports("./aux/stations/")
for transport in transports:
	transport.order()
	print(transport)