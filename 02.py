def your_function(*args):
	sum = 0
	for i in args:
		if isinstance(i,bool)!=True and isinstance(i,int) or isinstance(i,float): 
			sum += i
	return sum

################################################

def sum(n):
	if n <=1 :
		return n
	return  n + sum(n-1)

def sumpara(n):
	if n<=1 and n%2==0 :
		return n
	if n%2 == 0:
		return n + sumpara(n-1)
	return sumpara(n-1)
	
def sumimpara(n):
	if n<=1 and n%2!=0:
		return n
	if n%2 !=0:
		return n + sumimpara(n-1)
	return sumimpara(n-1)

################################################

def citire():
	a = input("Introduceti valoarea:")
	try:
		valoare = int(a)
	except ValueError:
		return None
	return valoare


