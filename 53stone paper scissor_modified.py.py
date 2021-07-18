
import random


def winning(comp , you):

    
    if comp == you :
        return None

    elif comp == "s":
        if you=="c":
            return False
        elif you=="p":
            return True

    elif comp == "p":
        if you=="s":
            return False
        elif you=="c":
            return True

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

elif comp=="s" and you== "p":
    print("congratulatios!!  You won the Game..\nYour Paper coverd the stone..")
elif comp=="s" and you== "c":
    print("Better Luck next time..You Lose.\nYour scissor blunded!")
elif comp=="p" and you== "c":
    print("congratulatios!!  You won the Game..\nYour Scissor cut the Paper..")
elif comp=="p" and you== "s":
    print("Better Luck nest time..You Lose.\nYour Stone got cover with paper..")
elif comp=="c" and you== "p":
    print("Better Luck next time..You Lose.\nScissor cut your paper.")
elif comp=="c" and you== "s":
    print("Congratulatios!!  You won the Game..\nYour stone blunded the scissor.")










