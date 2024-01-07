# *** Hi-Lo Game ***
import random
list=[12]
while True:
    # Rules
    print("Rules of Hi-Lo: \nIf Card = 2-9 : 1.5X \nIf Card = JQKA : 3X \nIf Card = KA : 6X \nIf Card = A : 12X \nIf Card = Joker : 24X \nIf Card = Hi : Conditional \nIf Card = Lo : Conditional")

    # Previous card
    if list[-1]==1 or list[-1]==2:
        print("Previous Card was = 2")
    elif list[-1]==3 or list[-1]==4:
        print("Previous Card was = 3")
    elif list[-1]==5 or list[-1]==6:
        print("Previous Card was = 4")
    elif list[-1]==7 or list[-1]==8:
        print("Previous Card was = 5")
    elif list[-1]==9 or list[-1]==10:
        print("Previous Card was = 6")
    elif list[-1]==11 or list[-1]==12:
        print("Previous Card was = 7")
    elif list[-1]==13 or list[-1]==14:
        print("Previous Card was = 8")
    elif list[-1]==15 or list[-1]==16:
        print("Previous Card was = 9")
    elif list[-1]==17 or list[-1]==18:
        print("Previous Card was = J")
    elif list[-1]==19 or list[-1]==20:
        print("Previous Card was = Q")
    elif list[-1]==21 or list[-1]==22:
        print("Previous Card was = K")
    elif list[-1]==23 or list[-1]==24:
        print("Previous Card was = A")
    elif list[-1]==25:
        print("Previous Card was = *Joker*")

    # Bet Info
    while True:
        bet=int(input("Enter your bet amount: "))
        if bet in range(1,100001):
            break
        else:
            print("Please enter bet amount in the range 10-100000")
            continue

    while True:
        choice = int(input("Enter \n'1' for 2-9 \n'2' for JQKA \n'3' for KA \n'4' for A \n'5' for Joker \n'6' for Hi \n'7' for Lo \n'8' for Red \n'9' for Black \n\nYour Choice : "))
        if choice in range(1,10):
            break
        else:
            print("Please enter a valid choice") 
            continue

    # Computer generated random card
    comp=random.randint(1,25)
    list.append(comp)
    if comp==1 or comp==2:
        print("Card = 2")
    elif comp==3 or comp==4:
        print("Card = 3")
    elif comp==5 or comp==6:
        print("Card = 4")
    elif comp==7 or comp==8:
        print("Card = 5")
    elif comp==9 or comp==10:
        print("Card = 6")
    elif comp==11 or comp==12:
        print("Card = 7")
    elif comp==13 or comp==14:
        print("Card = 8")
    elif comp==15 or comp==16:
        print("Card = 9")
    elif comp==17 or comp==18:
        print("Card = J")
    elif comp==19 or comp==20:
        print("Card = Q")
    elif comp==21 or comp==22:
        print("Card = K")
    elif comp==23 or comp==24:
        print("Card = A")
    elif comp==25:
        print("Card = *Joker*")
    
    # Check for bet outcome
    if choice==1 and (comp in range(1,17)):
        print("You Win : ",bet*1.5,"\n")
    elif choice==2 and (comp in range(17,25)):
        print("You Win : ",bet*3,"\n")
    elif choice==3 and (comp in range(21,25)):
        print("You Win : ",bet*6,"\n")
    elif choice==4 and (comp in range(23,25)):
        print("You Win : ",bet*12,"\n")
    elif choice==5 and comp==25:
        print("You Win : ",bet*24,"\n")  
    elif choice==6 and comp>list[-2]:
        print("You Win : ",bet*2,"\n")
    elif choice==7 and comp<list[-2]:
        print("You Win : ",bet*2,"\n")
    elif choice==8 and comp%2==1:
        print("You Win : ",bet*2,"\n")
    elif choice==9 and comp%2==0:
        print("You Win : ",bet*2,"\n")
    else:
        print("You Lose : ",bet,"\n")

    # Continue or Quit using while loop at the start 
    counter=int(input("Enter 1 to continue and 2 to quit\n"))
    if counter==1:
        continue
    else:
        break 
    


