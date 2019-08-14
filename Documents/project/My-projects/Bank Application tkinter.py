<<<<<<< HEAD
import os
import time
def cls():
   os.system('cls')
b=[0]
i=1
def create(nameentry,passwdentry,initbalentry):
  nameentry1=nameentry.get("1.0","end-1c")
  passwdentry1=passwdentry.get("1.0","end-1c")
  initbalentry1=initbalentry.get("1.0","end-1c")
  global b
  global i
  b.append(bank(nameentry1,passwdentry1,initbalentry1))
  i+=1
  Label(root, text="account has been created: "+ str(bank.count),font=("Algerian",20),bg="red",fg="white").pack()


from tkinter import *
from tkinter.messagebox import *
root=Tk()
root.geometry("999x999")
root.title("Bank Application")
Label(root, text= "Welcome to Bank " ,font="lucida 19 bold").pack()
Button(root,text='LOGIN',command=lambda:Entryfunc_login()).pack()
Button(root,text='sign-up',command=lambda:Entryfunc_create()).pack()
Button(root,text='Exit',command=root.destroy).pack()
def Entryfunc_create():
 Label(root, text="Enter account Holder's Name: ").pack()   
 nameentry = Text(root, font=("Arial"), width="50", height="1.2")
 nameentry.pack()
 Label(root, text="Set new Password: ").pack() 
 passwdentry = Text(root,font=("Arial"), width="50", height="1.2")
 passwdentry.pack()
 Label(root, text="Enter the Initial Balance to be credited: ").pack() 
 initbalentry = Text(root,font=("Arial"), width="50", height="1.2")
 initbalentry.pack()
 Button(root,text='Submit',command=lambda:create(nameentry,passwdentry,initbalentry)).pack()
 
  

def Entryfunc_login():
 acc_no=IntVar()
 passwd_login=StringVar()
 Label(root, text="Enter account no: ").pack()
 acc_noentry=Text(root, font=("Arial"), width="50", height="1.2")
 acc_noentry.pack()
 Label(root, text="Enter password: ").pack()
 passwd_entry= Text(root, font=("Arial"), width="50", height="1.2")
 passwd_entry.pack()
 Button(root,text='Submit',command=lambda:login_tk(acc_noentry,passwd_entry)).pack()




def login_tk(acc_noentry,passwd_entry):
   acc_noentry1=acc_noentry.get("1.0","end-1c")
   passwd_entry1=passwd_entry.get("1.0","end-1c")
   login(acc_noentry1,passwd_entry1)
    
    


class bank:
    count=1000
    acc=dict()
    def __init__(self,name_get,passwd_get,bal_get):
        bank.count+=1
        self.data=dict()
        self.data.update(name=name_get,password=passwd_get,
                         bal=bal_get,acc_no=bank.count)
        bank.acc.update([(self.data['acc_no'] , self.data['password'])])
        msg=f"Your generated Account Number is : {self.data['acc_no']}"
        
        #input("...Press Enter key...".center(60))
              
    def edit(self):
       Button(root,text='Credit',command=lambda:credit(self)).pack()
       Button(root,text='Debit',command=lambda:debit(self)).pack()
       Button(root,text='Check Balance',command=lambda:checkbal(self)).pack()

       def credit(self):
         top=Toplevel()
         Label(top, text="Enter Amount to credit: ").pack()   
         amountentry = Text(top, font=("Arial"), width="50", height="1.2")
         amountentry.pack()
         Button(top,text='Submit to credit',command=lambda:credit_done(self,amountentry)).pack()
         def credit_done(self,amountentry):
             print("printing")
             amountentry1=amountentry.get("1.0","end-1c")
             self.data['bal']=int(self.data['bal'])
             self.data['bal']+=int(amountentry1)
             Label(top, text="Amount has been successfully credited " + str(amountentry1)).pack()  
             Label(top, text="Current balance is" + str(self.data['bal'])).pack()

       def debit(self):
         top1=Toplevel()
         Label(top1, text="Enter Amount to debit: ").pack()   
         damountentry = Text(top1, font=("Arial"), width="50", height="1.2")
         damountentry.pack()
         Button(top1,text='Submit to Debit',command=lambda:debit_done(self,damountentry)).pack()
         def debit_done(self,damountentry):
             print("printing")
             damountentry1=damountentry.get("1.0","end-1c")
             self.data['bal']=int(self.data['bal'])
             if int(damountentry1)>int(self.data['bal']):
                Label(top1, text="Amount cannot be debited due to insufficient Balance.").pack()
                return 0
             self.data['bal']-=int(damountentry1)
             Label(top1, text="Amount has been successfully debited " + str(damountentry1)).pack()  
             Label(top1, text="Current balance is" + str(self.data['bal'])).pack()

       def checkbal(self):
         top2=Toplevel()
         top2.geometry("140x70")
         Label(top2, text="Current balance is: " + str(self.data['bal'])).pack()   

        
              
def login(temp_acc_noentry,temp_psswd):
        print(temp_acc_noentry,temp_psswd)
        if int(temp_acc_noentry) in bank.acc.keys():
              Label(root, text="Account exists.\n ").pack()
        else:
              Label(root, text="Account not exist").pack()
        
        temp_acc_noentry=int(temp_acc_noentry)
        if temp_psswd==bank.acc[temp_acc_noentry]:
              Label(root, text="Access Granted ").pack()
        else:
              Label(root, text="Access Denied ").pack()
              return 0
        num=temp_acc_noentry%1000    
        global b
        print("\n Data is--->")
        print(b[num].data)
        Label(root, text=b[num].data ,font=("Algerian",20),bg="red",fg="white").pack()
        Button(root,text='Click for more features',command=lambda:b[num].edit()).pack()
        

