from db import db


cur=db.cursor()
def count(et,esc):
    cur.execute(("select  count(ESC) from detail where ESC=%s"),(str(et)) )
    etcs=cur.fetchall()
    cur.execute(("select  count(ESC) from detail where ESC=%s"),(str(esc)) )
    escs=cur.fetchall()


    return etcs[0][0],escs[0][0]


a,b=count("Green Buildings","Introduction to Electrical Engineering")


print(a,b)