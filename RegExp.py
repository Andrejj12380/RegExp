# coding=utf-8
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re

with open("phonebook_raw.csv", encoding = 'utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
print(contacts_list)

res_list = [contacts_list[0]]
for j in range(len(contacts_list[1:])):
    name_list = ['', '',  '']
    name = ' '.join(contacts_list[j + 1][0:3]).split(' ')
    for i in range(3):
        name_list[i] = name[i]
    res_list.append(name_list)
    res_list[j + 1] += contacts_list[j + 1][3:]

dict_ = {}

for index in range(1, len(res_list[1:]) + 1):
    man = res_list[index][0:2]
    for name in res_list[index + 1:]:
        if man == name[0:2]:
            for i in range(len(res_list[index])):
                if res_list[index][i] == '' and name[i] != '':
                    res_list[index][i] = name[i]
            dict_[index] = res_list[index]

for row in res_list[1:]:
    for key, value in dict_.items():
        if row[0:2] == value[0:2]:
            res_list.remove(row)
for key, value in dict_.items():
    res_list.append(value)


pattern = r'(\+7|8|7)?\s*\(?(\d{2,4})\)?\s*\-?(\d+)\-?(\d+)\-?(\d+)'
pattern_sub = r'+7(\2)\3\4\5'
pattern_additional = r'\(?доб\.?\s?(\d+)\)?'
pattern_additional_sub = r'доб.\1'

for human in res_list[1:]:
    human[5] = re.sub(pattern, pattern_sub, human[5])
    human[5] = re.sub(pattern_additional, pattern_additional_sub, human[5])


with open("phonebook.csv", "w", newline='') as f:
    data_writer = csv.writer(f , delimiter=',')
    data_writer.writerows(res_list)

print(res_list)