# задаем переменную с просьбой в вести год.
year = int(input('Введите год: '))

if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print('YES')
else:
    print('NO')
