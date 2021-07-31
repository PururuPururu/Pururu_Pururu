def nums_generator(max_num):                                #Создаем функцию, возвращающую генератор
   for num in range(1, max_num + 1, 2):
       yield num

num_gen = nums_generator(15)
print(*num_gen, type(num_gen))

max_num = 21
num_gen_2 = (num for num in range(1, max_num + 1, 2))       #Создаем генератор, используя генераторное выражение
print(*num_gen_2, type(num_gen_2))