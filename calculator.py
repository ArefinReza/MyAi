import myAI
import subprocess

def open_calculator():
    try:
        subprocess.Popen("calc.exe")
        print("Calculator opened successfully.")
    except Exception as e:
        print(f"Error: {e}")
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero"

def calculator():
    print("Simple Calculator")
    print("Open Calculator app ! ")
    print("Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Enter operation number (1/2/3/4): ")
    
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            result = add(num1, num2)
            print(f"{num1} + {num2} = {result}")
            myAI.speak(result)
        elif choice == '2':
            result = subtract(num1, num2)
            print(f"{num1} - {num2} = {result}")
            myAI.speak(result)
        elif choice == '3':
            result = multiply(num1, num2)
            print(f"{num1} * {num2} = {result}")
            myAI.speak(result)
        elif choice == '4':
            result = divide(num1, num2)
            print(f"{num1} / {num2} = {result}")
            myAI.speak(result)
    else:
        myAI.speak("Invalid input. Please choose a valid operation.")
        

if __name__ == "__main__":
    open_calculator()
    calculator()
