a = [7,8,9,2,3,1,4,10,5,6]

################################################

b = a
b.sort()
print(b)
print('\n')

################################################

c=a
c.sort(reverse=True)
print(c)
print('\n')

################################################

for x in a:
	if x%2 == 0:
		print(x,end =" ")
print('\n')

################################################

for x in a:
	if x%2 !=0 :
		print(x,end = " ")
print('\n')

################################################

for x in a:
	if x%3 == 0:
		print(x,end= " ")