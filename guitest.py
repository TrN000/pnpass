#!/usr/bin/python
from Tkinter import *
import tkMessageBox
import MySQLdb


class sqlacces():

    def __init__(self):

        db = MySQLdb.connect(host="localhost", user="demouser", passwd="demopassword", db="demodb")   #how to connect to database
        
        cur = db.cursor()
   
    def checkuser(self, name):

        cur.execute("select * from users where name = %s", [name])
        
        if cur.rowcount >0:
            return True
        else:
            return False


    def acces(self):
        pass

    def createu(self):
        pass

    def login(self):
        pass

    def printall(self):
        pass

    #acces sql server
    #send request
    #receive/parse answer
    #sql server has one table with name,passwd,email,unique id

class cli(Text): #should be function not class?
    pass
    #using a text() widget(according to some gui on the internet)
    #check if valid command
    #regex to find correct command
    #call method of command and pass rest of string
    #regex to read arguments 
    #methods of commands takes rest of string

def donothing():  #dummy function
    pass

def helpmenu():
    tkMessageBox.showinfo("shhhh", "no tears, only dreams now")

def createloginwindow():
    def checklogin():
        #here sql acces check
        db = sqlacces()
        u = unameInput.get()
        p = passwInput.get()
        db.checkuser(u)
        if True:
            tkMessageBox.showinfo("", "login succesful")
            
            top.destroy()

    top = Toplevel()

    uname = Label(top, text="user name:")
    uname.grid(column=1, row=1)
    unameInput = Entry(top)
    unameInput.grid(column=2, row=1)

    passw = Label(top, text="password:")
    passw.grid(column=1, row=2)
    passwInput = Entry(top)
    passwInput.grid(column=2, row=2)

    login = Button(top, text="Login", command=checklogin)
    login.grid(column=1, row=5)
    button = Button(top, text="Cancel", command=top.destroy)
    button.grid(column=2, row=5)


db = MySQLdb.connect(host="localhost", user="demouser", passwd="demopassword", db="demodb")   #how to connect to database

cur = db.cursor()  #need to define a cursor to work

cur.execute("select * from users;") # how to execute queries



root = Tk()


#here we create the menubar


menu = Menu(root)
root.config(menu=menu)


# the file menu
fileMenu = Menu(menu)
menu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Login",command=createloginwindow)
fileMenu.add_command(label="Login to personal SQL", command=createloginwindow)
fileMenu.add_command(label="Exit", command=root.destroy)

#the edit menu
editMenu = Menu(menu)
menu.add_cascade(label="edit", menu=editMenu)
editMenu.add_command(label="example", command=donothing)

#help menu
helpMenu = Menu(menu)
menu.add_command(label="Help", command=helpmenu) 


button = Button(text="close", command=root.destroy)
button.pack()

root.mainloop()
