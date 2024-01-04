import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Apple_123$",
    
)
cur=mydb.cursor()
cur.execute("Show databases")
res=cur.fetchall()
for i in res :
    print(i) 
