emp_list = []

def addition(x, y):
    total = x + y
    emp_list.append(total)

def substration(x, y):
    total = x - y
    emp_list.append(total)

def multiply(x, y):
    total = x * y
    emp_list.append(total)

def divide(x, y):
    total = x / y
    emp_list.append(total)

first_num = float(input("Enter number: "))

operation_choice = input("What operation: ")

if operation_choice == "add":
    second_num = float(input("Enter second number: "))

    addition(first_num, second_num)
elif operation_choice == "minus":
    second_num = float(input("Enter second number: "))

    substration(first_num, second_num)
elif operation_choice == "times":
    second_num = float(input("Enter second number: "))

    multiply(first_num, second_num)
elif operation_choice == "divide":
    second_num = float(input("Enter second number: "))

    divide(first_num, second_num)
else:
    print(emp_list)

get_total = sum(emp_list)

continue_choice = input("Enter n to stop: ")

if continue_choice == 'n':

    print(get_total)

else:
    while(True):

        third_number = float(input("Enter number: "))

        get_total = get_total + third_number

        print(get_total)