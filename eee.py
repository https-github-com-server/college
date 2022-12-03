from db import db


from flask import Flask,render_template,jsonify,request,flash,redirect,url_for

cur =db.cursor()
def in_EEE(ph ,Name ,ETC,ESC):

    cur.execute("INSERT INTO  detail ( phone,name,subject1,subject2,subject3,subject4,subject5,subject6,ESC,ETC,dept) VALUES (%s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s)",( ph,Name,"Mathematics for EES-I","Chemistry for EES","Computer-Aided Engineering Drawing","Communicative English-I","Indian Constitution","Social Innovationc",ETC,ESC,"EEE"))
    db.commit()
    
    return "True"


man_eee=[{"name":"22MATE11 - Mathematics for EES-I"},
{"name":"22CHEE12 - Chemistry for EES"},{"name":"22CED13 - Computer-Aided Engineering Drawing"},
{"name": "22CE16 - Communicative English  I"},
{"name": "22IC17 - Indian Constitution"},
{"name":"22SI18 - Social Innovation"}]
