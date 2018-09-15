# URLify: Write a method to replace all spaces in a string with '%20'
# since python strings are immutable, I have converted the input string to list to perform all the conversations and then again 
# converted it to a string using str.join(list) method

# implementation is based on "in-place algorithm" assuming that we have extra space in input string
# Time Complexity: O(n)
# Space Complexity: O(1)

def replace_space(string, str_len):
	num_space = 0
	cnt = 0
	s = [None] * 100
	ss = list(string)
	for x in range(len(ss)):
		s[x] = ss[x]
	# count total number of spaces
	for i in range(len(s)):
		if(s[i] == " "):
			num_space += 1
	# remove extra number of spaces at the end of the string from num_spaces
	for i in range(len(s)-1,0,-1):
		if(s[i] == None):
			num_space = num_space
		elif(s[i] == " "):
			num_space -= 1
		else:
			break
	new_str_len = str_len + num_space * 2
	nsl = new_str_len
	new_str_len -= 1
	# Fill rest of the string from end
	for i in range(str_len-1,-1,-1):
		if(s[i] == " "):
			s[new_str_len] = "0"
			s[new_str_len-1] = "2"
			s[new_str_len-2] = "%"
			new_str_len = new_str_len -3
		else:
			s[new_str_len] = s[i]
			new_str_len = new_str_len -1
	# convert list to string
	s = ''.join([ str(x) for x in s if x != None ])   
	return s

s = raw_input("Enter String: ")
str_len = input("Enter length: ")
print("Entered String is: ", s)
replaced =  replace_space(s, str_len)
print("Replaced String is: ", replaced)
