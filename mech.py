from db import db


from flask import Flask,render_template,jsonify,request,flash,redirect,url_for

cur =db.cursor()
def in_mech(ph,
       
        Name ,
        ETC,
        ESC):
    cur.execute("INSERT INTO  detail ( phone,name,subject1,subject2,subject3,subject4,subject5,subject6,ESC,ETC,dept) VALUES (%s,%s, %s, %s,%s,%s,%s,%s,%s,%s,%s)", (ph,Name,"Mathematics for MES-I","Chemistry for MES",
                        "Computer-Aided Engineering Drawing",
                        "Communicative English-I",
                        "Indian Constitution",
                        "Social Innovation",ETC,ESC,"MECH"))
    db.commit()
    
    return "True"

man_mech=[{"name":"22MATM11 - Mathematics for MES-I"},{"name":"22CHEM12 - Chemistry for MES"},{"name":"22CED13 - Computer-Aided Engineering Drawing"},{"name":"22CE16 - Communicative English-I "},{"name":"22IC17 - Indian Constitution"},{"name":"22SI18 - Social Innovation"}]
