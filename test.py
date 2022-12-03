from db import db

cur=db.cursor()
dict={}

cur.execute(("select  count(ESC) from detail where ESC=%s"),("Green Buildings") )
count=cur.fetchall()

type(count)
dict["0"]=count[0][0]

print(dict["0"])