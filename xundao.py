
trackIdOrder = []
trackOrder = []
lenOrder = []

def FCFS(trackStart,trackNum):
	lastTrack = trackStart
	total = 0
	for i in range(trackNum):
		trackOrder[i] = trackIdOrder[i]
		length = abs(lastTrack - trackOrder[i])
		lenOrder[i] = length
		total += length
		lastTrack = trackOrder[i]
	aL = total / trackNum
	print("track order",trackOrder)
	print("length order",lenOrder)
	print("Average track length",aL)

def SSTF(trackStart,trackNum):
	lastTrack = trackStart
	total = 0
	n = trackNum
	index = 0
	TIO = trackIdOrder.copy()
	distance = [0 for i in range(trackNum)]
	while n>0:
		for i in range(trackNum):
			distance[i] = abs(TIO[i] - lastTrack)
		minLen = min(distance)
		lenOrder[index] = minLen
		total += minLen
		trackOrder[index] = TIO[distance.index(minLen)]
		TIO[distance.index(minLen)] = 1000
		lastTrack = trackOrder[index]
		index += 1
		n -= 1 
	aL = total / trackNum
	print("track order",trackOrder)
	print("length order",lenOrder)
	print("Average track length",aL)

def SCAN(trackStart,trackNum,direction):
	lastTrack = trackStart
	total = 0
	index = 0
	TIO = sorted(trackIdOrder)
	for i in range(trackNum):
		if TIO[i] >= trackStart:
			index = i
			break
	TIO_min = TIO[:index]
	TIO_max = TIO[index:]
	TIO_min.reverse()
	if direction == 0:
		for i in range(len(TIO_max)):
			trackOrder[i] = TIO_max[i]
			length = abs(trackOrder[i] - lastTrack)
			lenOrder[i] = length
			total += length
			lastTrack = trackOrder[i]
		for i in range(len(TIO_min)):
			trackOrder[i+len(TIO_max)] = TIO_min[i]
			length = abs(trackOrder[i+len(TIO_max)] - lastTrack)
			lenOrder[i+len(TIO_max)] = length
			total += length
			lastTrack = trackOrder[i+len(TIO_max)]
	else:
		for i in range(len(TIO_min)):
			trackOrder[i] = TIO_min[i]
			length = abs(trackOrder[i] - lastTrack)
			lenOrder[i] = length
			total += length
			lastTrack = trackOrder[i]
		for i in range(len(TIO_max)):
			trackOrder[i+len(TIO_min)] = TIO_max[i]
			length = abs(trackOrder[i+len(TIO_min)] - lastTrack)
			lenOrder[i+len(TIO_min)] = length
			total += length
			lastTrack = trackOrder[i+len(TIO_min)]
	aL = total / trackNum
	print("track order",trackOrder)
	print("length order",lenOrder)
	print("Average track length",aL)

def CSCAN(trackStart,trackNum,direction):
	lastTrack = trackStart
	total = 0
	index = 0
	TIO = sorted(trackIdOrder)
	for i in range(trackNum):
		if TIO[i] >= trackStart:
			index = i
			break
	TIO_min = TIO[:index]
	TIO_max = TIO[index:]
	if direction == 0:
		for i in range(len(TIO_max)):
			trackOrder[i] = TIO_max[i]
			length = abs(trackOrder[i] - lastTrack)
			lenOrder[i] = length
			total += length
			lastTrack = trackOrder[i]
		for i in range(len(TIO_min)):
			trackOrder[i+len(TIO_max)] = TIO_min[i]
			length = abs(trackOrder[i+len(TIO_max)] - lastTrack)
			lenOrder[i+len(TIO_max)] = length
			total += length
			lastTrack = trackOrder[i+len(TIO_max)]
	else:
		TIO_min.reverse()
		TIO_max.reverse()
		for i in range(len(TIO_min)):
			trackOrder[i] = TIO_min[i]
			length = abs(trackOrder[i] - lastTrack)
			lenOrder[i] = length
			total += length
			lastTrack = trackOrder[i]
		for i in range(len(TIO_max)):
			trackOrder[i+len(TIO_min)] = TIO_max[i]
			length = abs(trackOrder[i+len(TIO_min)] - lastTrack)
			lenOrder[i+len(TIO_min)] = length
			total += length
			lastTrack = trackOrder[i+len(TIO_min)]
	aL = total / trackNum
	print("track order",trackOrder)
	print("length order",lenOrder)
	print("Average track length",aL)

while True:
	trackOrder.clear()
	trackIdOrder.clear()
	lenOrder.clear()

	trackNum = int(input("Please input track number: "))
	trackStart = int(input("Please input start track id: "))
	for i in range(trackNum):
		trackIdOrder.append(int(input("Please input track id: ")))
	lenOrder = [0 for i in range(trackNum)]
	trackOrder = [0 for i in range(trackNum)]

	while True:
		option = int(input("Please select 1-FCFS 2-SSTF 3-SCAN 4-CSCAN,5-input data again: "))
		if option == 1:
			FCFS(trackStart,trackNum)
		elif option == 2:
			SSTF(trackStart,trackNum)
		elif option == 3:
			direction = int(input("Please select direction 0-increase or 1-decrease: "))
			SCAN(trackStart,trackNum,direction)
		elif option == 4:
			direction = int(input("Please select direction 0-increase or 1-decrease: "))
			CSCAN(trackStart,trackNum,direction)
		else:
			break
	