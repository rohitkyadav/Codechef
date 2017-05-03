"""
Bears love candies and games involving eating them. Limak and Bob play the following game. Limak eats 1 
candy, then Bob eats 2 candies, then Limak eats 3 candies, then Bob eats 4 candies, and so on. Once 
someone can't eat what he is supposed to eat, he loses.

Limak can eat at most A candies in total (otherwise he would become sick), while Bob can eat at most B 
candies in total. Who will win the game? Print "Limak" or "Bob" accordingly.

Input
The first line of the input contains an integer T denoting the number of test cases. The description of 
T test cases follows.

The only line of each test case contains two integers A and B denoting the maximum possible number of 
candies Limak can eat and the maximum possible number of candies Bob can eat respectively.

Output
For each test case, output a single line containing one string — the name of the winner ("Limak" or 
"Bob" without the quotes).

Example

Input:
10
3 2
4 2
1 1
1 2
1 3
9 3
9 11
9 12
9 1000
8 11

Output:
Bob
Limak
Limak
Bob
Bob
Limak
Limak
Bob
Bob
Bob
"""

#program
T = int(input())

while T:
	A, B = [int(x) for x in input().split()]
	l = 1
	b = 2
	
	while(1):
		if(A<l):
			print ("Bob")
			break
		if(B<b):
			print ("Limak")
			break
		A -= l
		l += 2
		B -= b
		b += 2 
	T -= 1