def typeA(n):
	bs = format(n, 'b')
	newString = ""
	for digit in bs:
		if digit == '0':
			newString += '1'
		elif digit == '1':
			newString += '0'

	return newString[::-1] == bs

def typeB(n):
	ans = 0
	for digit in str(n):
		ans += int(digit)
		ans += int(digit)**3
	
	return ans == n

def typeC(n):
	square = str(n**2)
	cube = str(n**3)
	ans = 0

	for digit in square:
		ans += int(digit)**3
	for digit in cube:
		ans += int(digit)

	return ans == n

typeAs = []
typeBs = []
typeCs = []

for i in range(1,1001):
	if typeA(i):
		typeAs.append(str(i))
	if typeB(i):
		typeBs.append(str(i))
	if typeC(i):
		typeCs.append(str(i))

print("TYPE A: " + " ".join(typeAs))
print("TYPE B: " + " ".join(typeBs))
print("TYPE C: " + " ".join(typeCs))

