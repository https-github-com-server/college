from db import db


from flask import Flask,render_template,jsonify,request,flash,redirect,url_for

cur =db.cursor()
def in_ECE(ph,
        
        Name ,
        ETC,
        ESC):
    cur.execute("INSERT INTO  detail ( phone,name,subject1,subject2,subject3,subject4,subject5,subject6,ESC,ETC,dept) VALUES (%s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s)", (ph,Name,"Mathematics for EEE Stream-I","Physics for EEE Stream",
                        "Basic Electronics",
                        "Communicative English-I",
                        "Samskrutika Kannada/ Balake Kannada",
                        "Engineering Exploration",ETC,ESC,"ECE"))
    db.commit()
    
    return "True"


man_ece=[{"name":"22MATE11 - Mathematics for EEE Stream-I"},{"name":"22CHEE12 - Chemistry for EES"},{"name":"22CED13 - Computer-Aided Engineering Drawing"},{"name":"22CE16 - Communicative English-I "},{"name":"22IC17 - Indian Constitution"},{"name":"22SI18 - Social Innovation"}]
