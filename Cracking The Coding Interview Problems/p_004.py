# Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards. 
# A permutation is a rerangement of letters. The palindrome does not need to be limited to just dictionary words.

# -*- coding: utf8 -*-
NO_OF_CHARS = 256
count = [0] * (NO_OF_CHARS)

def is_palindrome(s):
	for i in range( 0, len(s)):
		count[ord(s[i])] += 1
	# all odd numbers will have 1 at the end, all even numbers will hace 0 at the end
 	odd = 0 
	for i in range(0, NO_OF_CHARS):
	    if (count[i] & 1) :
	        odd = odd + 1
	    if (odd > 1) :
	        return False
	return True

def get_permutation(l):
	if len(l) == 0:
		return []
	elif len(l) == 1:
		return [l]
	else:
		prm = []
		for i in range(len(l)):
			x = l[i]
			xs = l[:i] + l[i+1:]
			for p in get_permutation(xs):
				prm.append([x]+p)
		return prm

def palindrome_permutation(s):
	if (is_palindrome(s)):
		l = len(s)
		half = ""
		for i in range(0, NO_OF_CHARS):
			if(count[i]%2 == 1):
				oddChar = chr(i)
			if(count[i] > 0):
				half += chr(i)*(count[i]/2)
		prm = get_permutation(list(half))
		i = 0
		for p in prm:            # do the following for each permutation
			ans = ""
			p = "".join(p)
			ans += p           # join first half of the string
			if(l%2 == 1):
				ans += oddChar	# join the odd character if present
			ans += p[::-1]      # join seconf half(reverse) of the string
			print(ans)

	else:
		print("permutation of a palindrome is not possible for the input string")

s = "TactCoa"
palindrome_permutation(s.lower())
