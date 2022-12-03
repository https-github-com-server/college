import pymysql
from flask import Flask,render_template,jsonify,request,flash,redirect,url_for
from Data import *
from civil import in_civil,man_civil
from db import db
from mech import in_mech,man_mech
from eee import in_EEE,man_eee
from ece import in_ECE,man_ece
from cse import in_CSE,man_cse
from get_count import count

courssssse=""

emtc=["Green Buildings",
"Introduction to Nano Technology",
"Renewable Energy Sources",
"Introduction to Internet of Things (IOT)",
"Introduction to Cyber Security"]



engscour=["Introduction to Civil Engineering" ,
 "Introduction to Electrical Engineering",
  "Introduction to Electronics Engineering",
  "Introduction to Mechanical Engineering",
  "Introduction to C Programming"
]



progcour=[  "Introduction to Web Programming" ,
 "Introduction to Python Programming ",
 "Basics of JAVA programming  ",
 "Introduction to C++ Programming"
]




save={}


course_data=[{"name":"CSE"},{"name":"AIML"},{"name":"ISE"},{"name":"MECH"},{"name":"EEE"},{"name":"ECE"},{"name":"CIVIL"}]

app=Flask(__name__)
app.secret_key = "super secret key"
#set up Cursor


cursor = db.cursor()

db.autocommit( 1 )
cursor = db.cursor( pymysql.cursors.DictCursor )

cur=db.cursor()



@app.route('/')
@app.route('/index')
def home():
    
    for data in progcour:
        cur.execute(("select  count(ESC) from detail where ETC=%s"),(str(data)) )
        c=cur.fetchall()
    
        save[data]=[c[0][0],120]
       


    for data in emtc:
        cur.execute(("select  count(ESC) from detail where ESC=%s"),(str(data)) )
        c=cur.fetchall()
        if data=="Introduction to Nano Technology":
            save[data]=[c[0][0],180]
            
        elif data=="Renewable Energy Sources":
            save[data]=[c[0][0],120]
           
        else:
            save[data]=[c[0][0],60]
           



    for data in engscour:
        cur.execute(("select  count(ESC) from detail where ESC=%s"),(str(data)) )
        c=cur.fetchall()
    
        save[data]=[c[0][0],"No limit"]
        

    return render_template("index.html",data=course_data,result=save)

@app.route("/about.html")
def about():
    return render_template("about.html")







@app.route('/insert', methods = ['GET','POST'])
def insert():

    if request.method == "POST":
        
            ph=request.form['Phone']
          
            Name = request.form['Name']
            ETC= request.form.get('Emerging Technology Courses')
            ESC=request.form.get('Emerging Science Courses')
            cur =db.cursor()
      
            if 0==0:
                a,b=count(ETC,ESC)
                if ETC=="Introduction to Nano Technology" and a==180:
                    flash("The number of seats are full")
                    return redirect(url_for('home'))
                elif ETC=="Renewable Energy Sources" and a==120:
                    flash("The number of seats are full")
                    return redirect(url_for('home'))
                elif a==60 and b in progcour and b==60:
                    flash("The number of seats are full")
                    return redirect(url_for('home'))

                else:
                    
                        if courssssse=="CSE":
                                    ans=in_CSE(ph,Name , ETC,ESC,courssssse)
                                    flash("Data Inserted Successfully")
                                    return redirect(url_for('home'))
                        if courssssse=="AIML":
                                    ans=in_CSE(ph ,Name , ETC,ESC,courssssse)
                                    flash("Data Inserted Successfully")
                                    return redirect(url_for('home'))
                        if courssssse=="ISE":
                                    ans=in_CSE(ph ,Name , ETC,ESC,courssssse)
                                    flash("Data Inserted Successfully")
                                    return redirect(url_for('home'))
                        elif courssssse=="CIVIL":
                                ans=in_civil(ph ,Name , ETC,ESC)
                                flash("Data Inserted Successfully")
                                return redirect(url_for('home'))
                        elif courssssse=="MECH":
                                ans=in_mech(ph ,Name , ETC,ESC)
                                flash("Data Inserted Successfully")
                                return redirect(url_for('home'))
                        elif courssssse=="EEE":
                                ans=in_EEE(ph ,Name , ETC,ESC)
                                flash("Data Inserted Successfully")
                                return redirect(url_for('home'))
                        elif courssssse=="ECE":
                                ans=in_ECE(ph ,Name , ETC,ESC)
                                flash("Data Inserted Successfully")
                                return redirect(url_for('home'))
                    
            else:
                flash("Please enter valid number/email registered with college")
                return redirect(url_for('home'))
        



@app.route('/course', methods = ['POST'])
def course():
    if request.method=='POST':
        global courssssse
        courssssse= request.form.get('comp_select')
       

        if courssssse=="CSE":
            return render_template("index.html",man=man_cse,head="Engineering Science Courses",main="Emerging Technology Courses",data=cs_open,EmergingTechnologyCourses=cs_pro,course=course,data_course=cs_pro,data_course_science=cs_open,c_image=True)
        
        if courssssse=="AIML":
            return render_template("index.html",man=man_cse,head="Engineering Science Courses",main="Emerging Technology Courses",data=cs_open,EmergingTechnologyCourses=cs_pro,course=course,data_course=cs_pro,data_course_science=cs_open,c_image=True)
        
        if courssssse=="ISE":
            return render_template("index.html",man=man_cse,head="Engineering Science Courses",main="Emerging Technology Courses",data=cs_open,EmergingTechnologyCourses=cs_pro,course=course,data_course=cs_pro,data_course_science=cs_open,c_image=True)
        if courssssse=='CIVIL':
            return render_template("index.html",man=man_civil,head="Programming Language Courses-I",main="Engineering Science Courses",data=civil_open,EmergingTechnologyCourses=civil_pro,course=course,data_course=civil_pro,data_course_science=civil_open,civil_image=True)

        
        if courssssse=='EEE':
            return render_template("index.html",data=eee_open,man=man_eee,head="Programming Language Courses-I",main="Engineering Science Courses",EmergingTechnologyCourses=eee_pro,course=course,data_course=eee_pro,data_course_science=eee_open,eee_img=True)

    
        if courssssse=='MECH':
            return render_template("index.html",man=man_mech,data=mech_open,head="Programming Language Courses-I",main="Engineering Science Courses",EmergingTechnologyCourses=mech_pro,course=course,data_course=mech_pro,data_course_science=mech_open,mec_img=True)

        if courssssse=='ECE':
            return render_template("index.html",man=man_ece,head="Engineering Science Courses",data=ece_open,main="Engineering Science Courses",EmergingTechnologyCourses=ece_pro,course=course,data_course=ece_pro,data_course_science=ece_open,ece_img=True)
        else:
            flash("select a course")
            return redirect(url_for('home'))






if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)