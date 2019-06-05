'''
Problem
Banny has just bought a new programmable robot. Eager to test his coding skills, he has placed the robot in a grid of squares with R rows (numbered 1 to R from north to south) and C columns (numbered 1 to C from west to east). The square in row r and column c is denoted (r, c).
Initially the robot starts in the square (SR, SC). Banny will give the robot N instructions. Each instruction is one of N, S, E or W, instructing the robot to move one square north, south, east or west respectively.
If the robot moves into a square that it has been in before, the robot will continue moving in the same direction until it reaches a square that it has not been in before. Banny will never give the robot an instruction that will cause it to move out of the grid.

Can you help Banny determine which square the robot will finish in, after following the N instructions?

Input  
 
3
5 3 6 2 3
EEWNS
4 3 3 1 1
SESE
11 5 8 3 4
NEESSWWNESE

Output

Case #1: 3 2
Case #2: 3 3
Case #3: 3 7
'''
  

test = input() 

for t in range(int(test)):
	inp = input() 
	x, c, r, curr_r, curr_c = (inp.split(" "))
	x, c, r, curr_r, curr_c = int(x), int(c), int(r), int(curr_r), int(curr_c)
	s = input()

	curr_c -= 1
	curr_r -= 1
	d = set()
	d.add((curr_r, curr_c))

	for i in s:
		if i == "E":
			curr_c += 1
		elif i == "W":
			curr_c -= 1
		elif i == "N":
			curr_r -= 1
		elif i == "S":
			curr_r += 1

		if (curr_r, curr_c) not in d:
			d.add((curr_r, curr_c))

		else:
			while((curr_r, curr_c) in d):

				if i == "E":
					curr_c += 1
				elif i == "W":
					curr_c -= 1
				elif i == "N":
					curr_r -= 1
				elif i == "S":
					curr_r += 1

			if (curr_r, curr_c) not in d:
				d.add((curr_r, curr_c))
	
	print("Case #%d: %d %d" %(int(t)+1, curr_r+1, curr_c+1))
