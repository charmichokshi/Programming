# Given two strings, write a method to decide if one is a permutation of the other.

# Time Complexity: O(n)
# Space Complexity: None
#############################################################################
def isPermutations(s, s1):
	if(len(s) != len(s1)):
		return False
	for i in range(len(s)):
		if(s[i] != s1[len(s)-i-1]):
			return False
	return True

s = "abcd"
s1 = "dcba"
if isPermutations(s, s1):
	print("The Strings are permutations of each other")
else:
	print("The Strings are NOT a permutations of each other")
#############################################################################


# Time Complexity: O(n * log(n))
# Space Complexity: None
#############################################################################
def isPermutations(s, s1):
	if(len(s) != len(s1)):
		return False
	s = sorted(s)
	s1 = sorted(s1)
	for i in range(len(s)):
		if(s[i] != s1[i]):
			return False
	return True

s = "abad" 
s1 = "dcba"
if isPermutations(s, s1):
	print("The Strings are permutations of each other")
else:
	print("The Strings are NOT a permutations of each other")
#############################################################################
