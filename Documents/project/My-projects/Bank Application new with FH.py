<<<<<<< HEAD
import os
import os.path
import time
import copy
import json
from getpass import getpass
def cls():
   os.system('cls')
class bank:
    count=1000
    acc=dict()
    def __init__(self):
        bank.count+=1
        while os.path.isfile(f"./app_data/{str(bank.count)}"):
           bank.count+=1
           continue
        self.data=dict()
        self.data.update(name=input("Enter name: "),password=getpass("Enter password: "),
                         bal=int(input("Enter initial balance: ")),acc_no=bank.count)
        bank.acc.update([(self.data['acc_no'] , self.data['password'])])
        print(f"\n\nYour generated Account Number is : {self.data['acc_no']}\n\n ")
        input("...Press Enter key...".center(60))
        path=copy.copy(self.data['acc_no'])
        path=str(path)
        fp=open(f"./app_data/{str(path)}","w")
        json.dump(self.data,fp)
        fp.close()
        
              
def edit(temp_data,temp_acc_no):

     while True:
      cls()  
      print("Enter 1. Credit\nEnter 2. Debit\nEnter 3. Check Balance\nEnter 4. Logout ")
      ch=int(input("Enter choice: "))
      global b 
      if ch==1:
         temp_data['bal']+=int(input("Enter Amount to Credit: "))
         
         print(temp_data)
         fp=open(f"./app_data/{str(temp_acc_no)}",'w')
         json.dump(temp_data,fp)
         fp.close()
         
         print("\n\n          Amount has been succesfully credited to your account\n\n ")
         input("...Press Enter key...".center(90))
      elif ch==2:
         temp_amount=int(input("Enter Amount to Debit: "))   
         if temp_amount< temp_data['bal']:
            temp_data['bal']-=temp_amount
            fp=open(f"./app_data/{str(temp_acc_no)}",'w')
            json.dump(temp_data,fp)
            fp.close()
            print("\n\n          Amount has been succesfully debited from your account\n\n ")
         else:
            print("Your current balance is low. Please try lower Amount. ")
         
         input("...Press Enter key...".center(90))
      elif ch==3:
         fp=open(f"./app_data/{str(temp_acc_no)}",'r')
         temp_databal=json.load(fp)
         print("Your current account balance: ",temp_databal['bal'])
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
        if os.path.isfile(f"./app_data/{str(temp_acc_no)}"):
              print("Account exists.\n ")
        else:
              print("Account not exist")
              input("...Press Enter key...".center(90))
              return 0
            
        temp_password=getpass("Enter password: ")
        fp=open(f"./app_data/{str(temp_acc_no)}",'r')
        temp_data = json.load(fp)
        fp.close()
        
        if temp_password == temp_data['password']:
              print("Access Granted ".center(90))
        else:
              print("Access Denied ".center(90))
              input("...Press Enter key...".center(90))
              return 0
        
        num=temp_acc_no%1000    
        global b
        print("\n Data is--->")
        
        print(temp_data)

        print("\n\n")
        print("Please wait Logging in...".center(90))
        time.sleep(2.2)
        edit(temp_data,temp_acc_no)
             
              
                     

        
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
import os.path
import time
import copy
import json
from getpass import getpass
def cls():
   os.system('cls')
class bank:
    count=1000
    acc=dict()
    def __init__(self):
        bank.count+=1
        while os.path.isfile(f"./app_data/{str(bank.count)}"):
           bank.count+=1
           continue
        self.data=dict()
        self.data.update(name=input("Enter name: "),password=getpass("Enter password: "),
                         bal=int(input("Enter initial balance: ")),acc_no=bank.count)
        bank.acc.update([(self.data['acc_no'] , self.data['password'])])
        print(f"\n\nYour generated Account Number is : {self.data['acc_no']}\n\n ")
        input("...Press Enter key...".center(60))
        path=copy.copy(self.data['acc_no'])
        path=str(path)
        fp=open(f"./app_data/{str(path)}","w")
        json.dump(self.data,fp)
        fp.close()
        
              
def edit(temp_data,temp_acc_no):

     while True:
      cls()  
      print("Enter 1. Credit\nEnter 2. Debit\nEnter 3. Check Balance\nEnter 4. Logout ")
      ch=int(input("Enter choice: "))
      global b 
      if ch==1:
         temp_data['bal']+=int(input("Enter Amount to Credit: "))
         
         print(temp_data)
         fp=open(f"./app_data/{str(temp_acc_no)}",'w')
         json.dump(temp_data,fp)
         fp.close()
         
         print("\n\n          Amount has been succesfully credited to your account\n\n ")
         input("...Press Enter key...".center(90))
      elif ch==2:
         temp_amount=int(input("Enter Amount to Debit: "))   
         if temp_amount< temp_data['bal']:
            temp_data['bal']-=temp_amount
            fp=open(f"./app_data/{str(temp_acc_no)}",'w')
            json.dump(temp_data,fp)
            fp.close()
            print("\n\n          Amount has been succesfully debited from your account\n\n ")
         else:
            print("Your current balance is low. Please try lower Amount. ")
         
         input("...Press Enter key...".center(90))
      elif ch==3:
         fp=open(f"./app_data/{str(temp_acc_no)}",'r')
         temp_databal=json.load(fp)
         print("Your current account balance: ",temp_databal['bal'])
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
        if os.path.isfile(f"./app_data/{str(temp_acc_no)}"):
              print("Account exists.\n ")
        else:
              print("Account not exist")
              input("...Press Enter key...".center(90))
              return 0
            
        temp_password=getpass("Enter password: ")
        fp=open(f"./app_data/{str(temp_acc_no)}",'r')
        temp_data = json.load(fp)
        fp.close()
        
        if temp_password == temp_data['password']:
              print("Access Granted ".center(90))
        else:
              print("Access Denied ".center(90))
              input("...Press Enter key...".center(90))
              return 0
        
        num=temp_acc_no%1000    
        global b
        print("\n Data is--->")
        
        print(temp_data)

        print("\n\n")
        print("Please wait Logging in...".center(90))
        time.sleep(2.2)
        edit(temp_data,temp_acc_no)
             
              
                     

        
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
