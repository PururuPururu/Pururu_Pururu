import sys

with open('users.csv', 'r', encoding='utf-8') as file_users, open('hobby.csv', 'r', encoding='utf-8') as file_hobby:
    new_dict = {}
    i = 0
    j = 0
    for line in file_users:
        i += 1
    for line in file_hobby:
        j += 1
    if i < j:
        sys.exit(1)
    file_users.seek(0, 0)
    file_hobby.seek(0, 0)
    for line in file_users:
        a = file_hobby.readline().rstrip('\n')
        if a:
            new_dict[line.split()[0].replace(',', ' ')] = a
        else:
            new_dict[line.split()[0].replace(',', ' ')] = 'None'

print(new_dict.items())
