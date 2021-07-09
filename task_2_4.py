workers = ['инженер-конструктор Игорь',
           'главный бухгалтер МАРИНА',
           'токарь высшего разряда нИКОЛАй',
           'директор аэлита']

counter1 = 0
while counter1 < len(workers):
    print('Привет, ', workers[counter1].split(' ')[-1].capitalize())
    counter1 += 1
