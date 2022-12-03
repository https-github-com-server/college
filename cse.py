from db import db


from flask import Flask,render_template,jsonify,request,flash,redirect,url_for

cur =db.cursor()
def in_CSE(ph,
        
        Name ,
        ETC,
        ESC,
        course):
        




        
        cur =db.cursor()
                       
        cur.execute("INSERT INTO  detail ( phone,name,subject1,subject2,subject3,subject4,subject5,subject6,ESC,ETC,Dept) VALUES (%s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s)", (ph,Name,"Mathematics for CSE","Physics for CSE Stream",
                        "Principles of Programming Using C",
                        "Communicative English",
                        "Samskrutika Kannada/Balake Kannada",
                        "Engineering Exploration",ETC,ESC,course))
        db.commit()
        return "True"



man_cse=[{"name":"22MATS11 - Mathematics for CSE" },{"name":"22PHYS12 - Physics for CSE Stream"},{"name":"22POP13 - Principles of Programming Using C"},{"name":"22CE16 - Communicative English - I "},{"name":"22KSK17 - Samskrutika Kannada/22KBK17 Balake Kannada"},{"name":"22EEX18 - Engineering Exploration "}]

