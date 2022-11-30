import json
records = []
email_dob = []
try:
    fs = open("data.txt","r")
    for data in fs:
        d = data.split("\n")
        to_json = json.loads(d[0])
        records.append(to_json)

    email ="e"
    dob = "dob"
    for i in records:
        if email in i.keys():
            if dob in i.keys():
                email_dob.append((i["e"],i["dob"]))
            else:
                email_dob.append((i["e"],))


    for k in email_dob:
        print(k)
except:
    print("file not found, try again")