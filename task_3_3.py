# ' Kolya ,  Vasya, Igor,Inna,Anna ,   Boris  ' тестовая строка


def thesaurus(w_names):
    w_names_dict = {}
    for el in w_names:
        if el[0] not in w_names_dict:
            w_names_dict[el[0]] = []
            w_names_dict[el[0]].append(el)
        else:
            w_names_dict[el[0]].append(el)
    return  w_names_dict


workers_names = list(map(lambda x: x.strip(),
                 input('Введите имена работников через запятую').split(',')))
workers_names_dict = thesaurus(workers_names)
print('Несортированный словарь:')
for el in workers_names_dict:
    print(f'{el}:, {workers_names_dict[el]}')
print('Сортированный словарь:')
for el in sorted(list(workers_names_dict.keys())):
    print(f'{el}:, {workers_names_dict[el]}')
