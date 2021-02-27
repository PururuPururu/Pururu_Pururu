phrase = ['В', '5', 'часов',
          '17', 'минут', 'температура',
          'воздуха', 'была', '-5',
          'градусов']
print(id(phrase))
counter1 = 0
while counter1 < len(phrase):
    if (phrase[counter1].isdigit() or
       (phrase[counter1][1::].isdigit() and
       ('-' in phrase[counter1] or '+' in phrase[counter1]))):
        phrase.insert(counter1+1, '"')
        phrase.insert(counter1, '"')
        counter1 += 2
    counter1 += 1
print(phrase)

phrase_out = ''
counter1 = 0
while counter1 < len(phrase):
    if phrase[counter1].isalpha():
        phrase_out += phrase[counter1] + ' '
    if phrase[counter1].isdigit():
        phrase_out += phrase[counter1 - 1] + \
                      '{:02d}'.format(int(phrase[counter1])) + \
                      phrase[counter1 + 1] + ' '
    if (phrase[counter1][1::].isdigit() and
       ('-' in phrase[counter1] or '+' in phrase[counter1])):
        phrase_out += phrase[counter1 - 1] + \
                      '{:03d}'.format(int(phrase[counter1])) + \
                      phrase[counter1 + 1] + ' '
    counter1 += 1

print(phrase_out)
print(id(phrase))
# print('-' in phrase[-2] or '+' in phrase[-2])
#
# print('{:+03d}'.format(int(phrase[-2])))

