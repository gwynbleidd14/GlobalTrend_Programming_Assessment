'''
5. Write a Python function to compute the nth Fibonacci number using recursion.
'''

def fib(n):
    if n < 1:
        return "Invalid input!!"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
    

n = int(input("Enter a n value: "))
print(fib(n))