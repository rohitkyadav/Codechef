# Given 2 strings, decide one is permutation of other.

def checkPermutation(str1, str2):
	if len(str1) != len(str2):
		return False
	else:
		return " ".join(sorted(str1)) == " ".join(sorted(str2))

print(checkPermutation("abc", "bcc"))