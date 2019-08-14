<<<<<<< HEAD
from tkinter import *
from tkinter.messagebox import *
main = Tk()
main.geometry("999x999")
main.title("Smart Calculator-By NIK")
Label(main, text="Enter any Ques:").grid(row=0)
numq = Text(main, font=("Arial"),bg="red",fg="black", width="60", height="10")
numq.grid(row=0,column=1)
def storeques():
 que=numq.get("1.0","end-1c")
 print("printing que")
 print(que)
 global ques
 ques = que.split(" ")
 print(ques)
 return ques



def intfinder1(mylist):
    resultlist = []
    for x in mylist:
        try:
            i = int(x)
            resultlist.append(i)
            index = mylist.index(i)
            mylist = mylist.pop(index)

        except ValueError:
            continue

    return resultlist


def intfinder2(mylist):
    for y in mylist:
        try:
            j = int(y)
        except ValueError:
            continue
    return j

def show_answer(ans):
    num3.insert(0, ans)
def cal(ques):
    print("entred in function")
    print(ques)
    if ('exit' in ques):
        main.destroy()
    if ('sum' in ques or 'plus' in ques or 'add' in ques or 'addition' in ques or '+' in ques):
        sum1 = intfinder1(ques)
        ans=sum(sum1)
        print(ans)
        show_answer(ans)
    elif ('sub' in ques or 'minus' in ques or 'subtraction' in ques or 'difference' in ques or '-' in ques):
        a = intfinder1(ques)
        s = 0
        s = a[0] - a[1]
        for i in range(2, len(a)):
            s = s - a[i]

        ans=s
        show_answer(ans)

    elif ('multiply' in ques or 'product' in ques or 'mult' in ques or 'multiplication' in ques or '*' in ques):

        a = intfinder1(ques)
        s = 1
        for i in range(len(a)):
            s = s * a[i]
        ans=s
        show_answer(ans)

    elif ('divide' in ques or 'division' in ques or '/' in ques):
        a = intfinder1(ques)
        b = intfinder2(ques)
        ans=a/b
        show_answer(ans)

    elif ('underoot' in ques or 'squareroot' in ques or 'root' in ques):
        a = intfinder1(ques)
        ans=(a ** (1 / 2))
        show_answer(ans)
    elif 'square' in ques:
        a = intfinder1(ques)
        ans=(a ** 2)
        show_answer(ans)
    elif 'cube' in ques:
        a = intfinder1(ques)
        ans=(a ** 3)
        show_answer(ans)
    elif ('power' in ques or '^' in ques):
        a = intfinder1(ques)
        b = intfinder2(ques)
        ans=(a ** b)
        show_answer(ans)
    else:
        ans="wrong input"
Label(main, text="Result:",font=("Algerian",25),bg="red",fg="white").grid(row=2)
num3 = Entry(main, width="60")
num3.grid(row=2,column=1,sticky=W,pady=7)
def chng(e):
    b3.configure(bg="black")
def chng2(e):
    b3.configure(bg="light grey")
Button(main,text='Quit',command=main.destroy).grid(row=6,column=1,sticky=W,pady=7)
Button(main,text='Show',command=lambda: cal(ques),bg="light grey").grid(row=5,column=1,sticky=W,pady=4)
b3=Button(main,text='Confirm',command=storeques,bg="light grey")
b3.bind("<Enter>",chng)
b3.bind("<Leave>",chng2)
b3.grid(row=4,column=1,sticky=W,pady=5)
mainloop()
=======
from tkinter import *
from tkinter.messagebox import *
main = Tk()
main.geometry("999x999")
main.title("Smart Calculator-By NIK")
Label(main, text="Enter any Ques:").grid(row=0)
numq = Text(main, font=("Arial"),bg="red",fg="black", width="60", height="10")
numq.grid(row=0,column=1)
def storeques():
 que=numq.get("1.0","end-1c")
 print("printing que")
 print(que)
 global ques
 ques = que.split(" ")
 print(ques)
 return ques



def intfinder1(mylist):
    resultlist = []
    for x in mylist:
        try:
            i = int(x)
            resultlist.append(i)
            index = mylist.index(i)
            mylist = mylist.pop(index)

        except ValueError:
            continue

    return resultlist


def intfinder2(mylist):
    for y in mylist:
        try:
            j = int(y)
        except ValueError:
            continue
    return j

def show_answer(ans):
    num3.insert(0, ans)
def cal(ques):
    print("entred in function")
    print(ques)
    if ('exit' in ques):
        main.destroy()
    if ('sum' in ques or 'plus' in ques or 'add' in ques or 'addition' in ques or '+' in ques):
        sum1 = intfinder1(ques)
        ans=sum(sum1)
        print(ans)
        show_answer(ans)
    elif ('sub' in ques or 'minus' in ques or 'subtraction' in ques or 'difference' in ques or '-' in ques):
        a = intfinder1(ques)
        s = 0
        s = a[0] - a[1]
        for i in range(2, len(a)):
            s = s - a[i]

        ans=s
        show_answer(ans)

    elif ('multiply' in ques or 'product' in ques or 'mult' in ques or 'multiplication' in ques or '*' in ques):

        a = intfinder1(ques)
        s = 1
        for i in range(len(a)):
            s = s * a[i]
        ans=s
        show_answer(ans)

    elif ('divide' in ques or 'division' in ques or '/' in ques):
        a = intfinder1(ques)
        b = intfinder2(ques)
        ans=a/b
        show_answer(ans)

    elif ('underoot' in ques or 'squareroot' in ques or 'root' in ques):
        a = intfinder1(ques)
        ans=(a ** (1 / 2))
        show_answer(ans)
    elif 'square' in ques:
        a = intfinder1(ques)
        ans=(a ** 2)
        show_answer(ans)
    elif 'cube' in ques:
        a = intfinder1(ques)
        ans=(a ** 3)
        show_answer(ans)
    elif ('power' in ques or '^' in ques):
        a = intfinder1(ques)
        b = intfinder2(ques)
        ans=(a ** b)
        show_answer(ans)
    else:
        ans="wrong input"
Label(main, text="Result:",font=("Algerian",25),bg="red",fg="white").grid(row=2)
num3 = Entry(main, width="60")
num3.grid(row=2,column=1,sticky=W,pady=7)
def chng(e):
    b3.configure(bg="black")
def chng2(e):
    b3.configure(bg="light grey")
Button(main,text='Quit',command=main.destroy).grid(row=6,column=1,sticky=W,pady=7)
Button(main,text='Show',command=lambda: cal(ques),bg="light grey").grid(row=5,column=1,sticky=W,pady=4)
b3=Button(main,text='Confirm',command=storeques,bg="light grey")
b3.bind("<Enter>",chng)
b3.bind("<Leave>",chng2)
b3.grid(row=4,column=1,sticky=W,pady=5)
mainloop()
>>>>>>> ffa54a7009b3986a920100cbf48d0af75002874e
