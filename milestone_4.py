import random

class Hangman:
    def __init__(self, word_list, num_lives=5): 
        self.word = random.choice(word_list)
        self.word_guessed = ['_']*len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

        print(f"{word_list}")
        print(f"word: {self.word}")
        print(f"#unique letters: {self.num_letters}")
        print(f"correctly guessed letters: {self.word_guessed}")
        print(f"lives available: {self.num_lives}")
        print(f"previously guessed letters: {self.list_of_guesses}")
        print("----------------------------------------")

    def check_guess(self, guess):
        guess = guess.lower()
        self.list_of_guesses.append(guess)
        
        if guess in self.word: 
            print(f"Good guess! {guess} is in the word.")
            self.num_letters -= 1
            for i in range(len(self.word)): 
                if self.word[i] == guess: 
                    self.word_guessed[i] = guess

        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
    
        print(f"#unique letters remaining: {self.num_letters}")
        print(f"correctly guessed letters: {self.word_guessed}")
        print(f"lives remaining: {self.num_lives}")
        print(f"previously guessed letters: {self.list_of_guesses}")
        

    def ask_for_input(self):
        while True:
            self.guess = input("guess the letter ")
            if not self.guess.isalpha() or len(self.guess)!=1 : 
                print("Invalid letter. Please, enter a single alphabetical character.")
                print("----------------------------------------")
            elif self.guess in self.list_of_guesses:
                print("You already tried that letter!")
                print("----------------------------------------")
            else: 
                self.check_guess(self.guess)
                print("----------------------------------------")
                if self.num_lives == 0 or self.num_letters == 0:
                    break
    
Hangman(["apple", "banana"], 5).ask_for_input()

