'''
Fibonacci Sequence: Generate the first ( n ) Fibonacci numbers using iterative and recursive methods.
'''

def fibonacci_iterative(n: int) -> None:
    '''Iterative method.'''
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib_seq = [0, 1]
    while len(fib_seq) < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq
# print(fibonacci_iterative(10))

def fibonacci_recursive(n: int) -> None:
    '''Recursive method.'''
    def fib(n: int) -> int:
        if n <= 1:
            return n
        else:
            return fib(n - 1) + fib(n - 2)
    return [fib(i) for i in range(n)]
# print(fibonacci_recursive(10))

