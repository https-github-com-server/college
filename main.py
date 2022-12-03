import pymysql
from flask import Flask,render_template,jsonify,request,flash,redirect,url_for
from Data import *
from civil import in_civil,man_civil
from db import db
from mech import in_mech,man_mech
from eee import in_EEE,man_eee
from ece import in_ECE,man_ece
from cse import in_CSE,man_cse

courssssse=""

emtc=["Green Buildings",
"Introduction to Nano Technology",
"Renewable Energy Sources",
"Introduction to Internet of Things (IOT)",
"Introduction to Cyber Security"]



engscour=["Introduction to Civil Engineering" ,
 "Introduction to Electrical Engineering",
  "Introduction to Electronics Engineering",
  "Introduction to Mechanical Engineering"
  "Introduction to C Programming"
]



progcour=[  "Introduction to Web Programming" ,
 "Introduction to Python Programming ",
 "Basics of JAVA programming  ",
 "Introduction to C++ Programming"
]


save={}









course_data=[{"name":"CSE/AIML/ISE"},{"name":"CIVIL"},{"name":"MECH"},{"name":"EEE"},{"name":"ECE"}]

app=Flask(__name__)
app.secret_key = "super secret key"
#set up Cursor

cursor = db.cursor()

db.autocommit( 1 )
#cursor = db.cursor( pymysql.cursors.DictCursor )




@app.route('/')
@app.route('/index')
def home():
    
    for data in progcour:
        cursor.execute(("select  count(ESC) from detail where ESC=%s"),(str(data)) )
        c=cursor.fetchall()
    
        save[data]=60-c[0][0]


    for data in emtc:
        cursor.execute(("select  count(ESC) from detail where ESC=%s"),(str(data)) )
        c=cursor.fetchall()
    
        save[data]=60-c[0][0]



    for data in engscour:
        cursor.execute(("select  count(ESC) from detail where ESC=%s"),(str(data)) )
        c=cursor.fetchall()
    
        save[data]=60-c[0][0]

    return render_template("index.html",data=course_data,result=save)


@app.route('/insert', methods = ['GET','POST'])
def insert():

    if request.method == "POST":
       
        ph=request.form['Phone']
        Email = request.form['Email']
        Name = request.form['Name']
        ETC= request.form.get('Emerging Technology Courses')
        ESC=request.form.get('Emerging Science Courses')
        cur =db.cursor()
        cursor.execute(("select  count(ESC) from detail where ESC=%s"),(str(ETC)) )
        etcs=cursor.fetchall()
        cursor.execute(("select  count(ESC) from detail where ESC=%s"),(str(ESC)) )
        escs=cursor.fetchall()
        if etcs[0][0]>=60 or escs[0][0]>=60:
            flash("Fulll")
        cur.execute("SELECT * FROM 1ST_SEM_ISE where MOBILE={value}".format(value=ph))
        s=cur.fetchall()
        if s:
        
            if courssssse=="CSE/AIML/ISE":
                    ans=in_CSE(ph,Email ,Name , ETC,ESC)
                    flash("Data Inserted Successfully")
                    return redirect(url_for('home'))
            elif courssssse=="CIVIL":
                ans=in_civil(ph,Email ,Name , ETC,ESC)
                flash("Data Inserted Successfully")
                return redirect(url_for('home'))
            elif courssssse=="MECH":
                ans=in_mech(ph,Email ,Name , ETC,ESC)
                flash("Data Inserted Successfully")
                return redirect(url_for('home'))
            elif courssssse=="EEE":
                ans=in_EEE(ph,Email ,Name , ETC,ESC)
                flash("Data Inserted Successfully")
                return redirect(url_for('home'))
            elif courssssse=="ECE":
                ans=in_ECE(ph,Email ,Name , ETC,ESC)
                flash("Data Inserted Successfully")
                return redirect(url_for('home'))
        else:
            flash("Please enter vaid mobile number registered with college")
            return redirect(url_for('home'))


@app.route('/course', methods = ['POST'])
def course():
    if request.method=='POST':
        global courssssse
        courssssse= request.form.get('comp_select')
       

        if courssssse=="CSE/AIML/ISE":
            return render_template("index.html",man=man_cse,head="Engineering Science Courses",data=cs_open,EmergingTechnologyCourses=cs_pro,course=course,data_course=cs_pro,data_course_science=cs_open)

        if courssssse=='CIVIL':
            return render_template("index.html",man=man_civil,head="Programming Language Courses-I",data=civil_open,EmergingTechnologyCourses=civil_pro,course=course,data_course=civil_pro,data_course_science=civil_open)

        
        if courssssse=='EEE':
            return render_template("index.html",data=eee_open,man=man_eee,head="Programming Language Courses-I",EmergingTechnologyCourses=eee_pro,course=course,data_course=eee_pro,data_course_science=eee_open)

    
        if courssssse=='MECH':
            return render_template("index.html",man=man_mech,data=mech_open,head="Programming Language Courses-I",EmergingTechnologyCourses=mech_pro,course=course,data_course=mech_pro,data_course_science=mech_open)

        if courssssse=='ECE':
            return render_template("index.html",man=man_ece,head="Engineering Science Courses",data=ece_open,EmergingTechnologyCourses=ece_pro,course=course,data_course=ece_pro,data_course_science=ece_open)







if __name__=="__main__":
    app.run(debug=True)