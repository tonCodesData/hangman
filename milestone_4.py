import random

class Hangman:
    def __init__(self, word_list, num_lives=5): 
        self.word = random.choice(word_list)
        self.word_guessed = ['_']*len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
    
    def check_guess(self, guess):
        guess = guess.lower()
        self.list_of_guesses.append(guess)
        if guess in self.word: 
            print(f"Good guess! {guess} is in the word.")
            """for i in range(len(self.word)): 
                if self.word[i] == guess: 
                    self.word_guessed[i] = guess
            self.num_letters -= 1
            

        # when the guess is Not in the word
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")"""
    
    def ask_for_input(self):
        while True:
            self.guess = input("guess the letter ")
            if not self.guess.isalpha() or len(self.guess)!=1 : 
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif self.guess in self.list_of_guesses:
                print("You already tried that letter!")
            else: 
                self.check_guess(self.guess)
"""                if self.num_lives == 0 or self.num_letters == 0:
                    break
"""

new_game = Hangman(["apple", "banana"], 5)
new_game.ask_for_input()
