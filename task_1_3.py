percent = input('Введите число от 0 до 20 или напишите "S" для вывода всех склонений: ')

try: #честно, я за полчаса не смог придумать, как перестать получать ВалуеЭррор, если у меня в инпут падает не S, а другая строка
    if (percent == 'S') or (0 <= int(percent) <= 20):
        if percent == 'S':
            i = 0
            while i <= 20:
                if (i == 0) or (5 <= i <= 20):
                    print(i, ' процентов')
                elif i == 1:
                    print(i, ' процент')
                elif 2 <= i <= 4:
                    print(i, ' процента')
                i += 1
        if percent != 'S':
            percent = int(percent)
        if (percent != 'S') and ((percent == 0) or (5 <= percent <= 20)):
            print(percent, ' процентов')
        elif (percent != 'S') and (percent == 1):
            print(percent, ' процент')
        elif (percent != 'S') and (2 <= percent <= 4):
            print(percent, ' процента')
    else:
        print('Вы ввели некорректное значение')
except ValueError:
    print('Вы ввели некорректное значение')
