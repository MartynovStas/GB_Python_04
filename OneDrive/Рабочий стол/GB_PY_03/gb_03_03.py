slovar = {1:"AEIOULNSTRАВЕИНОРСТ",2:"DGДКЛМПУ",3:"BCMPБГЁЬЯ",
        4:"FHVWYЙЫ",5:"KЖЗХЦЧ",8:"JXШЭЮ",10:"QZФЩЪ"}

s = input("Введите слово: ").upper()
sum = 0
for i in s:
    for k, v in slovar.items():
        if i in v:
            sum += k
print(f"Стоимость слова: {sum}")