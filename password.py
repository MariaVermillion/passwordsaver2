import random
import sqlite3
import string

conn=sqlite3.connect('saver1.db')
create_table = "'''CREATE TABLE IF NOT EXISTS usertable (id INTEGER PRIMARY KEY, user text,Password text)'''"
print(create_table)
db = conn.cursor()
results = db.execute('''CREATE TABLE IF NOT EXISTS usertable (id INTEGER PRIMARY KEY, user text,Password text)''')
name=""
password=""
count=0
db.execute(name,password)

closes="No" and "no"
def gen():
    gen="abcdefghijklmnopqrstuvwxyzQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*()"
    passlen = 16
    genp= "".join(random.sample(gen,passlen))
    print ("Your password: "+genp)
    return genp
while (closes=="No" or closes=="no"):
    namen=("")
    Passwordn=("")
    usi=input("Password Saver. Saved Passwords(1), generate password(2), or Enter password(3).")
    if (usi=="1"):
        db.execute('SELECT * FROM usertable WHERE user != ""')
        print ("\n>>>>>>>>>>>>>>>>>>|>>>>>>>>>>>>>>>>")
        print ("      Website     |    Password    ")
        print (">>>>>>>>>>>>>>>>>>|>>>>>>>>>>>>>>>>")
        for row in db:
            l=len(row[1])
            l=18-l
            sp=""
            for x in range(1,l):
                sp+=" "
            print (row[1]+sp+" | " + row[2])            
        print (">>>>>>>>>>>>>>>>>>|>>>>>>>>>>>>>>>>\n")    
    if(usi=="2"):
        namen=input("Website Name: ")
        Passwordn=gen()
        db.execute("insert into usertable (user ,Password) values (?,?)",list(( namen ,Passwordn),))
        conn.commit()
        
    if (usi=="3"):
        namen=input("Enter name of web site: ")
        Passwordn=input("Enter password: ")
        db.execute("insert into usertable (user ,Password) values (?,?)",list(( namen ,Passwordn),))
        conn.commit()
    closes=input("Close program.Yes or No: ")
db.close()
conn.close()

