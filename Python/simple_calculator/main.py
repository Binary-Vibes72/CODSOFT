def calculate(value_a, value_b):
        print("(1) --- Addition")
        print("(2) --- Subtraction")
        print("(3) --- Multiplication")
        print("(4) --- Division")
        choice = int(input("Enter the operation number: "))
        
        if choice == 1:
            print(f"The Addition of {value_a} and {value_b} is: {value_a + value_b}")

        elif choice == 2:
            print(f"The Subtraction of {value_a} and {value_b} is: {value_a - value_b}")

        elif choice == 3:
            print(f"The Multiplication of {value_a} and {value_b} is: {value_a * value_b}")

        elif choice == 4:
            print(f"The Division of {value_a} and {value_b} is: {value_a / value_b}")

        else:
            print("Invalid input. Try Again")

flag = True

while(flag):
    value_a = int(input("Enter the Value of a: "))
    value_b = int(input("Enter the Value of b: "))
    calculate(value_a, value_b)