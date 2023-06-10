import random

lwr_bnd=int(input("choose a lower bound"))
up_bnd=int(input("choose a upper bound"))

if lwr_bnd<up_bnd:
    rnd_int = random.randint(lwr_bnd,up_bnd)
    while True:
        guess = int(input('Please guess a number'))
        if guess < lwr_bnd or guess > up_bnd:
            print("please choose a number between your lower and upper bound.")

        elif guess == rnd_int:
            print('You got it!')
            break

        elif guess > rnd_int:
            print('Nope, too high.')
        else:
            print('Nope, too low.')
