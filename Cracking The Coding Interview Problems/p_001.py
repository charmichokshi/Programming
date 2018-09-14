# Implement an algorithm to determine if a string has all unique character
# Time Complexity: O(n)
# Space Complexity: O(1)

###################### with using extra data structure ######################
def isUnique(s):
	a = [0] * 256
	for i in range(len(s)):
		if(a[ord(s[i])] != 0):
			return False
		a[ord(s[i])] += 1
	return True

s = "ab$+AA"
if isUnique(s):
	print("The String {} has all unique characters".format(s))
else:
	print("The String {} has duplicate characters".format(s))
#############################################################################


# Time Complexity: O(n * log(n))
# Space Complexity: None
###################### without using extra data structure ######################
def isUnique(s):
	s = sorted(s)
	for i in range(len(s)-1):
		if(s[i] == s[i+1]):
			return False
	return True

s = "ab$+A A"
if isUnique(s):
	print("The String {} has all unique characters".format(s))
else:
	print("The String {} has duplicate characters".format(s))
#############################################################################
