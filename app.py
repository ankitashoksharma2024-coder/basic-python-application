def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def main():
    while True:
        print("\n--- MENU DRIVEN CALCULATOR ---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "5":
            print("Exiting...")
            break
            
        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice")
            continue
            
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Error: Please enter valid numbers.")
            continue
            
        if choice == "1":
            print("Result:", add(a, b))
        elif choice == "2":
            print("Result:", subtract(a, b))
        elif choice == "3":
            print("Result:", multiply(a, b))
        elif choice == "4":
            try:
                print("Result:", divide(a, b))
            except ValueError as e:
                print(e)

if __name__ == "__main__":
    main()
