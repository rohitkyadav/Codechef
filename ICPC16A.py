"""
Robot Bunny is lost. It wants to reach its home as soon as possible. Currently it is standing at 
coordinates (x1, y1) in 2-D plane. Its home is at coordinates (x2, y2). Bunny is extremely worried. 
Please help it by giving a command by telling the direction in which it should to go so as to reach its 
home. If you give it a direction, it will keep moving in that direction till it reaches its home. 
There are four possible directions you can give as command - "left", "right", "up", "down". It might 
be possible that you can't instruct the robot in such a way that it reaches its home. In that case, 
output "sad".

Input
First line of the input contains an integer T denoting the number of test cases. T test cases follow.

First line of each test case contains four space separated integers x1, y1, x2, y2.

Output
For each test case, output a single line containing "left" or "right" or "up" or "down" or "sad" 
(without quotes).

Example

Input
3
0 0 1 0
0 0 0 1
0 0 1 1

Output:
right
up
sad
"""

#program
T = int(input())

while T:
	x1, y1, x2, y2 = [int(x) for x in input().split()]

	if x1==x2 and y1<y2:
		print("up")

	elif x1==x2 and y1>y2:
		print("down")

	elif y1==y2 and x1<x2:
		print("right")

	elif y1==y2 and x1>x2:
		print("left")

	else:
		print("sad")

	T -= 1