specialChar = "!\"$%&\'()*,-.:?@"

def ternary(n):
	q = n/3
	r = n%3

	if q == 0:
		return ""
	else:
		return ternary(int(q))+str(int(r))

def getSequence():
	seq = []
	for i in range(82):
		s = "0"*(4-len(ternary(i))) + ternary(i)
		if s == "0000" or s == "1111":
			pass
		else:
			seq.append(s)

	return seq

decrypted = [chr(x+65) for x in range(26)]+[chr(x+97) for x in range(26)]
decrypted += [str(x) for x in range(10)]+[" "]+list(specialChar)+["LOCKOUT"]

seq = getSequence()

dictionary = dict(zip(seq,decrypted))

def ternaryFromClacks(clack):
	ans = ""
	convert = {"X.": "0", ".X": "1", "..": "2"}

	for i in range(0,8,2):
		ans += convert[clack[i:i+2]]

	return ans[::-1]


def main():
	message = ""

	with open("input4.txt") as f:
		N = int(f.readline().strip())
		lockedOut = False

		for i in range(N):
			clack = f.readline().strip()
			ternaryRep = ternaryFromClacks(clack)
			
			if not ternaryRep in seq:
				message += "#"
			elif ternaryRep == "LOCKOUT":
				lockedOut = True
				print(message)
				print("LOCKOUT")
				break
			else:
				message += dictionary[ternaryRep]

		if not lockedOut:
			print(message)

main()
