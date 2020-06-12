vowel = {"a","e","i","o","u","y"}

def unscramble(n):
	if n == '':
		return "\n"

	vowels = []
	ans = ""
	for letter in n:
		if letter.lower() in vowel:
			vowels.append(letter.lower())


	vowels = [vowels[-1]]+vowels[:-1]
	
	for letter in n:
		if letter.lower() in vowel:
			s = vowels.pop(0)
		else:
			s = letter.lower()

		if letter.isupper():
			ans += s.upper()
		else:
			ans += s

	return ans

def main():
	string = ""

	with open("input2.txt") as f:
		lines = f.readlines()
		for l in lines:
			l = l.strip().split(" ")
			for word in l:
				string += unscramble(word) + " "

	with open("out.txt","w") as o:
		o.write(string)

main()
