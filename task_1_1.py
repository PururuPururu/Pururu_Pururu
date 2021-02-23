#Время скоротечно
raw_seconds = int(input('Введите количество секунд: '))

const_sec_to_mins = 60
const_sec_to_hours = 3600
const_sec_to_days = 86400
const_sec_to_months = 2592000 #Константа примерная, месяц условно равен 30 дням
const_sec_to_years = 31104000 #Константа примерная, год равен 12 условным месяцам

seconds = 0
minutes = 0
hours = 0
days = 0
months = 0
years = 0

years = raw_seconds // const_sec_to_years
months = (raw_seconds % const_sec_to_years) // const_sec_to_months #можно сделать вычитанием из raw_seconds
days = (raw_seconds % const_sec_to_months) // const_sec_to_days #значения предыдущего разряда, умноженного на нужную константу
hours = (raw_seconds % const_sec_to_days) // const_sec_to_hours #например, hours = (raw_seconds - days * const_sec_to_days) // const_sec_to_hours
minutes = (raw_seconds % const_sec_to_hours) // const_sec_to_mins #потому что умножение и вычитание должны быть быстрее деления, но это не точно (:
seconds = raw_seconds % const_sec_to_mins #Короткий анекдот: человек похож на розу: иногда ему нужна таблетка аспирина и свежая вода.

output_string = ''

if years:
    output_string += 'Y: ' + str(years) + ', '
if months:
    output_string += 'M: ' + str(months) + ', '
if days:
    output_string += 'D: ' + str(days) + ', '
if hours:
    output_string += 'h: ' + str(hours) + ', '
if minutes:
    output_string += 'm: ' + str(minutes) + ', '
if seconds:
    output_string += 's: ' + str(seconds) + '.'

print(output_string)


