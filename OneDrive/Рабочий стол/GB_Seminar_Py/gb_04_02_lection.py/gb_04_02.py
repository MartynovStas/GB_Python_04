import random
list1 = [random.randint(1, 10) for i in range(4)]
print(list1)
max_namber = 0
for i in list1:
    max_namber += max(list1)
    list1.remove(max(list1))
max_namber += max(list1)
print(max_namber)

