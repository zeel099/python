def add(a, s):
    return a + s


def subtract(a, s):
    return a - s

def multiply(a, s):
    return a * s

def divide(a, s):
    return a / s


print("Select choice.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
 
    choice = input("Enter your choice: ")


    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter a number1: "))
        num2 = float(input("Enter a number2: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

    
    else:
        print("Invalid Input")