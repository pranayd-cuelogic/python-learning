def Fibonacci(n):
	result = []
	a , b = 0 , 1
	if(n <= 1):
		result.append(1)
		return result
	while(a < n):
		result.append(a)
		a , b = b , a + b
	return result

fib = Fibonacci(10)

print fib
