import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Apple_123$",
    database="pythonsql"
)
print(mydb.connection_id)
#Show DataBase Command:-
'''
cur=mydb.cursor()
cur.execute("SHOW DATABASES")
res=cur.fetchall()
for i in res:
    {
        print(i)
    }
    '''
#Create DataBase Command:-
'''cur.execute("CREATE DATABASE pythonsql")'''

#Create Table Command:-
'''float(5,2) =>It consists of 5 digits and 2 digits after point
cur.execute("CREATE TABLE analysis(bookid int,title varchar(20),price float(5,2))")'''

# Insert Table Command:-
'''  s="INSERT INTO analysis (bookid,title,price) VALUES(%s,%s,%s)"
b1=(1,"Wingsoffire",290)
b2=[(2,"Bhagavatgeeta",590),(1,"Python",250),(1,"Mswordbasics",220)]
cur.executemany(s,b2)
# mydb.commit()'''

# if mydb.is_connected():
#     print("Connection is Established ")

#Update & Display Command:-
'''s1="UPDATE analysis  SET price=price+10 WHERE price>250"
cur.execute(s1)
mydb.commit()
s="SELECT * FROM analysis"
cur.execute(s)
result=cur.fetchall()
for i in result:
    {
        print(i)
    }'''

#Delete Command:-
'''cur=mydb.cursor()
s="Delete from analysis where title='Mswordbasics'"
cur.execute(s)
mydb.commit()'''

#To print the no of characters in the title:-Wingsoffire
cur=mydb.cursor()
cur.execute("Select char_length(title) from analysis where title='Wingsoffire'")
res=cur.fetchall()
print(res)