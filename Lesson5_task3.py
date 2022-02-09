tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б'
]

tuple_gen = ((tutors[i], klasses[i]) if len(klasses) > i else (tutors[i], None) for i in range(len(tutors)))

print(type(tuple_gen), *tuple_gen)
print('(', *tuple_gen, ')')