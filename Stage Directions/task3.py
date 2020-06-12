def generateGrayCode(n):
	
	if (n <= 0):
		return

	arr = list()

	arr.append("0")
	arr.append("1")

	i = 2
	j = 0

	while (True):
		if i >= 1 << n:
			break
		
		for j in range(i-1, -1, -1):
			arr.append(arr[j])

		for j in range(i):
			arr[j] = "0" + arr[j]

		for j in range(i, 2*i):
			arr[j] = "1" + arr[j]

		i = i << 1

	for i in range(len(arr)):
		arr[i] = [int(x) for x in arr[i]][::-1]
	
	arr.append([0 for i in range(n)])
	return(arr)

def transition(sOne, sTwo):
	# gives stage direction from state 1 to state2
	for i in range(len(sOne)):
		if sTwo[i] - sOne[i] == 1:
			return "Leave " + str(i+1)
		elif sTwo[i] - sOne[i] == -1:
			return "Enter " + str(i+1)


def format(n):
	grayCode = generateGrayCode(n)
	title = " ".join([str(i+1) for i in range(n)])
	state = " ".join(["-" for i in range(n)])
	
	print("%-11s %-11s %-11s" %("Direction", "On stage", title))
	print("%-11s %-11s %-11s" %(" ", " ", state))
	
	for i in range(1,len(grayCode)):
		direction = transition(grayCode[i], grayCode[i-1])
		onStage = [str(x+1) for x in range(len(grayCode[i])) if grayCode[i][x] == 1]
		note = ["X" if grayCode[i][x] == 1 else "-" for x in range(len(grayCode[i]))]

		onStage = " ".join(onStage)
		note = " ".join(note)

		print("%-11s %-11s %-11s" % (direction, onStage, note))
	
format(3)
print
format(5)
