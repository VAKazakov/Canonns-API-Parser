#coding=utf-8
import requests
import json
import csv
servers={"live": "https://api.canonn.tech",
         "beta": "https://api.canonn.tech:2053",
         "alpha":"https://api.canonn.tech:2083",
         "local":"https://localhost:1337"}
#r=requests.get("{}/reporttypes?journalID={}&_limit=1000".format(self.getUrl(),id))

def writeToFile(data,count):
    print("writing initilised")
    j=json.dumps(data)
    #with open ('output.csv',"w") as output_file:
    #    dw=csv.DictWriter(output_file,sorted(j),delimiter="\t")
    #    dw.writeheader()
    #    dw.writerows(j)

    f = open('data.txt', 'w')
    this=1
    for row in data[0]:
        print("writing row {}/{}".format(this,count))
        this+=1
        json.dump(row,f)
    f.close()

def CAPIParse(schema,serv):
    print("Retriving data from schema {} on {} server".format(schema,serv))
    url=servers[serv]+"/"+schema 
    urlCount=url+"/count"
    rCount=requests.get(urlCount)
    start=1
    print(rCount.text)
    result=[]
    Count=0
    while start < int(rCount.text):
        print("now retriving {}".format(start))
        r= requests.get(url+"?_start={}&_limit=100".format(start))
       #J=json.load (r.json())
        data=(r.json())
        result.extend(data[0])
        start = start+100
    return result ,rCount.text

if __name__ == "__main__":
    print("programm started")
    rawData,count=CAPIParse("cssites","live")
    #writeToFile(rawData,count)
    print("all done")