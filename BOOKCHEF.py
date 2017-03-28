"""
Chef Watson uses a social network called ChefBook, which has a new feed consisting of posts by his 
friends. Each post can be characterized by f - the identifier of the friend who created the post, 
p - the popularity of the post(which is pre-calculated by ChefBook platform using some machine 
learning algorithm) and s - the contents of the post which is a string of lower and uppercase 
English alphabets.

Also, Chef has some friends, which he has marked as special.

The algorithm used by ChefBook for determining the order of posts in news feed is as follows:

Posts of special friends should be shown first, irrespective of popularity. Among all such posts 
the popular ones should be shown earlier.
Among all other posts, popular posts should be shown earlier.
Given, a list of identifiers of Chef's special friends and a list of posts, you have to implement 
this algorithm for engineers of ChefBook and output the correct ordering of posts in the new feed.

Input
First line contains N, number of special friends of Chef and M, the number of posts. Next line 
contains N integers A1, A2, ..., AN denoting the identifiers of special friends of Chef. Each of 
the next M lines contains a pair of integers and a string denoting f, p and s, identifier of the 
friend who created the post, the popularity of the post and the contents of the post, respectively. 
It is guaranteed that no two posts have same popularity.

Output
Output correct ordering of posts in news feed in M lines. Output only the contents of a post.


Example

Input:
2 4
1 2
1 1 WhoDoesntLoveChefBook
2 2 WinterIsComing
3 10 TheseViolentDelightsHaveViolentEnds
4 3 ComeAtTheKingBestNotMiss

Output:
WinterIsComing
WhoDoesntLoveChefBook
TheseViolentDelightsHaveViolentEnds
ComeAtTheKingBestNotMiss
"""

#program
N, M = map(int, input().split())
identifier = input().split() #can't input as intergers bcoz needs to be compared in if statement

special = []
normal = []

for x in range(0, M):
	f, p, s = input().split()
	if f in identifier:
		special.append((int(p),s))
	else :
		normal.append((int(p),s))

special.sort(key=lambda x: x[0], reverse = True)
normal.sort(reverse = True)

for p,s in special:
	print(s)

for p,s in normal:
	print(s)