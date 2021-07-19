# ' Kolya ,  Vasya, Igor,Inna,Anna ,   Boris  ' тестовая строка

#Можно через распаковку, но я хотел поиграться с лямбдами

#Я не стал делать 4* задание из-за нехватки времени,
#но я сделал бы так: функция собирает и возвращает
# словарь словарей списков. Входные данные сплитим по запятым
# и переводим в список(как в этой задаче), а потом сплитим по пробелу
# и для ключей фамилий берем первый символ из второго элемента получившегося списка.
# Так и собираем словарь.
# print(list(map(lambda x: x.strip(),
#                input().split(','))))  #это точно не лисп? :D

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
