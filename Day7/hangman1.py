#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
random_index = random.randint(0,len(word_list))
chosen_word = word_list[random_index]
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

for char in chosen_word:
    if(guess==char):
        print(True)
    else:
        print(False)