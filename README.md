🎯 Number Guessing Game (Python)
A simple command-line number guessing game built with Python. The program generates a random number between 1 and 100, and the user tries to guess it. The game gives hints until the correct number is guessed or the user quits.

🧠 How It Works
The program uses Python’s built-in random module to generate a random number between 1 and 100.

The user is prompted to guess the number or type Q to quit.

Based on the user's guess, the program provides feedback:

If the guess is correct: 🎉 BINGO! YOU GOT IT RIGHT

If the guess is too low: 📉 YO SHOULD GUESS A BIT LARGER VALUE

If the guess is too high: 📈 YO SHOULD GUESS A BIT SMALLER VALUE

The game continues until the correct number is guessed or the user quits.

🛠️ Requirements
Python 3.x

🚀 How to Run
Clone this repository or copy the code into a .py file:

bash
git clone https://github.com/IqramZargar/GuessTheNumberGame
cd GuessTheNumberGame
Run the game:

bash
python guess_game.py
Follow the prompts and try to guess the number!

📝 Code Overview
python
import random

rand_num = random.randint(1, 100)

while True:
    guess_no = input("GUESS ANY NUMBER BETWEEN 1-100 or QUIT(Q) :- ")
    if guess_no == "Q":
        break
    guess_no = int(guess_no)

    if guess_no == rand_num:
        print("BINGO! YOU GOT IT RIGHT")
        break
    elif guess_no < rand_num:
        print("YO SHOULD GUESS A BIT LARGER VALUE")
    elif guess_no > rand_num:
        print("YO SHOULD GUESS A BIT SMALLER VALUE")

print("---------GAME OVER-----------")
📦 Features
Simple and fun game logic

Clean input handling

Easy to understand and modify

Great for Python beginners

🧊 Tips
Try modifying the number range to make it easier or harder.

Add a counter to track how many guesses it took.

Implement a high score feature!
# GuessTheNumberGame
