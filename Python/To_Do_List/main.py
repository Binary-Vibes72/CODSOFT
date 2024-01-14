import time

# Variable Declartaion
flag = True
database_file = "Python/To_Do_List/database/data.txt"

# function Declration
def last_record():
    last_record = ""

    #This function reads "database_file" file and assign the each line to a "last record" variable so assign 
    #the data to a same variable gives us last line of a data present in the "data.txt", and return that 
    #variable.
    with open(database_file, "r") as data:
        for line in data:
            last_record = line
    return last_record

def new_task():
    #Takes the "Task_title, task_description, task_time" as a input from a user. 
    #and the we call to last_record function and manipulate the variable to get a series number of 
    #that last record so we can assign the next series to a new task.
    task_title = input("Enter the title of New Task: ")
    task_description = input("Enter the description for new Task: ")
    task_time = time.ctime()
    with open(database_file, "a+") as data:
        data.write(f"{int((last_record().split('#'))[0]) + 1}# {task_title}# {task_description}# {task_time}\n")
        
        print("Task has been created.")
        data.close()

def show_data():
    print("\n")
    with open(database_file, "r") as data:
        # Here,
        # data = All the content in the data
        # if we iterate through the data using for loop then we get a list of words named as record.
        # Then we iterate through the record manipulate the record to print the desied output to show the tasks.

        for line in data:
            record = line.split("#")
            if int(record[0]) != 0:
                sentence = ""
                for _ in record:
                    if record.index(_) == 3:
                        sentence += _ + " "
                    else:
                        sentence += _ + " | "
                print(sentence)
    print("\n")

def remove_record(series_number):
            # First we open the data file using read mode and then put all the lines in inputfiledata 
            #variable and initiated lineindex = 1
            with open(database_file , 'r') as data:
                inputfiledata = data.readlines()
                lineindex = 1
            
            # Then open the data file with write mode and iterate through the inputfiledata variable. 
            #if the series_number is present in the list then skip the line from writing and print 
            #the rest of the file.     
            with open(database_file, 'w') as data:
                for number, line in enumerate(inputfiledata):
                    if number not in [series_number]:
                        data.write(line)
                        lineindex += 1
            print(f"The record {series_number} sucessfully removed")

def remove():
    while(True):
        series_number = int(input("Enter the series number to be removed from above list: "))
        if series_number <= int((last_record().split("#"))[0]):
            print("Please conferme the remove operation. This can not undo!!!")
            choice = input("Type 'yes' for processesing or Press any keyboard character and press enter to cancel: ")
            if choice == "yes":
                remove_record(series_number)
                break
            else:
                print("Operation has been terminated.")
                break
        else:
            print("Invalid Task series number. Try again.")


def update_record(series_number):
    # First we open the data file using read mode and then put all the lines in inputfiledata variable 
    #and initiated lineindex = 1
    with open(database_file , 'r') as data:
        inputfiledata = data.readlines()
        lineindex = 1

    # Then open the data file with write mode and iterate through the inputfiledata variable. 
    #if the series_number is present in the list then skip the line from writing and print the rest of the file.     
    with open(database_file, 'w') as data:
        for number, line in enumerate(inputfiledata):
            if number+1 == series_number:
                task_title = input("Enter the Task Title: ")
                task_description = input("Enter the Task description: ")
                task_time = time.ctime()
                new_data = f"{series_number}# {task_title}# {task_description}# {task_time}\n"
                data.write(new_data)
                number += 1
            else:
                data.write(line)
            lineindex += 1
    print(f"The record {series_number} sucessfully Updated")

def update():
    while(True):
        series_number = int(input("Enter the series number to be update from above list: "))

        if series_number <= int((last_record().split("#"))[0]):
            print("Please conferme the remove operation. This can not undo!!!")
            choice = input("Type 'yes' for processesing or Press any keyboard character and press enter to cancel: ")
            if choice == "yes":
                update_record(series_number)
                break
            else:
                print("Operation has been terminated.")
                break
        else:
            print("Invalid Task series number. Try again.")

# Main Program
while(flag):
    with open(database_file, "r+") as data:
        if data.readlines() == []:
            init_data = "0# task_title# task_discription# task_time\n"
            data.write(init_data)

    print("(1) Add new Task")
    print("(2) Remove Task")
    print("(3) Update Task")
    print("(4) Show Task")
    print("(0) Exit")
    choice = int(input("Enter your Choice: "))

    if(choice == 1):
        new_task()

    elif(choice == 2):
        show_data()
        remove()
        
    elif(choice == 3):
        show_data()
        update()

    elif(choice == 4):
        show_data()

    elif(choice == 0):
        flag = False
        break
    
    else:
        print("Invalid Choice")