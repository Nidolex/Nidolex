from random import randint

def randomizer():
    numb1 = 1
    numb2 = 0
    score = 0
    while int(numb1) != int(numb2):
        numb1 = randint(1,100)
        numb2 = randint(1,100)
        score += 1
        print("Первое число: " + str(numb1))
        print("Второе число: " + str(numb2))
        if int(numb1) == int(numb2):
            print("Количество попыток: " + str(score))
            return
randomizer()
