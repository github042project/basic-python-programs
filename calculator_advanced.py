# calculator_advanced.py
def add(x, y): return x + y
def sub(x, y): return x - y
def mul(x, y): return x * y
def div(x, y): return x / y if y != 0 else "Undefined"

while True:
    print("\nOptions:\n1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Exit")
    choice = input("Enter choice: ")

    if choice == '5':
        break
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))

    if choice == '1': print("Result:", add(x, y))
    elif choice == '2': print("Result:", sub(x, y))
    elif choice == '3': print("Result:", mul(x, y))
    elif choice == '4': print("Result:", div(x, y))
    else: print("Invalid option")
