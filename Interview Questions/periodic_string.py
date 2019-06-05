'''
Periodic String
For example:
"abcabc" - periodic with period 3 → ‘abc’ repeats itself
"abababababab" - periodic with period 2 → ‘ab’ repeats itself
"abababx" - not periodic
“abc” - not periodic 

Q) Given a string s and a period p, checks if the string s has a period p

''' 
    
#time complexity: O(n/p) | Space Complexity: None (n: length of string, p: value of period)

def check_period(s, p):
	if s:
		for index in range(p, len(s), p):		
			if s[index : p+index] != s[0 : p]:
				return False			
	else:
		return False
