from tkinter import *
from dataBaseSystem import *

window = Tk()
window.title("To Do list Manager")
window.minsize(height=600, width=500)

def addTask():
    dataBaseSystem.newTask()

def removeTask():
    dataBaseSystem.deleteTask()

def updateTask():
    dataBaseSystem.editTask()

newTaskButton = Button(text="Add Task", command=addTask)
newTaskButton.pack()

removeTaskButton = Button(text="Remove Task", command=removeTask)
removeTaskButton.pack()

updateTaskButton = Button(text="Edit task", command=updateTask)
updateTaskButton.pack()

window.mainloop()