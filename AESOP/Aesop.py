def solve(sequence):
	# first find out if there's a cycle
	tortoise = 1
	hare = 2
	has_cycle = False

	while hare < len(sequence):
		if sequence[tortoise] == sequence[hare]:
			# cycle found!
			has_cycle = True
			break
		tortoise += 1
		hare += 2
	
	i = tortoise
	s_preview = map(str, sequence[:5])
	
	if has_cycle:
		tortoise = 0
		while hare < len(sequence):
			if sequence[tortoise] == sequence[hare]:
				m = tortoise
				break
			tortoise += 1
			hare += 1
		hare = tortoise+1
		while sequence[hare] != sequence[tortoise]:
			hare += 1
		c = hare - tortoise
		k = i/c
		print("m = %d, c = %d, k = %d, %s" % (m, c, k, s_preview))
	else:
		print("No solution for %s" % s_preview)


def test():
	data = [1,2,4,11,33,6,82,55,15,9,27,0,44,8,3,7,21,40,6,82,
		    55,15,9,27,0,44,8,3,7,21,40,6,82,55,15,9,]
	d = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
	
	solve(data)

def main():
	f = open("task2.dat")
	N = int(f.readline().strip())

	for i in xrange(N):
		sequence = map(int, f.readline().strip().split())
		solve(sequence)

main()
