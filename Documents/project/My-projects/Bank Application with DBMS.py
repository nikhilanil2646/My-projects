<<<<<<< HEAD
import os
import time
import MySQLdb as sql
from getpass import getpass
def cls():
   os.system('cls')
class bank:
    count=1000
    
    def __init__(self):
        global cur   
        cmd="select count(*) from user_info"
        cur.execute(cmd)
        addition=cur.fetchall()
        addition1=addition[0][0]
        bank.count+=addition1
        self.data=dict()
        name=input("Enter name: ")
        password=getpass("Enter password: ")
        bal=int(input("Enter initial balance: "))
        acc_no=bank.count
        print(f"\n\nYour generated Account Number is : {acc_no}\n\n ")
        cmd="insert into user_info(name,password,bal,acc_no) values(%s,%s,%s,%s)"
        val=(name,password,bal,acc_no)      
           
        cur.execute(cmd,val)
        cmd="select * from user_info"      
        cur.execute(cmd)
        db.commit()      
        data=cur.fetchall() 
        input("...Press Enter key...".center(60))
              
    def edit(temp_acc_no):

     while True:
      cls()  
      print("Enter 1. Credit\nEnter 2. Debit\nEnter 3. Check Balance\nEnter 4. Logout ")
      ch=int(input("Enter choice: "))
      global b 
      if ch==1:
         
         temp_bal=int(input("Enter Amount to Credit: "))
         cmd = "update user_info set bal=bal + %s where acc_no=%s"
         value=(temp_bal,temp_acc_no)     
         cur.execute(cmd,value)
         data=cur.fetchall()
         db.commit()     
         print("\n\n          Amount has been succesfully credited to your account\n\n ")
         input("...Press Enter key...".center(90))
      elif ch==2:
         temp_amount=int(input("Enter Amount to Debit: "))
         cmd=f"select bal from user_info where acc_no={temp_acc_no}"
         cur.execute(cmd)
         data=cur.fetchall()
              
         if temp_amount< data[0][0]:
             cmd = "update user_info set bal=bal - %s where acc_no=%s"
             value=(temp_amount,temp_acc_no)     
             cur.execute(cmd,value)
             print("\n\n          Amount has been succesfully debited from your account\n\n ")
         else:
            print("Your current balance is low. Please try lower Amount. ")
         db.commit()
         input("...Press Enter key...".center(90))
      elif ch==3:
         cmd=f"select bal from user_info where acc_no = {temp_acc_no}"
         cur.execute(cmd) 
         data=cur.fetchall()     
         print(f"\n\n         Your current balance is {data[0]}\n\n")
         input("...Press Enter key...".center(90))
         
      elif ch==4:
         print("\n\n") 
         print(" Logging out... ".center(90))
         time.sleep(2)
         return 0
      else:
         print("\n\n          Entered wrong Choice ")
         
   
              
def login():
        temp_acc_no=int(input("Enter account number: ")) 
        print(temp_acc_no)       
        cmd="select acc_no from user_info" 
        cur.execute(cmd)
        data=cur.fetchall()   
        if temp_acc_no in data:
              print("Account exists.\n ")
        else:
              pass
        temp_password=getpass("Enter password: ")
        cmd = f"select password from user_info where acc_no=%s and password=%s"
        value=(temp_acc_no,temp_password)      
        cur.execute(cmd,value)
        data=cur.fetchall()
        if data :
              print("Access Granted ".center(90))
        else:
              print("Access Denied ".center(90))
              input("...Press Enter key...".center(90))
              return 0
        
        num=temp_acc_no%1000    
        global b
        print("\n Data is--->")
        cmd=f"select * from user_info where acc_no={temp_acc_no}"
        cur.execute(cmd)
        data=cur.fetchall()
        print(f"Name: {data[0][0]}\nPassword: {data[0][1]}\nAmount: {data[0][2]}\nAccount Number: {data[0][3]}")

        print("\n\n")
        print("Please wait Logging in...".center(90))
        time.sleep(2.2)
        bank.edit(temp_acc_no)
             
              
                     

        
b=[0]        
def start():
  i=1
  global b
             
  while True:
    cls()
    print("***BANK APPLICATION***".center(100))
    print("\n\n\n")
    print("Enter 1. Log-in\nEnter 2. Sign-up\nEnter 3. Exit")
    choice=int(input("Enter choice: "))
    cls()
    if choice==1:
        login()
    elif choice==2:
        b.append(bank())
        i+=1       
    elif choice==3:
        return 0
               
