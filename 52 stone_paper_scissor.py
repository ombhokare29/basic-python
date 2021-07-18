
import random


def winning(comp , you):

    
    if comp == you :
        return None

    elif comp == "s":
        if you=="p":
            return True
        elif you=="c":
            return False

    elif comp == "p":
        if you=="c":
            return True
        elif you=="s":
            return False

    elif comp == "c":
        if you == "p":
            return False
        elif you == "s":
            return True

print("computers turn: Stone(s) Paper(p) Scissor(c) ")



randNo = random.randint(1,3)
if randNo==1:
    comp="s"
elif randNo==2:
    comp="p"
elif randNo==3:
    comp="c"

print("computer has chosen..!\n Now its your turn ")


you= input("your turn: \nplease select\nStone(s) Paper(p) Scissor(c) ")

a = winning(comp , you)

print(f"compter chosen: {comp} ")
print(f"you chosen: {you} ")

if a == None:
    print("The Game Is Tie!!")
elif a:
    print("congratulatios!!  You won the Game..")
else:
    print("Better Luck Next Time..You lose.")