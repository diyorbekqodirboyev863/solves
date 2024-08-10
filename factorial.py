'''
Factorial Calculation: Compute the factorial of a number ( n ) iterative and recursive methods.
'''

def factorial_iterative(n: int) -> None:
	'''Iterative method.'''
	if n <= 0:
		raise ValueError('Factorial is not defined for negative numbers.')
	s: int = n - (n - 1)
	for i in range(1, n + 1):
		s *= i
	return s

# print(factorial_iterative(6))

def factorial_recursive(n: int) -> None:
	'''Recursive method.'''
	if n < 0:
		raise ValueError('Factorial is not defined for negative numbers.')
	if n == 0 or n == 1:
		return 1
	return n * factorial_recursive(n-1)
# print(factorial_recursive(6))