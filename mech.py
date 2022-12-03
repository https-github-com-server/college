from db import db


from flask import Flask,render_template,jsonify,request,flash,redirect,url_for

cur =db.cursor()
def in_mech(ph,
        Email ,
        Name ,
        ETC,
        ESC):
    cur.execute("INSERT INTO  detail ( phone,email,name,subject1,subject2,subject3,subject4,subject5,subject6,ESC,ETC) VALUES (%s,%s, %s, %s,%s,%s,%s,%s,%s,%s,%s)", (ph,Email,Name,"Mathematics for MES-I","Chemistry for MES",
                        "Computer-Aided Engineering Drawing",
                        "Communicative English-I",
                        "Indian Constitution",
                        "Social Innovation",ETC,ESC))
    db.commit()
    
    return "True"

man_mech=[{"name":"Mathematics for MES-I"},{"name":"Chemistry for MES"},{"name":"Computer-Aided Engineering Drawing"},{"name":"Communicative English-I "},{"name":"Indian Constitution"},{"name":"Social Innovation"}]
