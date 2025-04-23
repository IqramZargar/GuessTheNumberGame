#using import random module so to get any random number between given numbers
import random
rand_num = random.randint(1,100) #Stored the random number in rand_num

#Running while loop so to ask user to guess the number until user finds it.
while True:
    guess_no = input("GUESS ANY NUMBER BETWEEN 1-100 or QUIT(Q) :- ")
#Taken input from user and stored it in guess_no & the user can guess the number or quit the game by simple typing Q.
    if guess_no == "Q":
#checking whether user entered 'Q' or not. If yes then game is over. If not the it moves to another conditonal statements.
        break
    guess_no = int(guess_no)
#type casting the value from user from type-string to type-int so to match the rules of game.    
    if guess_no == rand_num:
        print("BINGO! YOU GOT IT RIGHT")
        break

    elif guess_no < rand_num:
        print("YO SHOULD GUESS A BIT LARGER VALUE")

    elif guess_no > rand_num:
        print("YO SHOULD GUESS A BIT SMALLER VALUE")
#simple use of conditional statements if user guessed the number then game is over and if not then is number lesser or greater and shown accordingly to user.        

print("---------GAME OVER-----------")


    

