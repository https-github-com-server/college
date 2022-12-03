from db import db


from flask import Flask,render_template,jsonify,request,flash,redirect,url_for

cur =db.cursor()
def in_CSE(ph,
        Email ,
        Name ,
        ETC,
        ESC):
        
        cur =db.cursor()
                       
        cur.execute("INSERT INTO  detail ( phone,email,name,subject1,subject2,subject3,subject4,subject5,subject6,ESC,ETC) VALUES (%s,%s, %s, %s,%s,%s,%s,%s,%s,%s,%s)", (ph,Email,Name,"Mathematics for CSE","Physics for CSE Stream",
                        "Principles of Programming Using C",
                        "Communicative English",
                        "Samskrutika Kannada/Balake Kannada",
                        "Engineering Exploration",ETC,ESC))
        db.commit()
        return "True"



man_cse=[{"name":"Mathematics for CSE" },{"name":"Physics for CSE Stream"},{"name":"Principles of Programming Using C"},{"name":"Communicative English-I "},{"name":"Samskrutika Kannada/ Balake Kannada"},{"name":"Engineering Exploration "}]

