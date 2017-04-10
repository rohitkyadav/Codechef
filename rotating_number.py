# Rotation of a number

num = int(input())

def rotate(num, x):
	#numbers can't be converted to list directly
	
	#lst = map(int, str(num))    note, This will return a map object in python 3.(no pop fxn in map object)
	#[int(x) for x in str(num)]      another way to convert a int into list

	lst = list(str(num))
	
	if x >= 0:
		for i in range(x):
			lastNum = lst.pop(-1)
			lst.insert(0, lastNum)

	else:
		for i in range(abs(x)):
			firstNum = lst.pop(0)
			lst.append(firstNum)

	return ''.join(lst)

print(rotate(num, 1))



# rotate(lst, x):
#     return [lst[-x:] + lst[:-x]