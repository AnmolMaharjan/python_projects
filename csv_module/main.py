
import csv,sys

filename = 'read.csv'

# with open('read.csv','r') as csvread:
#     csv_file1 = csv.reader(csvread, delimiter=' ')
#     for row in csv_file1:
#         print(', '.join(row))

# with open('write.csv', 'w') as csvwrite:
#     csv_file2 = csv.writer(csvwrite, lineterminator='\t\t', delimiter=':')
#     csv_file3 = csv.writer(csvwrite)
#     for i in range(1,11):
#         for j in range(1,11):
#             csv_file2.writerow([f'{j} x {i} = {i*j}'])
#         csv_file3.writerow([])

# with open(filename, newline='', encoding='utf-8') as csvread:
#     csv_file2 = csv.reader(csvread)
#     try:
#         for row in csv_file2:
#             if row == []:continue
#             print(row)
#     except csv.Error as e:
#         sys.exit(f'File {filename}, line{csv_file2.line_num}:{e}')

with open(filename, newline='', encoding='utf-8') as csvread:
    csv_file = csv.DictReader(csvread)
    for i in csv_file:
        print(i['name'],i['phone_no'])