def additionner(a,b):
	return (a + b)

def soustraction(a, b):
	return (a - b)

def division(a, b):
	if b == 0:
		raise ZeroDivisionError("Imposible de diviser par 0")
	return (a / b)

def multiplication(a, b):
	return (a * b)