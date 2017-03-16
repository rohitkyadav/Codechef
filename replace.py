# Method to replace all spaces in a string with a %20

def urlifyString (str):
	res = " "
	start = False
	for char in reversed(str):
		if char != " ":
			start = True
		if (char == " " and start == True):
			res += "02%"
		else:
			res += char
	return res[::-1]
print(urlifyString("Mr. John Smith"))