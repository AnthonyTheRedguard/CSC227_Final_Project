from random import randint
from time import sleep


def display_menu(options, num):
    print("WOW! Such a wondrous variety of beverages to choose from!\n")
    print("1. Pepsi                        $1.00")
    print("2. Diet Dr. Pepper              $1.00")
    print("3. Mountain Dew                 $1.50")
    print("4. Schweppes Ginger Ale         $1.25")
    print("5. Mug Root Beer                $1.25")
    print("6. Crush Orange                 $1.75")
    print("7. Crush Grape                  $1.75")
    print("8. Crush Strawberry             $1.75")
    print("9. Aquafina                     $1.00")
    print("10. Kick the vending machine    FREE")
    print("11. Take a sip")
    print("12. Count your soda")
    print("13. Check your wallet")
    print("14. Go home")
    _choice = options[num]
    print(f'You picked option {_choice}')
    print("\n")

    if 14 >= choice >= 1:
        return choice
    else:
        print("Invalid Option. Choose a number 1-11\n")


def bonus_soda(_sodas, _encumbrance):
    bonus = randint(1, 25)
    if bonus == 14:
        print("Bonus Soda!!!\n")
        _sodas += 1
        _encumbrance += 0.5


test_case = [11, 10, 10, 10, 10, 1, 2, 11, 3, 4, 5, 6, 7, 8, 9, 10, 10, 11, 12, 13, 11, 14]
wallet = 25.00
vendor_money = 100.00
encumbrance = 0
sodas = 0
failed_attempts = 0
i = 0

print("As you're walking down the street, you notice a strange looking vending machine. You're feeling quite \n"
      "parched, so you decide to go check it out.\n")

sleep(3.5)

while True:
    choice = display_menu(test_case, i)
    i += 1
    if wallet >= 1.00:
        if choice == 1 or choice == 2 or choice == 9:
            wallet -= 1.00
            vendor_money += 1.00
            sodas += 1
            encumbrance += 0.5
            bonus_soda(sodas, encumbrance)
            print("Soda Acquired\n")
        elif choice == 3 and wallet > 0:
            wallet -= 1.50
            vendor_money += 1.50
            sodas += 1
            encumbrance += 0.5
            bonus_soda(sodas, encumbrance)
            print("Soda Acquired\n")
        elif choice == 4 or choice == 5:
            wallet -= 1.25
            vendor_money += 1.25
            sodas += 1
            encumbrance += 0.5
            bonus_soda(sodas, encumbrance)
            print("Soda Acquired\n")
        elif choice == 6 or choice == 7 or choice == 8:
            wallet -= 1.75
            vendor_money += 1.75
            sodas += 1
            encumbrance += 0.5
            bonus_soda(sodas, encumbrance)
            print("Soda Acquired\n")
    else:
        if choice in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            print("You got soda money?\n")
    if choice == 10:
        cashback = randint(0, 201)
        if cashback == 1:
            print("You kicked a penny out from under the machine. +$0.01\n")
            wallet += 0.01
        elif cashback == 2:
            print("JACKPOT! Someone saw your sick kicks, and asked you to teach them. +$99.99\n")
            wallet += 99.99
        elif cashback == 25:
            print("Nice! You managed to get a quarter out from a secret compartment. +$0.25\n")
            wallet += 0.25
        elif cashback == 100:
            print("Heck yeah! While kicking the vending machine, you noticed a dollar bill laying on top of it. +$1.00\n")
            wallet += 1.00
        elif cashback not in [1, 2, 25, 100] and failed_attempts < 5:
            print("Ouch\n")
            failed_attempts += 1
        elif failed_attempts == 5:
            print("Congratulations, after fruitlessly kicking the vending machine 20 times, you broke your toe.\n"
                  "Who'd a thunk it?\n")
            failed_attempts += 1
        elif cashback not in [1, 2, 25, 100] and failed_attempts > 5:
            print("OUUUUUUUUUUUUUUUUCH!!!!!!!\n")
            failed_attempts += 1
    elif choice == 11:
        if sodas >= 1:
            sodas -= 1
            print('You took a sip of some tasty soda.\n')
        else:
            print("How doest one sip soda, if thou hast no soda to sip?\n")
    elif choice == 12:
        print(f'You have {sodas} sodas in your inventory.\n')
    elif choice == 13:
        print(f'You have ${wallet} in your wallet.\n')
    elif choice == 14:
        if encumbrance > 10:
            print("You're carrying over 10lbs of soda. Have fun walking home.\n")
            if failed_attempts > 5:
                print("Your broken toe makes the walk even more fun.\n")
            break
        elif sodas >= 8 and encumbrance <= 10:
            print("You make your way home with your bountiful harvest.\n")
            if failed_attempts > 5:
                print("Your broken toe makes the walk even more fun.\n")
            break
        else:
            print("You calmly make your way home.\n")
            if failed_attempts > 5:
                print("Your broken toe makes the walk even more fun.\n")
            break
