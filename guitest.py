#!/usr/bin/python
from Tkinter import *


class sqlapi():
    pass
    #acces sql server
    #send request
    #receive/parse answer
    #sql server has one table with name,passwd,email,unique id

class cli(): #should be function not class?
    pass
    #check if valid command
    #regex to find correct command
    #call method of command and pass rest of string
    #regex to read arguments 
    #methods of commands takes rest of string

def donothing():  #dummy function
    pass

root = Tk()


#here we create the menubar


menu = Menu(root)
root.config(menu=menu)


# the file menu
fileMenu = Menu(menu)
menu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Login",command=donothing)
fileMenu.add_command(label="Exit", command=root.destroy)

#the edit menu
editMenu = Menu(menu)
menu.add_cascade(label="edit", menu=editMenu)
editMenu.add_command(label="example", command=donothing)

btnExit = Button(root, text="Exit", command=root.destroy)
btnExit.pack()

root.mainloop()
