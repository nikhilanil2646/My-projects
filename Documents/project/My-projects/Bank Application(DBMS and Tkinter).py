
import os
from tkinter import *
import time
import MySQLdb as sql
from getpass import getpass
count=1000
def signup():
        global root
        root.destroy()
        root=Tk()
        root.geometry("999x999")
        root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
        root.title("Bank Application With DBMS")
        global cur   
        cmd="select count(*) from user_info"
        cur.execute(cmd)
        addition=cur.fetchall()
        addition1=addition[0][0]
        global count
        count+=addition1
        Label(text="Enter your name: ",font="arial 15").grid(row=0,column=0)
        name=Text(root,font="Arial",width="50",height="1.2")
        name.grid(row=0,column=1)
        Label(text="Enter your Password: ",font="arial 15").grid(row=1,column=0)
        password=Text(root,font="Arial",width="50",height="1.2")
        password.grid(row=1,column=1)
        Label(text="Enter your Initial Balance: ",font="arial 15").grid(row=2,column=0)
        bal=Text(root,font="Arial",width="50",height="1.2")
        bal.grid(row=2,column=1)
        Button(text="Submit",font="Arial",height="3",command=lambda:create(name,password,bal,acc_no),
               fg="white",bg="blue").grid(ipadx=22,ipady=4,row=4,column=1)
        Button(root,text="Main Menu",font="Arial",height="2",command=lambda:mainfun(),fg="white",bg="blue").grid(row=4,column=2,ipadx=10,ipady=10)
        acc_no=count
def create(name,password,bal,acc_no):
        name=name.get("1.0","end-1c")
        password=password.get("1.0","end-1c")
        bal=bal.get("1.0","end-1c")
        acc_no=acc_no
        print(name,password,acc_no,bal)
        Label(text=f"Your generated account Number is {acc_no}",font="arial 15").grid()
        cmd="insert into user_info(name,password,bal,acc_no) values(%s,%s,%s,%s)"
        val=(name,password,bal,acc_no)             
        cur.execute(cmd,val)
        cmd="select * from user_info"      
        cur.execute(cmd)
        db.commit()      
        data=cur.fetchall() 
              
def edit(temp_acc_no):
     global root
     root.destroy()
     root=Tk()
     root.geometry("999x999")
     root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
     root.title("Bank Application With DBMS")
     Label(text="Welcome to your Account.",font="arial 28 italic",fg="blue").grid(columnspan=5,pady=40)   
     Button(root,text="Credit",height="1",font="Arial 20",command=lambda:credit(),fg="white",bg="blue").grid(row=1,column=2,padx=65,pady=150)
     Button(root,text="Debit",height="1",font="Arial 20",command=lambda:debit(),fg="white",bg="blue").grid(row=1,column=3,pady=150)
     Button(root,text="Check Balance",height="1",font="Arial 20",command=lambda:checkbal(),fg="white",bg="blue").grid(row=1,column=4,pady=150,padx=65)
     Button(root,text="Log-Out",height="1",font="Arial 20",command=lambda:mainfun(),fg="white",bg="blue").grid(row=1,column=5,pady=150)
     def credit():
        global root
        root.destroy()
        root=Tk()
        root.geometry("999x999")
        root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
        root.title("Bank Application With DBMS")
        Label(text="Enter amount to credit: ",font="arial 15").grid(row=0,column=0)
        temp_bal=Text(root,width="50",height="1.2") 
        temp_bal.grid(row=0,column=1)
        Button(text="Submit",font="Arial 20",height="3",command=lambda:creditdone(temp_bal),fg="white",bg="blue").grid(row=1,column=1)
        
     def creditdone(temp_bal):
         temp_bal=temp_bal.get("1.0","end-1c")
         cmd = "update user_info set bal=bal + %s where acc_no=%s"
         value=(temp_bal,temp_acc_no)     
         cur.execute(cmd,value)
         data=cur.fetchall()
         db.commit()     
         Label(text="Amount has been successfully credited to your account. ",font="Arial 17 italic").grid(row=2,columnspan=5)
         Button(text="<--Back",height="3",font="Lucida 20",command=lambda:edit(temp_acc_no),fg="white",bg="blue").grid(row=3,column=1)
     def debit():
        global root
        root.destroy()
        root=Tk()
        root.geometry("999x999")
        root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
        root.title("Bank Application With DBMS")
        Label(text="Enter amount to debit: ",font="arial 15").grid(row=0,column=0)
        temp_bal=Text(root,width="50",height="1.2") 
        temp_bal.grid(row=0,column=1)
        Button(text="Submit",font="Arial 20",height="3",command=lambda:debitdone(temp_bal),fg="white",bg="blue").grid(row=1,column=1,pady=40)
     def debitdone(temp_bal):
         temp_amount=int(temp_bal.get("1.0","end-1c"))
         cmd=f"select bal from user_info where acc_no={temp_acc_no}"
         cur.execute(cmd)
         data=cur.fetchall()              
         if temp_amount< data[0][0]:
             cmd = "update user_info set bal=bal - %s where acc_no=%s"
             value=(temp_amount,temp_acc_no)     
             cur.execute(cmd,value)
             Label(text="Amount has been successfully debited from your account. ",font="Arial 17 italic").grid(row=2,columnspan=5)
        
         else:
            Label(text="Insufficient Balance. ",font="Arial 17 italic").grid(row=2,columnspan=5)
         db.commit() 
         Button(text="<--Back",height="3",font="Lucida 20",command=lambda:edit(temp_acc_no),fg="white",bg="blue").grid(row=3,column=1)       
     def checkbal():
         cmd=f"select bal from user_info where acc_no = {temp_acc_no}"
         cur.execute(cmd) 
         data=cur.fetchall()     
         Label(text=f"\n\n         Your current balance is {data[0]}\n\n",font="Arial 17").grid(row=2,pady=50,columnspan=5) 
              
