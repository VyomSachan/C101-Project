import random

roll_the_dice_status= input("Do you want to roll a dice or not? (Answer y for yes and n for no) : ")

while roll_the_dice_status == "y":
    number = random.randint(1, 6)
    if number == 1:
        print("[-----]")
        print("[     ]")
        print("[  *  ]")
        print("[     ]")
        print("[-----]")
    if number == 2:
        print("[-----]")
        print("[ *   ]")
        print("[     ]")
        print("[   * ]")
        print("[-----]")
    if number == 3:
        print("[-----]")
        print("[     ]")
        print("[* * *]")
        print("[     ]")
        print("[-----]")
    if number == 4:
        print("[-----]")
        print("[*   *]")
        print("[     ]")
        print("[*   *]")
        print("[-----]")
    if number == 5:
        print("[-----]")
        print("[*   *]")
        print("[  *  ]")
        print("[*   *]")
        print("[-----]")
    if number == 6:
        print("[-----]")
        print("[* * *]")
        print("[     ]")
        print("[* * *]")
        print("[-----]")

    roll_the_dice_status= input("Do you want to roll a dice or not? (Answer y for yes and n for no) : ")
    print("\r")