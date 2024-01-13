class dataBaseSystem:
    def newTask():
        open("Python/toDoList/database/_tasks.txt", "a") 
        print("Task Added")

    def deleteTask():
        open("Python/toDoList/database/_tasks.txt", "w")
        print("Task has been Removed")

    def editTask():
        open("Python/toDoList/database/_tasks.txt", "a")
        print("Task Updated")