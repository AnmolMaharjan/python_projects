
import json, csv

with open('users.json', 'r') as json_file:
    json_data = json.load(json_file)

csv_data = open('to_users.csv','w')
csv_write = csv.writer(csv_data)

count = 0

for i in json_data:
    if count == 0:
        header = i.keys()
        csv_write.writerow(header)
        count += 1
    
    csv_write.writerow(i.values())
csv_data.close()