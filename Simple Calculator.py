
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y
def power(x,y):
    return x**y
def floor_divide(x,y):
    if y == 0:
        return "Error! Division by zero."
    return x//y
def modulo(x,y):
     if y == 0:
        return "Error! Division by zero."
     return x % y
def inverse(x,y):
    return x**(-y)
def root(x,y):
    return x**(1/y)
def Comparison(x,y):
    if x>y:
        return f"{x} is greater than {y}"
    elif y>x:
        return f"{y} is greater than {x}"
    else:
        return "Both numbers are equal"
def average(x,y):
    return (x + y) / 2

def root(x,y):
    return x**(1/y)


print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exponent")
print("6. Floor Division ")
print("7. Modulo")
print("8. Comparison")
print("9. Average")
print("10. Root")



while True:
    choice = input("Enter choice (1/2/3/4/5/6/7/8/9/10: ")
    if choice in ['1', '2', '3', '4','5','6','7','8','9','10']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            print (f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print (f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print (f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print (f"{num1} / {num2} = {divide(num1, num2)}")
        elif choice == '5':
            print (f"{num1} ** {num2} = {pow(num1, num2)}")
        elif choice == '6':
            print (f"{num1} // {num2} = {floor_divide(num1,num2)}")
        elif choice == '7':
            print (f"{num1} % {num2} = {modulo(num1,num2)}")
        elif choice == '8':
            print (f"Comparing {num1} and {num2}= {Comparison(num1,num2)}")
        elif choice == '9':
            print (f"The average of {num1} and {num2} is = {average(num1,num2)}")
        elif choice == '10':
            print (f"{num2} root of {num1} is = {root(num1,num2)}")
        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break
    else:
        print("Invalid Input")
