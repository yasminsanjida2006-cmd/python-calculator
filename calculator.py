
def calculator():
    print("\n===== PYTHON CALCULATOR 2.0 =====")

    while True:
        print("\nChoose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "5":
            print("Thank you for using Calculator!")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice! Try again.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

        except ValueError:
            print("Please enter valid numbers!")
            continue

        if choice == "1":
            result = num1 + num2

        elif choice == "2":
            result = num1 - num2

        elif choice == "3":
            result = num1 * num2

        elif choice == "4":
            if num2 == 0:
                print("Cannot divide by zero!")
                continue
            result = num1 / num2

        print("Result:", result)

calculator()
