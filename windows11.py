a = int(input('Введи, будь ласка, перше число: '))
b = int(input('А тепер введи друге число: '))
c = input('Введи дію: ')
print('Творю magic...')
if c == "+":
    d = a + b
    print('Результат у мене вийшов ось такий: ', d)
elif c == '-':
    d = a - b
    print('Результат у мене вийшов ось такий: ', d)
elif c == "*":
    d = a * b
    print('Результат у мене вийшов ось такий: ', d)
elif c == "/":
    if b != 0:  # перевірка ділення на нуль
        d = a / b
        print('Результат у мене вийшов ось такий: ', d)
    else:
        print("Помилка! Ділення на нуль!")
else:
    print("Е ні, друже! Щось забагато ти від мене хочеш!")
