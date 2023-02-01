Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.

in Milestone 2, the following tasks are accomplished:
Task 1 Defines a list of possible words
Task 2 Chooses a random word from the list 
Task 3 asks the user for an input
Task 4 Checks that the input is a single character
And finally, Task 5 Encourages the user to document the experience of coding the program

# Milestone 3
Here, the program creates two functions. 
- check_guess function takes a guessed letter as an argument, converts the guess into lowercase,  and checks if the letter is in the word. 

- ask_for_input function iteratively checks if the input is a valid guess using a while loop. The loop checks if the guess is a single, alphabetical character. The check_guess function is also utilised here to check if the guess is in the word. 

# Milestone 4
Here, the program scripts the class for the Hangman game.

the constructor __init__ has two parameters word_list, num_lives = 5. Also, it initializes key attributes of the class such as word, word_guessed, num_letters, and list_of_guesses

ask_for_input() method prompts the user to input a single alphanumerical character. 
check_guess() method takes in the input from the user, makes it lowercase, and checks the necessary conditions of the hangman game. When the user input corresponds with a letter in the word, it replaces the '_' in the word_guessed list. 

# Milestone 5
creates play_game function that takes in a wordlist, and plays the hangman game. 

first, it initialises the num_lives and creates an instance of the Hnagman game called game. 

In a while loop, checks the num_lives available and at the end when num_lives = 0, it prints "You lost!"

As long as the num_letters>0 continues to ask for user input. 

and when the user has guessed all characters correctly before end of num_lives, it congratualte the user. 
