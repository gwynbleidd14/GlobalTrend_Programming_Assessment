'''
6. Write a Python function that divides two numbers and handles the case where the divisor
is zero by returning a custom error message.
'''

def division(num1, num2):
    try:
        quotient = num1 / num2
        remainder = num1 % num2
        print("Quotient is:", quotient)
        print("Remainder is:", remainder)
    except Exception as e:
        print("An error '", e, "' has occurred. Please use a non-zero divisor.")
        
        
dividend = int(input("Enter the dividend: "))
divisor = int(input("Enter the divisor: "))

division(dividend, divisor)