<<<<<<< HEAD
#import numpy as np
print("Welcome to Smart Calculator ")
que=input("Enter the Ques")
ques=que.split(" ")

def intfinder1(mylist):  
    resultlist=[]
    for x in mylist:
        try:        
            i=int(x)
            resultlist.append(i)
            index=mylist.index(i)
            mylist=mylist.pop(index)
          
        except ValueError:
            continue
     
    return resultlist   
def intfinder2(mylist):
    for y in mylist:
        try:        
            j=int(y)
        except ValueError:
            continue
    return j
while(1)   :     
 if ('exit' in ques):
     exit(1)
 if ('sum' in ques or 'plus' in ques or 'add' in ques or 'addition' in ques or '+' in ques):    
   sum1=intfinder1(ques)
   print(sum(sum1))
 elif ('sub' in ques or 'minus' in ques or 'subtraction' in ques or 'difference' in ques or '-' in ques):    
    a=intfinder1(ques)
    s=0
    s=a[0]-a[1]
    for i in range(2,len(a)):
      s=s-a[i]
    
    print(s)
    
 elif ('multiply' in ques or 'product' in ques or 'mult' in ques or 'multiplication' in ques or '*' in ques):

    a=intfinder1(ques)
    s=1
    for i in range(len(a)):
      s=s*a[i]
    print(s)

 elif ('divide' in ques or 'division' in ques or '/' in ques ):
    a=intfinder1(ques)
    b=intfinder2(ques)
    print(a/b)

 elif ('underoot' in ques or 'squareroot' in ques or 'root' in ques):
    a=intfinder1(ques)
    print(a**(1/2))
 elif 'square' in ques:
    a=intfinder1(ques)
    print(a**2)
 elif 'cube' in ques:
    a=intfinder1(ques)
    print(a**3)
 elif ('power' in ques or '^' in ques):
    a=intfinder1(ques)
    b=intfinder2(ques)
    print(a**b)
 else:
    print("wrong input")
 que=input("Enter the Ques")
 ques=que.split(" ")











=======
#import numpy as np
print("Welcome to Smart Calculator ")
que=input("Enter the Ques")
ques=que.split(" ")

def intfinder1(mylist):  
    resultlist=[]
    for x in mylist:
        try:        
            i=int(x)
            resultlist.append(i)
            index=mylist.index(i)
            mylist=mylist.pop(index)
          
        except ValueError:
            continue
     
    return resultlist   
def intfinder2(mylist):
    for y in mylist:
        try:        
            j=int(y)
        except ValueError:
            continue
    return j
while(1)   :     
 if ('exit' in ques):
     exit(1)
 if ('sum' in ques or 'plus' in ques or 'add' in ques or 'addition' in ques or '+' in ques):    
   sum1=intfinder1(ques)
   print(sum(sum1))
 elif ('sub' in ques or 'minus' in ques or 'subtraction' in ques or 'difference' in ques or '-' in ques):    
    a=intfinder1(ques)
    s=0
    s=a[0]-a[1]
    for i in range(2,len(a)):
      s=s-a[i]
    
    print(s)
    
 elif ('multiply' in ques or 'product' in ques or 'mult' in ques or 'multiplication' in ques or '*' in ques):

    a=intfinder1(ques)
    s=1
    for i in range(len(a)):
      s=s*a[i]
    print(s)

 elif ('divide' in ques or 'division' in ques or '/' in ques ):
    a=intfinder1(ques)
    b=intfinder2(ques)
    print(a/b)

 elif ('underoot' in ques or 'squareroot' in ques or 'root' in ques):
    a=intfinder1(ques)
    print(a**(1/2))
 elif 'square' in ques:
    a=intfinder1(ques)
    print(a**2)
 elif 'cube' in ques:
    a=intfinder1(ques)
    print(a**3)
 elif ('power' in ques or '^' in ques):
    a=intfinder1(ques)
    b=intfinder2(ques)
    print(a**b)
 else:
    print("wrong input")
 que=input("Enter the Ques")
 ques=que.split(" ")











>>>>>>> ffa54a7009b3986a920100cbf48d0af75002874e
