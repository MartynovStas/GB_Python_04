
a, n, num = [int(i) for i in input('Введите список через пробелж: ').split()], int(input('Введите число: ')), 100
for i in range(len(a)):
    if a[i] < n:
        num = -num
    else:
        num = num + 0
    if a[i] >= n and a[i] - n <= num - n:
        num = a[i]
    elif a[i] <= n and num - n <= a[i] - n:
        num = a[i]
print(num)
