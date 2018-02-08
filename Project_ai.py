from  random import choice
import random

def songs(mood):
    sad_mood=['He Stopped Loving Her Today','Last kiss', 'I will right here waittinh for you', 'Good bye my lover']
    rock_mood=['Numb','Purple Haze', 'Walk this Way', 'Hotel california']
    dance_mood=["Woman", "Complicated", "Bad at love", "X with U"]

    if mood==1:
        return random.choice(sad_mood)
    elif mood==2:
        return random.choice(rock_mood)
    elif mood==3:
        return random.choice(dance_mood)

user_mood=int(input("Press 1 if You are in a sad mood \n" "Press 2 if You are in a Rock mood \n "  "Press 3 if You are in a Party mood\n"))

action=songs(user_mood)
print(action)
