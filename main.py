emp_list = []

while(True):
    first_num = input("Enter number: ")

    second_num = input("Enter number: ")

    emp_list.append(float(first_num))
    emp_list.append(float(second_num))

    total = sum(emp_list)
    
    print(total)

    get_input = input("Enter 'n' to exit: ")

    if get_input == 'n':
        break
    else:
        third_num = input("Enter number: ")

        emp_list.append(float(third_num))

        total = sum(emp_list)
        
        print(total)
        
        break