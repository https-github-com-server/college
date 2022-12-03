from db import db


from flask import Flask,render_template,jsonify,request,flash,redirect,url_for

cur =db.cursor()
def in_EEE(ph,
        Email ,
        Name ,
        ETC,
        ESC):
    cur.execute("INSERT INTO  detail ( phone,email,name,subject1,subject2,subject3,subject4,subject5,subject6,ESC,ETC) VALUES (%s,%s, %s, %s,%s,%s,%s,%s,%s,%s,%s)", (ph,Email,Name,"Mathematics for EES-I","Chemistry for EES",
                        "Computer-Aided Engineering Drawing",
                        "Communicative English-I",
                        "Indian Constitution",
                        "Social Innovation",ETC,ESC))
    db.commit()
    
    return "True"


man_eee=[{"name":"Mathematics for EES-I"},
{"name":"Chemistry for EES"},

{"name":"Computer-Aided Engineering Drawing"},

{"name": "Communicative English  I"},
{"name": "Indian Constitution"},
{"name":"Social Innovation"}]
