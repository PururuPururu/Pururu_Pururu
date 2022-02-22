list_of_tuples = []
with open('nginx_logs.txt', 'r+', encoding='utf-8') as file_1:
    for line in file_1:
        list_of_tuples.append((line.split()[0], line.split()[5][1:],  line.split()[6]))
        #print(line.split()[0], ', ', line.split()[5][1:], ', ', line.split()[6])
for element in list_of_tuples:
    print(element)

dict_of_counts = {}
with open('nginx_logs.txt', 'r+', encoding='utf-8') as file_1:
    for line in file_1:
        if line.split()[0] not in dict_of_counts.keys():
            dict_of_counts.update({line.split()[0]: 1})
        else:
            dict_of_counts[line.split()[0]] += 1
spam_val = max(dict_of_counts.values())
dict_spam = {k: v for k, v in dict_of_counts.items() if v == spam_val}
spam_list = list(*dict_spam.items())
print('Спамер с IP-адресом', spam_list[0], 'отправил', spam_list[1], 'запросов.')
