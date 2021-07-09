prices = [57.02, 46.01, 97.07, 7.03, 74.42, 123, 54.1, 86, 46, 92.3, 667]

def show_prices(a_list):
    for element in a_list:
        print('{:02d}'.format(int(element)) + ' руб, ' +
              '{:02d}'.format((int((100 * element - 100 * int(element))))) +
              ' коп')

print('Вывод цен')
show_prices(prices)  # Вывод цен

prices.sort()
print('Вывод цен по возрастанию')
show_prices(prices)  # По возрастанию


prices2 = reversed(prices)
print('Вывод цен по убыванию')
show_prices(prices2)  # По убыванию


counter1 = -5
while counter1 < 0:
    print(prices.pop(counter1))  # Вывод 5 самых дорогих товаров по возрастанию.
    counter1 += 1

