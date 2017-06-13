"""
Today is the final round of La Liga, the most popular professional football league in the world. Real 
Madrid is playing against Malaga and Barcelona is playing against Eibar. These two matches will decide 
who wins the league title. Real Madrid is already 3 points ahead of Barcelona in the league standings. 
In fact, Real Madrid will win the league title, except for one scenario: If Real Madrid loses against 
Malaga, and Barcelona wins against Eibar, then the La Liga title will go to Barcelona. In any other 
combination of results, Real Madrid will win the title.

You will be given multiple scenarios for these two games, where in each one you will be given the 
number of goals each team scored in their respective match. A team wins a match if it scores more than 
the opponent. In case they score the same number of goals, it's a draw. Otherwise, the team loses the 
game. You are asked to tell the winner of the La Liga title in each scenario.


Input
The first line contains a single number T, the number of scenarios. Each scenario is described by four 
lines. Each line starts with a team name followed by the number of goals this team scored in its 
corresponding match. (Barcelona plays Eibar and Real Madrid plays Malaga). The names are given in any 
arbitrary order within a scenario.


Output
For each scenario, output a single line showing the title winner in case this scenario happens. It 
should be either "RealMadrid" or "Barcelona".


Constraints
1 ≤ T ≤ 500
0 ≤ number of goals scored by a team in a match ≤ 20

Example

Input:
2
Barcelona 2
Malaga 1
RealMadrid 1
Eibar 0

Malaga 3
RealMadrid 2
Barcelona 8
Eibar 6

Output:
RealMadrid
Barcelona

"""

# T = int(input())
# while T:
# 	rm=0
# 	bc=0
# 	ml=0
# 	ei=0
# 	for i in range(4):
# 	    inp=input().split()
# 		if(inp[0]=="RealMadrid"):
# 			rm=int(inp[1])
# 		elif(inp[0]=="Malaga"):
# 			ml=int(inp[1])
# 		elif(inp[0]=="Barcelona"):
# 			bc=int(inp[1])
# 		else:
# 			ei=int(inp[1])
# 	if(rm<ml and bc>ei):
# 		print("Barcelona")
# 	else:
# 		print("RealMadrid")
#	T -= 1


T = int(input())

while T:
	x1 = input().split()
	x2 = input().split()
	x3 = input().split()
	x4 = input().split()

	if "RealMadrid" in  x1:
		real = x1
	elif "RealMadrid" in  x2:
		real = x2
	elif "RealMadrid" in  x3:
		real = x3
	else:
		real = x4

	if "Malaga" in  x1:
		mal = x1
	elif "Malaga" in  x2:
		mal = x2
	elif "Malaga" in  x3:
		mal = x3
	else:
		mal = x4

	if "Barcelona" in  x1:
		bar = x1
	elif "Barcelona" in  x2:
		bar = x2
	elif "Barcelona" in  x3:
		bar = x3
	else:
		bar = x4

	if "Eibar" in  x1:
		eib = x1
	elif "Eibar" in  x2:
		eib = x2
	elif "Eibar" in  x3:
		eib = x3
	else:
		eib = x4

	if int(real[1]) >= int(mal[1]) or int(bar[1]) <= int(eib[1]):
	 	print(real[0])
	else:
	 	print(bar[0])

	T -= 1