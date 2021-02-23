#„Терпение и время дают больше, чем сила или страсть.“ Жан де Лафонтен

list_cube_numbers = [0]
number_length = 0
int_division_by_7_sum = 0
i = 1

while i <= 1000: #инициализируем цикл, для заполнения списка
    if i % 2: #проверяем значение на нечётность, если нечет, то остаток от деления даст 1, что эквивалентно True
        list_cube_numbers.append(i ** 3) #добавляем в список куб числа
        j = 1
        number_length = len(str(list_cube_numbers[-1])) #выясняем количество цифр в числе, преобразовав его в строку
        digit_sum = 0 #переменная для суммы цифр числа
        while j <= number_length:
            digit_sum += (list_cube_numbers[-1] // (10 ** (j - 1))) % 10 #суммируем цифры
            j += 1
        if digit_sum % 7 == 0: #проверка суммы цифр на делимость на 7, если делится без остатка - прибавляем его к сумме.
            int_division_by_7_sum += list_cube_numbers[-1]
           # print(list_cube_numbers[-1], digit_sum, number_length)
    i += 1
print('Сумма кубов чисел от 0 до 1000, сумма цифр которых делится на 7 без остатка: ', (int_division_by_7_sum))
i = 0
int_division_by_7_sum = 0
while i < len(list_cube_numbers):
    list_cube_numbers[i] += 17
    i += 1
for element in list_cube_numbers:
    j = 1
    number_length = len(str(element))
    digit_sum = 0
    while j <= number_length:
        digit_sum += (element // (10 ** (j - 1))) % 10
        j += 1
    if digit_sum % 7 == 0:
        int_division_by_7_sum += element
      #  print(element, digit_sum, number_length)
print('Сумма кубов чисел от 0 до 1000, к которым прибавили 17, сумма цифр которых делится на 7 без остатка: ', int_division_by_7_sum)


# number = int(input())
# number_length = len(str(number))
# digit_sum = 0
# i = 1
#
# while i <= number_length:
#     digit_sum += (number // (10 ** (i - 1))) % 10
#     print(digit_sum)
#     i += 1


