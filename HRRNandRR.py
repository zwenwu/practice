import copy
presentTime = 0
arrivalTimes = []
serviceTimes = []
processName = []
averageWT = 0.0
averageWWT = 0.0
def x(number):
	list = []
	for i in range(number):list.append([])
	return list
def y(at,st,pt):
	wt = pt - at
	R = wt/st + 1
	return R
def HRRN(number):
	Response = x(number)
	at = copy.deepcopy(arrivalTimes)
	st = copy.deepcopy(serviceTimes)
	n = number
	presentTime = min(at)
	while number>0:
		if presentTime < min(at):presentTime = min(at)
		for i in range(n):
			r = y(at[i],st[i],presentTime)
			Response[i] = r 
		index = Response.index(max(Response))
		print(presentTime," time,",processName[index]," start running")
		finishTime[index] = st[index] + presentTime
		presentTime = finishTime[index]
		print(presentTime," time,",processName[index]," stop running")
		wholeTime[index] = finishTime[index] - arrivalTimes[index]
		weightWholeTime[index] = round(wholeTime[index] / serviceTimes[index],2)
		at[index] = 10000
		number -= 1
def RR(number):
	q = int(input("Please input q: "))
	at = copy.deepcopy(arrivalTimes)
	st = copy.deepcopy(serviceTimes)
	presentTime = min(at)
	while number>0:
		index = at.index(min(at))
		print(presentTime," time,",processName[index]," start running")
		if q < st[index]:
			st[index] = st[index] - q
			at[index] = q + 0.5 + at[index]
			presentTime += q
			print(presentTime," time,",processName[index]," sleep")
		else: 
			finishTime[index] = st[index] + presentTime
			wholeTime[index] = finishTime[index] - arrivalTimes[index]
			weightWholeTime[index] = round(wholeTime[index] / serviceTimes[index],2)
			presentTime += st[index]
			print(presentTime," time,",processName[index]," stop running")
			at[index] = 10000
			number -= 1
while True:
	processName.clear()
	arrivalTimes.clear()
	serviceTimes.clear()
	number = int(input("Please input process number: "))
	finishTime = x(number)
	wholeTime = x(number)
	weightWholeTime = x(number)
	for i in range(number):
		processName.append(input("Please input process's name: "))
		arrivalTimes.append(int(input("Please input process's arrival time: ")))
		serviceTimes.append(int(input("Please input process's service time: ")))
	option = int(input("Please input your choice,1-HRRN,2-RR: "))
	if option == 1:
		HRRN(number)
		print("process: ",processName)
		print("arrival time: ",arrivalTimes)
		print("service time: ",serviceTimes)
		print("finish time: ",finishTime)
		print("whole time: ",wholeTime)
		print("weight whole time: ",weightWholeTime)
		for i in range(number):
			averageWT += wholeTime[i]
			averageWWT += weightWholeTime[i]
		print("average wholeTime is: ",averageWT/number)
		print("average weightWholeTime is: ",round(averageWWT/number,2))
	elif option == 2:
		RR(number)
		print("process: ",processName)
		print("arrival time: ",arrivalTimes)
		print("service time: ",serviceTimes)
		print("finish time: ",finishTime)
		print("whole time: ",wholeTime)
		print("weight whole time: ",weightWholeTime)
		for i in range(number):
			averageWT += wholeTime[i]
			averageWWT += weightWholeTime[i]
		print("average wholeTime is: ",averageWT/number)
		print("average weightWholeTime is: ",round(averageWWT/number,2))
	else:
		print("This is error number.Please input again!")


