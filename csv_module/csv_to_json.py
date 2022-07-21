
import json, csv

csv_file = open('users.csv', 'r')
csv_data = csv.DictReader(csv_file)

mylist = []
mydict = {}

for i in csv_data:
    if i == []:continue
    else:
        key = ''
        mydict[key] = i
    for k in mydict.values():
        mylist.append(k)
csv_file.close()

json_file = open('to_users.json', 'w')
json_file.write(json.dumps(mylist))