trivial = {"for", "has", "have", "she", "that", "the", "this", "will", "with"}

vowel = {"a","e","i","o","u"}

def dontChange(word):
	if word in trivial or word[0] in vowel or len(word) <= 2:
		return True
	else:
		return False

def getPrefix(word):
	prefix = ""
	rest = ""

	if word[:2] == "qu":
		return ("qu",word[2:])

	while len(word) > 0 and not word[0] in vowel:
		prefix += word[0]
		word = word[1:]

	rest = word
	return (prefix, rest)

def spoonerism(l):
	# takes a list of words, generate words after spoonerism
	prefixes = []
	rests = []
	spoonerism = []

	for word in l:
		if not dontChange(word):
			p,r = getPrefix(word)
			prefixes.append(p)
			rests.append(r)

	n = len(prefixes)
	for i in range(n):
		spoonerism.append(prefixes[i]+rests[(i+1)%n])
	
	if len(spoonerism) >= 1:
		s = [spoonerism[-1]] + spoonerism[0:-1]
	
	words = []
	for word in l:
		if dontChange(word):
			words.append(word)
		else:
			words.append(s.pop(0))

	return words

def main():
	with open("input.txt") as f:
		N = int(f.readline().strip())

		for i in range(N):
			l = f.readline().strip().split(" ")
			words = " ".join(spoonerism(l))
			print words

main()
