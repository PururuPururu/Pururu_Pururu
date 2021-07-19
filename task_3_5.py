from random import choice
from random import shuffle

# исходные данные для шуток
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


# функция, генерирующая шутки из исходных данных
def get_jokes(num, repeat=''):
    shuffle(nouns)  # перемешиваем элементы в списках исходных данных
    shuffle(adverbs)
    shuffle(adjectives)
    jokes = []  # создаем пустой список, куда мы будем складывать сгенерированные шутки
    num = int(num)
    if repeat == '':  # если флаг повтора пустой, то генерируем запрошенное количество шуток. Могут быть повторы.
        count = 0
        while count < num:
            jokes.append(f'{choice(nouns)} '
                         f'{choice(adverbs)} '
                         f'{choice(adjectives)}')
            count += 1
    elif repeat != '' and num <= 5:  # если флаг повтора не пустой, то генерируем уникальные шутки, до 5 штук.
        count = 0
        while count < num:
            jokes.append(f'{nouns.pop()} '
                         f'{adverbs.pop()} '
                         f'{adjectives.pop()}')
            count += 1
    else:
        jokes = 'Вы ввели неверные аргументы'
    return jokes


print(f'Введите желаемое количество шуток. '
      f'Если хотите избежать повторов, через пробел '
      f'напишите любой символ. '
      f'Но количество шуток должно быть не более 5')

b = list(map(lambda x: x.strip(), input().split(',')))  # выделяем из вводимых данных символы и формируем из них список
joke_num = int(b[0])  # преобразуем первый элемент в число
rep = ''
if len(b) > 1:  # проверяем, ввел ли флаг повторов.
    rep = b[1]
print(get_jokes(joke_num, rep))