def login():
        global root
        root.destroy()
        root=Tk()
        root.geometry("999x999")
        root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
        root.title("Bank Application With DBMS")
        Label(root,text="Enter Account Number to Login",font="Arial 15").grid(row=0,column=0)
        temp_acc_no=Text(root,font="Arial",width="50",height="1.2")
        temp_acc_no.grid(row=0,column=1)
        Label(root,text="Enter Password: ",font="Arial 15").grid(row=1,column=0)
        temp_password=Text(root,font="Arial",width="50",height="1.2")
        temp_password.grid(row=1,column=1)
        Button(root,text="Submit",font="Arial 20",height="2",command=lambda:log(root,temp_acc_no,temp_password),
               fg="white",bg="blue").grid(row=2,column=0,pady=60,padx=90)
        Button(root,text="Main Menu",font="Arial 20",height="2",command=lambda:mainfun(),fg="white",bg="blue").grid(row=2,column=1)      
        def log(root,temp_acc_no,temp_password):
            temp_acc_no=temp_acc_no.get("1.0","end-1c")
            temp_password=temp_password.get("1.0","end-1c")          
            cmd="select acc_no from user_info" 
            cur.execute(cmd)        
            data=cur.fetchall()
            cmd = f"select password from user_info where acc_no=%s and password=%s"
            value=(temp_acc_no,temp_password)      
            cur.execute(cmd,value)
            data=cur.fetchall()
            if data :
             l1=Label(root,text="Access Granted.")
            else:
             l1=Label(root,text="Access denied.")
             return 0           
            l1.grid() 
            time.sleep(1)      
            Label(root,text="Your data is -----> ").grid()
            cmd=f"select * from user_info where acc_no={temp_acc_no}"
            cur.execute(cmd)
            data=cur.fetchall()
            edit(temp_acc_no)

db=sql.connect(host="127.0.0.1",port=3306,user="root",password="",database="bank")
cur=db.cursor()  
root=Tk()
root.geometry("999x999")
root.title("Bank Application With DBMS")
def pr():
    print("fun")
def mainfun():
    global root
    root.destroy()
    root=Tk()
    root.geometry("999x999")   
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))      
    Label(text="\tWelcome to Barbad Bank\n\n ",fg="red",font="Helvetica 33 bold italic").grid(row=0,columnspan=5,pady=30)
    Button(text="Login",font="Lucida 20 bold",command=lambda:login(),fg="white",bg="blue").grid(row=2,column=2)
    Button(text="Signup",font="Lucida 20 bold",command=lambda:signup(),fg="white",bg="blue").grid(row=2,column=3)
    Button(text="Exit",font="Lucida 20 bold",command=root.destroy,fg="white",bg="blue").grid(row=2,column=4)
    root.columnconfigure(40, weight=10)
    root.rowconfigure(3, weight=1)
mainfun()        
mainloop()
