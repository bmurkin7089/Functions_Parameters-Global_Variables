#Coin flip program
#Describe the purpose of this program here.

import random, time #imports random and time inbuilt functions



def roll():


    s1 = "- - - - -\n|       |\n|   O   |\n|       |\n- - - - -\n"   #
    s2 = "- - - - -\n| O     |\n|       |\n|     O |\n- - - - -\n"   #
    s3 = "- - - - -\n| O     |\n|   O   |\n|     O |\n- - - - -\n"   # All of rhese are variables that display
    s4 = "- - - - -\n| O   O |\n|       |\n| O   O |\n- - - - -\n"   # the dice...
    s5 = "- - - - -\n| O   O |\n|   O   |\n| O   O |\n- - - - -\n"   #
    s6 = "- - - - -\n| O   O |\n| O   O |\n| O   O |\n- - - - -\n"   #


    print("rolling.....")
    roll = random.randint(1,7)
    print(roll)

    if roll == 1:
        print(s1)
    elif roll == 2:
        print(s2)
    elif roll == 3:
        print(s3)
    elif roll == 4:
        print(s4)
    elif roll == 5:
        print(s5)
    elif roll == 6:
        print(s6)


roll()
