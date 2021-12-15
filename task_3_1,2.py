dict_numerals = {'One': 'Один',
                 'Two': 'Два',
                 'Three': 'Три',
                 'Four': 'Четыре',
                 'Five': 'Пять',
                 'Six': 'Шесть',
                 'Seven': 'Семь',
                 'Eight': 'Восемь',
                 'Nine': 'Девять',
                 'Ten': 'Десять'}


def num_translate(en_numeral):
    if en_numeral.islower() and dict_numerals.get(en_numeral.capitalize()) is not None:
        return dict_numerals.get(en_numeral.capitalize()).casefold()
    elif en_numeral.istitle() and dict_numerals.get(en_numeral.capitalize()) is not None:
        return dict_numerals.get(en_numeral.capitalize()).capitalize()  # Второй capitalize() для наглядности
    else:
        return dict_numerals.get(en_numeral)


eng_numeral = input('Введите английское числительное для перевода: ')
if num_translate(eng_numeral) is None:
    print('Вы ввели некорректные данные')
else:
    print(f'{eng_numeral} переводится как '
          f'{num_translate(eng_numeral)}')
