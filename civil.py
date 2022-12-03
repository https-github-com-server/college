from db import db


from flask import Flask,render_template,jsonify,request,flash,redirect,url_for

cur =db.cursor()
def in_civil(ph,
      
        Name ,
        ETC,
        ESC):
    cur.execute("INSERT INTO  detail ( phone,name,subject1,subject2,subject3,subject4,subject5,subject6,ESC,ETC,Dept) VALUES (%s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s)", (ph,Name,"Mathematics for Civil Engg","Chemistry for Civil Engg Stream",
                        "Computer-Aided Engineering Drawing",
                        "Communicative English-I",
                        "Indian Constitution",
                        "Social Innovation",ETC,ESC,"CIVIL"))
    db.commit()
    
    return "True"

man_civil=[{"name":"22MATC11 - Mathematics for Civil Engg Stream"},{"name":"22CHEC12 - Chemistry for Civil Engg Stream"},{"name":"22CED13 - Computer-Aided Engineering Drawing"},{"name":"22CE16 - Communicative English-I "},{"name":"22IC17 - Indian Constitution"},{"name":"22SI18 - Social Innovation"}]