mainloop()
=======
import os
import time
def cls():
   os.system('cls')
b=[0]
i=1
def create(nameentry,passwdentry,initbalentry):
  nameentry1=nameentry.get("1.0","end-1c")
  passwdentry1=passwdentry.get("1.0","end-1c")
  initbalentry1=initbalentry.get("1.0","end-1c")
  global b
  global i
  b.append(bank(nameentry1,passwdentry1,initbalentry1))
  i+=1
  Label(root, text="account has been created: "+ str(bank.count),font=("Algerian",20),bg="red",fg="white").pack()


from tkinter import *
from tkinter.messagebox import *
root=Tk()
root.geometry("999x999")
root.title("Bank Application")
Label(root, text= "Welcome to Bank " ,font="lucida 19 bold").pack()
Button(root,text='LOGIN',command=lambda:Entryfunc_login()).pack()
Button(root,text='sign-up',command=lambda:Entryfunc_create()).pack()
Button(root,text='Exit',command=root.destroy).pack()
def Entryfunc_create():
 Label(root, text="Enter account Holder's Name: ").pack()   
 nameentry = Text(root, font=("Arial"), width="50", height="1.2")
 nameentry.pack()
 Label(root, text="Set new Password: ").pack() 
 passwdentry = Text(root,font=("Arial"), width="50", height="1.2")
 passwdentry.pack()
 Label(root, text="Enter the Initial Balance to be credited: ").pack() 
 initbalentry = Text(root,font=("Arial"), width="50", height="1.2")
 initbalentry.pack()
 Button(root,text='Submit',command=lambda:create(nameentry,passwdentry,initbalentry)).pack()
 
  

def Entryfunc_login():
 acc_no=IntVar()
 passwd_login=StringVar()
 Label(root, text="Enter account no: ").pack()
 acc_noentry=Text(root, font=("Arial"), width="50", height="1.2")
 acc_noentry.pack()
 Label(root, text="Enter password: ").pack()
 passwd_entry= Text(root, font=("Arial"), width="50", height="1.2")
 passwd_entry.pack()
 Button(root,text='Submit',command=lambda:login_tk(acc_noentry,passwd_entry)).pack()




def login_tk(acc_noentry,passwd_entry):
   acc_noentry1=acc_noentry.get("1.0","end-1c")
   passwd_entry1=passwd_entry.get("1.0","end-1c")
   login(acc_noentry1,passwd_entry1)
    
    


class bank:
    count=1000
    acc=dict()
    def __init__(self,name_get,passwd_get,bal_get):
        bank.count+=1
        self.data=dict()
        self.data.update(name=name_get,password=passwd_get,
                         bal=bal_get,acc_no=bank.count)
        bank.acc.update([(self.data['acc_no'] , self.data['password'])])
        msg=f"Your generated Account Number is : {self.data['acc_no']}"
        
        #input("...Press Enter key...".center(60))
              
    def edit(self):
       Button(root,text='Credit',command=lambda:credit(self)).pack()
       Button(root,text='Debit',command=lambda:debit(self)).pack()
       Button(root,text='Check Balance',command=lambda:checkbal(self)).pack()

       def credit(self):
         top=Toplevel()
         Label(top, text="Enter Amount to credit: ").pack()   
         amountentry = Text(top, font=("Arial"), width="50", height="1.2")
         amountentry.pack()
         Button(top,text='Submit to credit',command=lambda:credit_done(self,amountentry)).pack()
         def credit_done(self,amountentry):
             print("printing")
             amountentry1=amountentry.get("1.0","end-1c")
             self.data['bal']=int(self.data['bal'])
             self.data['bal']+=int(amountentry1)
             Label(top, text="Amount has been successfully credited " + str(amountentry1)).pack()  
             Label(top, text="Current balance is" + str(self.data['bal'])).pack()

       def debit(self):
         top1=Toplevel()
         Label(top1, text="Enter Amount to debit: ").pack()   
         damountentry = Text(top1, font=("Arial"), width="50", height="1.2")
         damountentry.pack()
         Button(top1,text='Submit to Debit',command=lambda:debit_done(self,damountentry)).pack()
         def debit_done(self,damountentry):
             print("printing")
             damountentry1=damountentry.get("1.0","end-1c")
             self.data['bal']=int(self.data['bal'])
             if int(damountentry1)>int(self.data['bal']):
                Label(top1, text="Amount cannot be debited due to insufficient Balance.").pack()
                return 0
             self.data['bal']-=int(damountentry1)
             Label(top1, text="Amount has been successfully debited " + str(damountentry1)).pack()  
             Label(top1, text="Current balance is" + str(self.data['bal'])).pack()

       def checkbal(self):
         top2=Toplevel()
         top2.geometry("140x70")
         Label(top2, text="Current balance is: " + str(self.data['bal'])).pack()   

        
              
def login(temp_acc_noentry,temp_psswd):
        print(temp_acc_noentry,temp_psswd)
        if int(temp_acc_noentry) in bank.acc.keys():
              Label(root, text="Account exists.\n ").pack()
        else:
              Label(root, text="Account not exist").pack()
        
        temp_acc_noentry=int(temp_acc_noentry)
        if temp_psswd==bank.acc[temp_acc_noentry]:
              Label(root, text="Access Granted ").pack()
        else:
              Label(root, text="Access Denied ").pack()
              return 0
        num=temp_acc_noentry%1000    
        global b
        print("\n Data is--->")
        print(b[num].data)
        Label(root, text=b[num].data ,font=("Algerian",20),bg="red",fg="white").pack()
        Button(root,text='Click for more features',command=lambda:b[num].edit()).pack()
        

mainloop()
>>>>>>> ffa54a7009b3986a920100cbf48d0af75002874e
