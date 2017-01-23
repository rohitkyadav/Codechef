tests = int(input("enter the no. of test cases: "))

while tests>0:
	color_string = input("enter the color sequence using a and b only : ")
	A = color_string.count('a')
	B = color_string.count('b')
	if A>B:
		for x in ['b']:             			# if x is equal to b
			color_string = color_string.replace('b', 'a')
			count = B
			print(count, color_string)
	else:
		for x in ['a']:
			color_string = color_string.replace('a', 'b')
			count = A
			print(count, color_string)
	tests -= 1