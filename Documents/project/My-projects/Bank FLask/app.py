from flask import Flask , render_template,request
import requests
import MySQLdb as sql
import random

#Database 
db=sql.connect(host="127.0.0.1",port=3306,user="root",password="",database="bank")
cur=db.cursor()
accessaccno=0000
OTP=0000
globalmessage=""
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signup.html/")
def signup():
     return render_template("signup.html")

@app.route("/login.html/",methods=["POST","GET"])
def login():
     return render_template("login.html")

@app.route("/signup1.html/",methods=['POST','GET'])
def signup1():
     message=""
     acc_no=1000
     fullname=request.form.get("fullname").capitalize()
     passd=request.form.get("passd")
     cpassd=request.form.get("cpassd")
     if passd==cpassd:
          pass
     else:
          message="Password doesnt matched"
          return render_template("signup.html",message=message)
     initialbal=request.form.get("initialbal")
     email=request.form.get("email")
     day=request.form.get("day")
     month=request.form.get("month")
     year=request.form.get("year")
     mobile=request.form.get("mobile")
     address=request.form.get("address")
     cmd="select count(*) from user_info"
     dob=day+"-"+month+"-"+year
     cur.execute(cmd)
     addition=cur.fetchall()
     addition1=addition[0][0]
     acc_no+=addition1
     cmd="insert into user_info(name,password,bal,acc_no,email,DOB,mob,address) values(%s,%s,%s,%s,%s,%s,%s,%s)"
     val=(fullname,passd,initialbal,acc_no,email,dob,mobile,address)      
     cur.execute(cmd,val)     
     db.commit()
     global globalmessage
     globalmessage = f"Account successfully created. Your Accout no : {acc_no}" 
     print("global message is: ",globalmessage)
     url = "https://www.fast2sms.com/dev/bulk"
     global OTP
     OTP=random.randrange(1111,9999)
     payload = f"sender_id=FSTSMS&message={OTP}&language=english&route=p&numbers=7988816585"
     headers = {
     'authorization': "FrfdjRCDYXlIMJktOxey0QTcZpL5gHq2Bm6GV39i7SKAsvz4awnxFIWMg4iUyr3OhEjPBbkJluvZHYAD",
     'Content-Type': "application/x-www-form-urlencoded"
     }
     response = requests.request("POST", url, data=payload, headers=headers)


     message=""
     return render_template("verify.html",message=message)
@app.route("/login1.html/",methods=['POST','GET'])
def login1():
   
     message=""
     if request.method == "POST":
       tempaccountno=request.form.get("tempaccountno")
       temppassd=request.form.get("temppass")
     cmd="select acc_no from user_info"

     cur.execute(cmd)
     data=cur.fetchall() 
     print("total accounts are:",data)
     
     print((int(tempaccountno),))  
     if (int(tempaccountno),) in data:
         pass
     else:
          print("account not found")
     print("pass is ",temppassd)    
     cmd="select password from user_info"
     cur.execute(cmd)
     datapass=cur.fetchall() 
     print(datapass)
     cmd = f"select password from user_info where acc_no=%s and password=%s"
     value=(tempaccountno,temppassd)      
     cur.execute(cmd,value)
     data=cur.fetchall()
     print("data is ",data)
     details=""
     if data:
        global accessaccno
        accessaccno=tempaccountno  
       
        return render_template("mypage.html",tempaccountno=tempaccountno,details=None)
     else:
          message="INVALID CREDENTIALS"
          return render_template("login.html",message=message)

@app.route("/profile.html/")    
def profile():
          
          cmd=f"select * from user_info where acc_no={accessaccno}" 
          
          cur.execute(cmd)
          data=cur.fetchall()
          
          return render_template("mypage.html",details=data)





@app.route("/mypage.html/",methods=['POST','GET'])
def mypage():
     return render_template("mypage.html")
  
@app.route("/banking.html/")
def banking():
     return render_template("banking.html")

@app.route("/credit.html/",methods=['GET','POST'])
def credit():
     message=""
     if request.method=='POST':
          tempcr=request.form.get("tempcr")
          cmd= f"update user_info set bal=bal+{tempcr} where acc_no={accessaccno}"  
          cur.execute(cmd)
          data=cur.fetchall()
          print(data)
          db.commit() 
          message="Amount has been Credited"   
     return render_template("credit.html",message=message)

@app.route("/debit.html/",methods=['POST','GET'])
def debit():
     message=""
     if request.method=='POST':
          tempdr=request.form.get("tempdr")
          cmd=f"select bal from user_info where acc_no={accessaccno}"
          cur.execute(cmd)
          data=cur.fetchall()
          if int(tempdr)< int(data[0][0]):
              cmd = "update user_info set bal=bal-%s where acc_no=%s"
              value=(tempdr,accessaccno)     
              cur.execute(cmd,value)
              message="Amount successfully debited"
          else:
             message="Insufficient Balance"
     db.commit()
     return render_template("debit.html",message=message)
@app.route("/verify.html/",methods=['POST','GET'])
def verify():
     if request.method=='POST':
          message=""
          tempOTP=request.form.get("tempOTP")
          global OTP
          print("ENtred OTP:",tempOTP)
          print("type of tempotp",type(tempOTP))
          
          print("REal OTP :",OTP)
          print("type of otp",type(OTP))
           
          if int(OTP)==int(tempOTP):
               message="Great! Mobile Number has been verified"
          else:
               message="Sorry! You have entered an invalid OTP."
               return render_template("verify.html",message=message)     
     print("global message is: ",globalmessage)
     return render_template("login.html",globalmessage=globalmessage,message=message)






app.run(host="localhost",port=5000,debug=True)    
