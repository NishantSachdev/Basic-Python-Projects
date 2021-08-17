#write a game function to update a text file with new highscores
 
def game(a):
    with open("highscore.txt","r") as store_highscore:    #opening highscore file in read mode
        retrieve=store_highscore.read()               #reading highscore file
        store_highscore.close()               
    if int(a)>int(retrieve):
        print("old high score was: ",retrieve)
    else:
        print("high score still is: ",retrieve)

    if int(a)>int(retrieve): #if new highscore is greater than previous open and update text file
        store_highscore=open("highscore.txt","w") 
        store_highscore.write(str(a))
        store_highscore.close()
        print("new highscore is: ",a)
b=input("enter a number: ")
game(b)
    


