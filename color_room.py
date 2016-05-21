T = int(input("Enter the number of test"))
for x in range(T):
	rooms = int(input("Enter the number of rooms"))
	S = input("Enter the string of the colors in the rooms")
	R = S.count('R')
	G = S.count('G')
	B = S.count('B')
	number = len(S) - max(R, G, B)
	print(number)