db=sql.connect(host="127.0.0.1",port=3306,user="root",password="",database="bank")
cur=db.cursor()         
start()        
=======
import os
import time
import MySQLdb as sql
from getpass import getpass
def cls():
   os.system('cls')
class bank:
    count=1000
    
    def __init__(self):
        global cur   
        cmd="select count(*) from user_info"
        cur.execute(cmd)
        addition=cur.fetchall()
        addition1=addition[0][0]
        bank.count+=addition1
        self.data=dict()
        name=input("Enter name: ")
        password=getpass("Enter password: ")
        bal=int(input("Enter initial balance: "))
        acc_no=bank.count
        print(f"\n\nYour generated Account Number is : {acc_no}\n\n ")
        cmd="insert into user_info(name,password,bal,acc_no) values(%s,%s,%s,%s)"
        val=(name,password,bal,acc_no)      
           
        cur.execute(cmd,val)
        cmd="select * from user_info"      
        cur.execute(cmd)
        db.commit()      
        data=cur.fetchall() 
        input("...Press Enter key...".center(60))
              
    def edit(temp_acc_no):

     while True:
      cls()  
      print("Enter 1. Credit\nEnter 2. Debit\nEnter 3. Check Balance\nEnter 4. Logout ")
      ch=int(input("Enter choice: "))
      global b 
      if ch==1:
         
         temp_bal=int(input("Enter Amount to Credit: "))
         cmd = "update user_info set bal=bal + %s where acc_no=%s"
         value=(temp_bal,temp_acc_no)     
         cur.execute(cmd,value)
         data=cur.fetchall()
         db.commit()     
         print("\n\n          Amount has been succesfully credited to your account\n\n ")
         input("...Press Enter key...".center(90))
      elif ch==2:
         temp_amount=int(input("Enter Amount to Debit: "))
         cmd=f"select bal from user_info where acc_no={temp_acc_no}"
         cur.execute(cmd)
         data=cur.fetchall()
              
         if temp_amount< data[0][0]:
             cmd = "update user_info set bal=bal - %s where acc_no=%s"
             value=(temp_amount,temp_acc_no)     
             cur.execute(cmd,value)
             print("\n\n          Amount has been succesfully debited from your account\n\n ")
         else:
            print("Your current balance is low. Please try lower Amount. ")
         db.commit()
         input("...Press Enter key...".center(90))
      elif ch==3:
         cmd=f"select bal from user_info where acc_no = {temp_acc_no}"
         cur.execute(cmd) 
         data=cur.fetchall()     
         print(f"\n\n         Your current balance is {data[0]}\n\n")
         input("...Press Enter key...".center(90))
         
      elif ch==4:
         print("\n\n") 
         print(" Logging out... ".center(90))
         time.sleep(2)
         return 0
      else:
         print("\n\n          Entered wrong Choice ")
         
   
              
def login():
        temp_acc_no=int(input("Enter account number: ")) 
        print(temp_acc_no)       
        cmd="select acc_no from user_info" 
        cur.execute(cmd)
        data=cur.fetchall()   
        if temp_acc_no in data:
              print("Account exists.\n ")
        else:
              pass
        temp_password=getpass("Enter password: ")
        cmd = f"select password from user_info where acc_no=%s and password=%s"
        value=(temp_acc_no,temp_password)      
        cur.execute(cmd,value)
        data=cur.fetchall()
        if data :
              print("Access Granted ".center(90))
        else:
              print("Access Denied ".center(90))
              input("...Press Enter key...".center(90))
              return 0
        
        num=temp_acc_no%1000    
        global b
        print("\n Data is--->")
        cmd=f"select * from user_info where acc_no={temp_acc_no}"
        cur.execute(cmd)
        data=cur.fetchall()
        print(f"Name: {data[0][0]}\nPassword: {data[0][1]}\nAmount: {data[0][2]}\nAccount Number: {data[0][3]}")

        print("\n\n")
        print("Please wait Logging in...".center(90))
        time.sleep(2.2)
        bank.edit(temp_acc_no)
             
              
                     

        
b=[0]        
def start():
  i=1
  global b
             
  while True:
    cls()
    print("***BANK APPLICATION***".center(100))
    print("\n\n\n")
    print("Enter 1. Log-in\nEnter 2. Sign-up\nEnter 3. Exit")
    choice=int(input("Enter choice: "))
    cls()
    if choice==1:
        login()
    elif choice==2:
        b.append(bank())
        i+=1       
    elif choice==3:
        return 0
               
db=sql.connect(host="127.0.0.1",port=3306,user="root",password="",database="bank")
cur=db.cursor()         
start()        
>>>>>>> ffa54a7009b3986a920100cbf48d0af75002874e
