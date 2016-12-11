import datetime
T = int(input("enter the number of tests: "))
while T>0:
	Y = int(input("enter the year: "))
	S = "January" + " " + str(1) + "," + " " + str(Y)
	day = datetime.datetime.strptime(S, '%B %d, %Y').strftime('%A')
	print(day.lower())
	T -= 1