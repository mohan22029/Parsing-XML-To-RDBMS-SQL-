import mysql.connector
import json
import xml.etree.ElementTree as ET

mydatabase=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="CPE"
)

operation=mydatabase.cursor()

# operation.execute("create database CPE")
# operation.execute("use CPE")
print("Connection established")


# operation.execute("create table data(cpe_title varchar(200),cpe_23_uri varchar(200),reference_links mediumtext,cpe_23_deprecation_date date)")
# print("Data base and table created successfull")


tree=ET.parse('official-cpe-dictionary_v2.3.xml')

root=tree.getroot()

# print(type(root[378][0].text))
# print(type(root[378][1][0].attrib["href"]))
# print(type(root[378][2].attrib["name"]))


# Going to push first 5 Lakh Data into the MySQL DataBase
for i in range(0,500000):
    try:
        title=root[i][0].text
        try:
            cpe23=root[i][2].attrib["name"]
            if len(root[i][2])>=1:
                cp23uri_date=root[i][2][0].attrib["date"][:10]
            else:
                try:
                    if root[i][2].attrib["deprecated"]=="true":
                        cp23uri_date=root[i][2].attrib["deprecation_date"]
                except:
                        cp23uri_date=None
            b=len(root[i][1])
            referencelinks={}
            for j in range(b):
                dummy=root[i][1][j].attrib["href"]
                # print(dummy)
                referencelinks[j+1]=dummy
            dict1=json.dumps(referencelinks)
            operation.execute("insert into data value(%s,%s,%s,%s)",(title,cpe23,dict1,cp23uri_date))
            mydatabase.commit()
        except:
            try:
                cpe23=root[i][1].attrib["name"]
                if len(root[i][1])>=1:
                            cp23uri_date=root[i][1][0].attrib["date"][:10]
                else:
                    try:
                        if root[i][1].attrib["deprecated"]=="true":
                            cp23uri_date=root[i][1].attrib["deprecation_date"]
                    except:
                            cp23uri_date=None
                
                referencelinks=""
                operation.execute("insert into data value(%s,%s,%s,%s)",(title,cpe23,referencelinks,cp23uri_date))
                mydatabase.commit()
            except:
                referencelinks=""
                cpe23=""
                cp23uri_date=None
                operation.execute("insert into data value(%s,%s,%s,%s)",(title,cpe23,referencelinks,cp23uri_date))
                mydatabase.commit()        
    except:
        title=None
        try:
            cpe23=root[i][1].attrib["name"]
            if len(root[i][1])>=1:
                cp23uri_date=root[i][1][0].attrib["date"][:10]
            else:
                try:
                    if root[i][1].attrib["deprecated"]=="true":
                        cp23uri_date=root[i][2].attrib["deprecation_date"]
                except:
                        cp23uri_date=None

            referencelinks={}
            for j in range(b):
                dummy=root[i][0][j].attrib["href"]
                # print(dummy)
                referencelinks[j+1]=dummy
            dict1=json.dumps(referencelinks)
            operation.execute("insert into data value(%s,%s,%s,%s)",(title,cpe23,dict1,cp23uri_date))
            mydatabase.commit()
        except:
            try:
                cpe23=root[i][0].attrib["name"]
                if len(root[i][0])>=1:
                    cp23uri_date=root[i][0][0].attrib["date"][:10]
                else:
                    try:
                        if root[i][0].attrib["deprecated"]=="true":
                            cp23uri_date=root[i][0].attrib["deprecation_date"]
                    except:
                            cp23uri_date=None
                referencelinks=""
                # cpe23=""
                # cp23uri_date=None
                operation.execute("insert into data value(%s,%s,%s,%s)",(title,cpe23,referencelinks,cp23uri_date))
                mydatabase.commit()
            except:
                operation.execute("insert into data value(%s,%s,%s,%s)",(None,None,None,None))
                mydatabase.commit()
                
    # try:
    #     cpe23=root[i][2].attrib["name"]
    # except:
    #     try:
    #         cpe23=root[i][1].attrib["name"]
    #     except:
    #         cpe23=None    
    # if len(root[i][2])>=1:
    #     cp23uri_date=root[i][2][0].attrib["date"][:10]
    # else:
    #     try:
    #         if root[i][2].attrib["deprecated"]=="true":
    #             cp23uri_date=root[i][2].attrib["deprecation_date"]
    #     except:
    #             cp23uri_date=None

    
    

# print("Inserted")


