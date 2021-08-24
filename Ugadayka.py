#Угадай число
import random

chislo = 0
random_ = random.randint(1,100)

while random_ != chislo:
    chislo = int(input("Введите число от 1-100: "))
    if chislo == random_:
        print (f'Вы отгадали загаданное число: {random_}')
    else:
        print (f"Попробуйте ещё раз (Число: {random_})")