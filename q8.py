'''
8. Write a Python function that takes two numbers and an operator (as a string) and
performs the corresponding arithmetic operation (addition, subtraction, multiplication, or
division).
'''

def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        try:
            return num1 / num2
        except Exception as e:
            return e
    else:
        return "Invalid operation!!"
    
    
a = int(input("Enter number1: "))
b = int(input("Enter number2: "))        
o = input("Enter arithmatic operator (+, *, -, /): ")

res = calculate(a, b, o)
print("Answer: ", res)