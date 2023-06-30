import random
import hangman_stages

print("Let's Start the Hangman Game")

# List of words for the game
word_list=['apple','banana','pears','grapes','strawberry','mango']
# Select a random word from the list
chosen_word=random.choice(word_list)
display=['_']*len(chosen_word)
print(display)
lives=6

def hangman():
    game_over= False
    while not game_over:
      guessed_letter=input("Guess a letter: ").lower()
      for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter==guessed_letter:
            display[position]=guessed_letter
    print(display)

    if guessed_letter not in chosen_word:
        lives-=1
        if lives==0:
            game_over=True
            print("YOU LOST!!")

    if '_' not in display:
        game_over=True
        print("Congrats!! YOU WON")
    print(hangman_stages.stages[lives])

hangman()

