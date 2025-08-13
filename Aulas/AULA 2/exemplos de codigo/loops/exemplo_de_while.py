from random import randint

number = randint(1, 100)

while True:

    guess = int(input("Adivinhe o número entre 1 e 100: "))

    if guess == number:
        print("Parabéns! Você adivinhou o número.")
        break
    elif guess < number:
        print("Tente um número maior.")
    else:
        print("Tente um número menor.")
