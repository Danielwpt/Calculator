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

second_num = float(input("Enter number: "))

operations = {
    "addition": addition,
    "minus": substration,
    "times": multiply,
    "divide": divide,
}

operations = operations[operation_choice]

operations(first_num, second_num)

print(emp_list)