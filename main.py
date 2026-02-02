# Simple Calculator
# Author: VOLTINO84
# Beginner Python project – learning by doing.
# Feel free to use or modify this code.
# Credit is appreciated if you share or republish it.
 
print("""Calculator
by VOLTINO84
- - - - - - - - - - - -
Commmands:
1...+ (addition)
2...- (subtraction)
3...* (multiplication)
4.../ (division)
5...exit program"""
)
 
while True:
    cmd = input("Command: ")
    match cmd:
        case "1":
            try:
                a = float(input("1st number: "))
                b = float(input("2nd number: "))
            except ValueError:
                print("Only numbers are accepted!")
                continue
            print("Result: ",a + b)
        case "2":
            try:
                a = float(input("1st number: "))
                b = float(input("2nd number: "))
            except ValueError:
                print("Only numbers are accepted!")
                continue
            print("Result: ",a - b)
        case "3":
            try:
                a = float(input("1st number: "))
                b = float(input("2nd number: "))
            except ValueError:
                print("Only numbers are accepted!")
                continue
            print("Result: ",a * b)
        case "4":
            try:
                a = float(input("1st number: "))
                b = float(input("2nd number: "))
            except ValueError:
                print("Only numbers are accepted!")
                continue
            print("Result: ",a / b)
        case "5":
            print("Program terminated!")
            break
        case _:
            print("Invalid command!")