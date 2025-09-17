from flask import Flask, jsonify
import pymysql as mysql
import json
app=Flask(__name__)
db=mysql.connect(host="localhost",user="root",password="root@123",database="flask")
cursor=db.cursor()

@app.route("/")
def load_data():
    with open("users.json") as file:
        users=json.load(file)
    # insert into mySQL
    for user in users:
        sql="INSERT INTO STUDENTS (S_NAME,S_EMAIL,S_MOB) VALUES(%s,%s,%s)"
        values=(user['name'],user['email'],user['mob'])
        cursor.execute(sql,values)
    db.commit()
    return "Data addedd successfully ✅"

@app.route("/get")
def fetch_data():
    sql="SELECT * FROM STUDENTS"
    cursor.execute(sql)
    new_data=[]
    for data in cursor.fetchall():
        new_data.append(data)
    return new_data

app.run()
