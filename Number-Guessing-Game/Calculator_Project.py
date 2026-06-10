print("Welcome to our Calculator")
while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = input("Enter your choice (1-4): ")
    if choice =="5":
        print("Thank you for using the calculator")
    num1 = float(input("Enter First number: "))
    num2 = float(input("Enter Second number: "))
    if choice =="1":
        result = num1 + num2
        print("Answer=", result)
    elif choice =="2":
        result = num1 - num2
        print("Answer =", result)
    elif choice == "3":
        result = num1 * num2
        print("Answer = ", result)
    elif choice == "4":
        if num2 != 0:
            result = num1 / num2
            print("Answer = ", result)
        else:
            print("Cannot divide by zero!")
    else:
        print("Invalid Choice!")