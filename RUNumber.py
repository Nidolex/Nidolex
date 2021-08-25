print("Проверка номера на стоимость")
print("1 балл - 1 рубль")
print("Пример: 89291239999")
number = input("Введите номер телефона: ")

#1-ый этап

numberfind1 = number.count("1")
numberfind2 = number.count("2")
numberfind3 = number.count("3")
numberfind4 = number.count("4")
numberfind5 = number.count("5")
numberfind6 = number.count("6")
numberfind7 = number.count("7")
numberfind8 = number.count("8")
numberfind9 = number.count("9")
numberfind0 = number.count("0")
numberfindall = 0

simple = [numberfind1, numberfind2, numberfind3,
          numberfind4, numberfind5, numberfind6]
dimple = [numberfind7, numberfind8, numberfind9]
for q in simple:
    if q >= 11:
        numberfindall += 1000000000
    elif q >= 10:
        numberfindall += 10000000
    elif q >= 9:
        numberfindall += 1000000
    elif q >= 8:
        numberfindall += 25000
    elif q >= 7:
        numberfindall += 10000
    elif q >= 6:
        numberfindall += 5000
    elif q >= 5:
        numberfindall += 2500
    elif q >= 4:
        numberfindall += 1000
    elif q >= 3:
        numberfindall += 250
    elif q >= 2:
        numberfindall += 100


for z in dimple:
    if z >= 11:
        numberfindall += 100000000000
    elif z >= 10:
        numberfindall += 100000000
    elif z >= 9:
        numberfindall += 1000000
    elif z >= 8:
        numberfindall += 25000
    elif z >= 7:
        numberfindall += 15000
    elif z >= 6:
        numberfindall += 5000
    elif z >= 5:
        numberfindall += 2500
    elif z >= 4:
        numberfindall += 1000
    elif z >= 3:
        numberfindall += 250
    elif z >= 2:
        numberfindall += 150

print("Количество баллов за 1 этап: " + str(numberfindall))

#2-ой этап

numbersectionall = 0
numbersection1 = number[1:4]
numbersection2 = number[4:7]
numbersection3 = number[7:9]
numbersection4 = number[9:11]

if numbersection1 == numbersection2:
    numbersectionall += 2000
if numbersection3 == numbersection4:
    numbersectionall += 1000

print("Количество баллов за 2 этап: " + str(numbersectionall))

#3-ий этап

numbersumall = 0
numbersumlista = list(map(int,numbersection1))
numbersum1 = sum(numbersumlista)
numbersumlistb = list(map(int,numbersection2))
numbersum2 = sum(numbersumlistb)
numbersumlistc = list(map(int,numbersection3))
numbersum3 = sum(numbersumlistc)
numbersumlistd = list(map(int,numbersection4))
numbersum4 = sum(numbersumlistd)
numbersum = numbersum1 + numbersum2 + numbersum3 + numbersum4

if int(numbersum1) == int(numbersum2):
    numbersumall += 250
if int(numbersum3) == int(numbersum4):
    numbersumall += 250
if int(numbersum2) == int(numbersum4):
    numbersumall += 250
if int(numbersum1) == int(numbersum3):
    numbersumall += 250
if int(numbersum2) == int(numbersum3):
    numbersumall += 250

print("Количество баллов за 3 этап: " + str(numbersumall))

#4-ый этап

num = number + "0"
counter = 0
for i in range(len(num)):
    if int(num[i-1])-1 == int(num[i]):
        counter += 250

print("Количество баллов за 4 этап: " + str(counter))

#5-ый этап

counter2 = 0
num2 = num
for j in range(len(num2)):
    if int(num2[j-1]) == int(num2[j])-1:
        counter2 += 250

print("Количество баллов за 5 этап: " + str(counter2))

#6-ой этап

counter3 = 0
num3 = num
for k in range(len(num3)):
    if num3[k - 5] + num3[k - 4] + num3[k - 3] == num[k - 2] + num[k - 1] + num[k]:
        counter3 += 1000

print("Количество баллов за 6 этап: " + str(counter3))

#7-ой этап

counter4 = 0
num4 = num
for u in range(len(num4)):
    if num4[u-3] + num4[u-2] == num4[u-1] + num4[u]:
        counter4 += 750

print("Количество баллов за 7 этап: " + str(counter4))

#8-ой этап

counter5 = 0
num5 = num
for y in range(len(num5)):
    if num5[y-3] + num5[y-2] == num5[y] + num5[y-1]:
        counter5 += 500

print("Количество баллов за 8 этап: " + str(counter5))

#9-ый этап

num6 = number
counter6 = 0
for p in range(len(num6)):
    if num6[p-1] == num6[p]:
        counter6 += 250

print("Количество баллов за 9 этап: " + str(counter6))

#10-ый этап

counter7 = 0
numbercut1 = number[2:3]
numbercut2 = number[5:6]
numbercut3 = number[8:9]
numbercut4 = number[10:]

if int(numbercut1) == 0:
    counter7 += 1000
if int(numbercut2) == 0:
    counter7 += 1000
if int(numbercut3) == 0:
    counter7 += 1000
if int(numbercut4) == 0:
    counter7 += 1000

print("Количество баллов за 10 этап: " + str(counter7))

counters = counter + counter2 + counter3 + counter4
counters2 = counter5 + counter6 + counter7
finalpoint = numberfindall + numbersectionall + numbersumall
finalpointall = finalpoint + counters + counters2

print("Количество баллов за все этапы: ", str(finalpointall))