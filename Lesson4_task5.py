from requests import get, utils
import datetime


def main(argv):
    currency1, date_time1 = (currency_rates(argv[1]))  # Получаем результат работы функции currency_rates и выводим его на экран
    print(currency1, date_time1)

    return 0


response = utils.get_unicode_from_response(get('https://www.nationalbank.kz/rss/rates_all.xml'))  #Получаем данные курсов валют нац банка Казахстана


def currency_rates(code):
    response_content = response.split("item")                                                     #Сплитим на блоки, относящиеся к каждой конкретной валюте
    for i in response_content:                                                                    #Исправляем регистр строки-аргумента нашей функциии currency_rates()
        if code.upper() in i:
            currency = float(i.replace("/", "").split("<description>")[-2])                       #Извлекаем курс валюты
            actual_time = (i.replace("/", "").split("<pubDate>")[-2])                             #Извлекаем дату
            format = "%d.%m.%Y"                                                                   #Задаем формат для метода strptime(), в этом формате содержится дата в строке.
            date_time = datetime.datetime.strptime(actual_time, format).date()                    #Преобразуем строку actual_time из строки в объект datetime и затем, в объект date
    return currency, date_time                                                                    #Выдаем результат


if __name__ == '__main__':
    import sys

    exit(main(sys.argv))
