# import xml.etree.ElementTree as ET

# tree=ET.parse('official-cpe-dictionary_v2.3.xml')

# root=tree.getroot()

# text=[]
# cp23uri=[]
# cp23uri_date=[]
# referencelinks={}
# for i in range(375,380):
#     text.append(root[i][0].text)
#     cp23uri.append(root[i][2].attrib["name"])
#     if len(root[i][2])>=1:
#         cp23uri_date.append(root[i][2][0].attrib["date"][:10])
#     else:
#         try:
#             if root[i][2].attrib["deprecated"]=="true":
#                 cp23uri_date.append(root[i][2].attrib["deprecation_date"])
#         except:
#                 cp23uri_date.append(None)
    
#     b=len(root[i][1])
#     for j in range(b):
#         dummy=root[i][1][j].attrib["href"]
#         # print(dummy)
#         referencelinks[j+1]=dummy
    
# print(text)
# print(cp23uri)
# print(cp23uri_date)
# print(referencelinks)

# # print(root[421][2].attrib)
    

import xml.etree.ElementTree as ET

tree=ET.parse('official-cpe-dictionary_v2.3.xml')

root=tree.getroot()


for cpe in root.findall("cpe-item"):
    a=cpe.find("title").text
    print(a)
    break
