import mysql.connector
from fastapi import FastAPI

app=FastAPI()

@app.get("/getdata")
def dummy1(skip:int=0,limit:int=10):
    mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="CPE")
    mycursor=mydb.cursor(dictionary=True)

    query="select * from data limit %s %s"
    mycursor.execute(query,(limit,skip))
    data=mycursor.fetchall()
    return data