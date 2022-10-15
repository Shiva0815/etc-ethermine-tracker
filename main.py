import requests
import pymongo

client = pymongo.MongoClient(
    "mongodb://test1508:vHoiWVhMpoHZGXENFJDcse1Sxkdgyi5zEPWrgQOXIvuZ7PbEcdYmNul457FFLue96JD89eWvHguKC6WZNh8DKQ==@test1508.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@test1508@")
mydb = client["mining"]
mycol = mydb["main1"]
miner_address = "0d5C3F715fc150F859F756Ec44dd846AE08A4364"
r = requests.get("https://api-etc.ethermine.org/miner/:" +
                 miner_address+"/dashboard")
if (r.status_code==200):
    d = r.json()
    temp = (d['data']['statistics'])
    l=len(temp)
    for i in range(l):
        res = temp[i]
        check_cod=res['time']
        if (mycol.find_one({"timestamp":check_cod})==None):
            val = {"timestamp": res['time'],
                "cur_has": res['currentHashrate'],
                "rep_has": res['reportedHashrate']
                }
            mycol.insert_one(val)


for b in mycol.find():
    print(list(dict(b).values())[1])
