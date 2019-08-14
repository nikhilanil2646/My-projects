<<<<<<< HEAD
import os
import time
from getpass import getpass
def cls():
   os.system('cls')
class bank:
    count=1000
    acc=dict()
    def __init__(self):
        bank.count+=1
        self.data=dict()
        self.data.update(name=input("Enter name: "),password=getpass("Enter password: "),
                         bal=int(input("Enter initial balance: ")),acc_no=bank.count)
        bank.acc.update([(self.data['acc_no'] , self.data['password'])])
        print(f"\n\nYour generated Account Number is : {self.data['acc_no']}\n\n ")
        input("...Press Enter key...".center(60))
              
    def edit(self):

     while True:
      cls()  
      print("Enter 1. Credit\nEnter 2. Debit\nEnter 3. Check Balance\nEnter 4. Logout ")
      ch=int(input("Enter choice: "))
      global b 
      if ch==1:
         self.data['bal']+=int(input("Enter Amount to Credit: "))
         print("\n\n          Amount has been succesfully credited to your account\n\n ")
         input("...Press Enter key...".center(90))
      elif ch==2:
         temp_amount=int(input("Enter Amount to Debit: "))   
         if temp_amount< self.data['bal']:
            self.data['bal']-=temp_amount
            print("\n\n          Amount has been succesfully debited from your account\n\n ")
         else:
            print("Your current balance is low. Please try lower Amount. ")
         
         input("...Press Enter key...".center(90))
      elif ch==3:
         print(f"\n\n         Your current balance is {self.data['bal']}\n\n")
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
        if temp_acc_no in bank.acc.keys():
              print("Account exists.\n ")
        else:
              print("Account not exist")
              input("...Press Enter key...".center(90))
              return 0
        temp_password=getpass("Enter password: ")
        if temp_password==bank.acc[temp_acc_no]:
              print("Access Granted ".center(90))
        else:
              print("Access Denied ".center(90))
              input("...Press Enter key...".center(90))
              return 0
        
        num=temp_acc_no%1000    
        global b
        print("\n Data is--->")
        print(b[num].data)

        print("\n\n")
        print("Please wait Logging in...".center(90))
        time.sleep(2.2)
        b[num].edit()
             
              
                     

        
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
        exit(1)
       
start()        
=======
import os
import time
from getpass import getpass
def cls():
   os.system('cls')
class bank:
    count=1000
    acc=dict()
    def __init__(self):
        bank.count+=1
        self.data=dict()
        self.data.update(name=input("Enter name: "),password=getpass("Enter password: "),
                         bal=int(input("Enter initial balance: ")),acc_no=bank.count)
        bank.acc.update([(self.data['acc_no'] , self.data['password'])])
        print(f"\n\nYour generated Account Number is : {self.data['acc_no']}\n\n ")
        input("...Press Enter key...".center(60))
              
    def edit(self):

     while True:
      cls()  
      print("Enter 1. Credit\nEnter 2. Debit\nEnter 3. Check Balance\nEnter 4. Logout ")
      ch=int(input("Enter choice: "))
      global b 
      if ch==1:
         self.data['bal']+=int(input("Enter Amount to Credit: "))
         print("\n\n          Amount has been succesfully credited to your account\n\n ")
         input("...Press Enter key...".center(90))
      elif ch==2:
         temp_amount=int(input("Enter Amount to Debit: "))   
         if temp_amount< self.data['bal']:
            self.data['bal']-=temp_amount
            print("\n\n          Amount has been succesfully debited from your account\n\n ")
         else:
            print("Your current balance is low. Please try lower Amount. ")
         
         input("...Press Enter key...".center(90))
      elif ch==3:
         print(f"\n\n         Your current balance is {self.data['bal']}\n\n")
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
        if temp_acc_no in bank.acc.keys():
              print("Account exists.\n ")
        else:
              print("Account not exist")
              input("...Press Enter key...".center(90))
              return 0
        temp_password=getpass("Enter password: ")
        if temp_password==bank.acc[temp_acc_no]:
              print("Access Granted ".center(90))
        else:
              print("Access Denied ".center(90))
              input("...Press Enter key...".center(90))
              return 0
        
        num=temp_acc_no%1000    
        global b
        print("\n Data is--->")
        print(b[num].data)

        print("\n\n")
        print("Please wait Logging in...".center(90))
        time.sleep(2.2)
        b[num].edit()
             
              
                     

        
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
        exit(1)
       
start()        
>>>>>>> ffa54a7009b3986a920100cbf48d0af75002874e
