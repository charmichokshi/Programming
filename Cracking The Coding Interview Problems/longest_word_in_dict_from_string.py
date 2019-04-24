#Find longest word in dictionary that is a subsequence of a given string

def find_longest_word(s, d):
	ele = str()
	max_len = 0

	for word in d:
		yes, start = 0, 0 
		l = len(s)
		for char in word:
			for c in range(start, l):
				if s[c] == char:
					yes += 1
					start = s.index(s[c])+1
					break
		if yes == len(word):
			if len(word) >= max_len:
				max_len = len(word)
				ele = word
	return ele

longest_word = find_longest_word("abppplee", {"a", "able", "ale", "apple", "bale", "kangaroo"})
print(longest_word)
