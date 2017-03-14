# Implement a algo to determine if a string has all unique characters
# Assuming ASCII 128 max unique characters

testString = "a b c"

def isUniqueChars(str):
	if len(str) > 128:
		return False
	arr = [False]*128

	for char in str:
		if arr[ord(char)] is False:
			arr[ord(char)] = True
		else:
			return False
	return True

print (isUniqueChars(testString))



"""
testString = input("Enter the string: ")

def isUniqueChars(str):
	if len(str) > 128:
		return False
	arr = [False]*128

	for char in str:
		if arr[ord(char)] is False:
			arr[ord(char)] = True
		else:
			return False
	return True

print (isUniqueChars(testString))

"""