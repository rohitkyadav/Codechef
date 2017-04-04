"""
Colleen is turning  years old! She has  candles of various heights on her cake, and candle  has 
height hi . Because the taller candles tower over the shorter ones, Colleen can only blow out the 
tallest candles.

Given the  for each individual candle, find and print the number of candles she can successfully 
blow out.

Input Format

The first line contains a single integer, , denoting the number of candles on the cake. 
The second line contains  space-separated integers, where each integer  describes the height of 
candle .


Output Format

Print the number of candles Colleen blows out on a new line.

Sample Input
4
3 2 1 3

Sample Output
2

Explanation

We have one candle of height , one candle of height , and two candles of height . Colleen only 
blows out the tallest candles, meaning the candles where . Because there are  such candles, we 
print  on a new line.
"""

#!/bin/python3

import sys
n = int(input().strip())
height = [int(height_temp) for height_temp in input().strip().split(' ')]

print(height.count(max(height)))