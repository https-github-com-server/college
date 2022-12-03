from db import db


from flask import Flask,render_template,jsonify,request,flash,redirect,url_for

cur =db.cursor()
def in_ECE(ph,
        Email ,
        Name ,
        ETC,
        ESC):
    cur.execute("INSERT INTO  detail ( phone,email,name,subject1,subject2,subject3,subject4,subject5,subject6,ESC,ETC) VALUES (%s,%s, %s, %s,%s,%s,%s,%s,%s,%s,%s)", (ph,Email,Name,"Mathematics for EEE Stream-I","Physics for EEE Stream",
                        "Basic Electronics",
                        "Communicative English-I",
                        "Samskrutika Kannada/ Balake Kannada",
                        "Engineering Exploration ",ETC,ESC))
    db.commit()
    
    return "True"


man_ece=[{"name":"Mathematics for EEE Stream-I"},{"name":"Physics for EEE Stream"},{"name":"Basic Electronics"},{"name":"Communicative English-I "},{"name":"Samskrutika Kannada/ Balake Kannada"},{"name":"Engineering Exploration "}]
