from random import randint
n = int(input('Введите размер масива: '))
a = int(input('Введите число которое нужно найти в  масиве: '))
sum = 0
numbers = []
for i in range(n):
    numbers.append(randint(0, 9))
print(numbers)
for color in numbers:
    if color == a:
         sum+= 1
print('Элемент присутствует в списке!')if a in numbers else print('Элемент отсутствует в списке!')
print(f'количество совпадений:',sum)



