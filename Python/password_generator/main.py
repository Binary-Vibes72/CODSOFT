from module.char import *
from random import *

def password(password_length, condition_results):
    raw_password = []
    password = ''
    for count in range(len(condition_results)):
        if condition_results[count] == 'y':
            if count == 0:
                for _ in lower_alphabets:
                    raw_password.append(_)
                
            if count == 1:
                for _ in upper_alphabets:
                    raw_password.append(_)
            
            if count == 2:
                for _ in digits:
                    raw_password.append(_)
    
    for length in range(0, password_length):
        password += choice(raw_password)

    return password

def condition_checker(condition):
    if condition == 'y' or condition == 'n' or condition.isdigit():
        return False
    else:
        return True
    
print("Password Generator")

conditions = [
    "Enter the length of Password in digits only: ",
    "Do you want to include Lower Case Characters in your password (y/n): ",
    "Do you want to include Upper Case Characters in your password (y/n): ",
    "Do you want to include Digits in your password (y/n): "
    ]

condition_results = []
password_length = 0
generate_new = True

while(generate_new):
    for condition in range(len(conditions)):
        flag = True
        while(flag):
            _input = input(conditions[condition])

            if condition == 0:
                int(_input)

            flag = condition_checker(_input)
            
            if _input.isdigit() and flag == False:
                password_length = int(_input)
            elif flag == False:
                condition_results.append(_input)
            else:
                print("\n!!! Invalid Input. Try Again !!!\n")

    print(f"\nPassword: {password(password_length, condition_results)}\n")

    generate_new = True
    while(generate_new):
        _continue = input("Do you want to Generate new Password (y/n): ")
        if _continue == 'y':
            generate_new == False
            break
        elif _continue == 'n':
            generate_new = False
            break
        else:
            print("\n!!! Invalid Input. Try Again !!!\n")
    