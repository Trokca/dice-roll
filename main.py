import random


def roll_dice(max_val):
    return random.randint(1, max_val)


T_dice = [2, 4, 6, 8, 10, 12, 20, 100]  # Варианты кубиков
print("There are these types of dice: ", T_dice)
print("What dice are you roll?")
while True:
    try:
        N_dice = int(input())  # Вводим нужный кубик
        if N_dice <= 100:
            if N_dice not in T_dice:
                print("There is no such dice in dnd, but as you say")
            print("Result is", roll_dice(N_dice))
        else:
            print("To much, 100 and no more")
    except:
        print("Oops, this is not number")
    print("Do you want to roll again? (Yes/No)")
    ans = input().lower()
    if ans == "no":
        break
    elif ans != "yes":
        print("You are talking nonsense, so I will assume that you want to finish")
        break
    elif ans == "yes":
        print("Then write what dice you want to roll")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
