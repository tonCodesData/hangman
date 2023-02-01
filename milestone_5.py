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
        # in both cases
        guess = guess.lower()
        self.list_of_guesses.append(guess)

        # when the guess is in the word
        if guess in self.word: 
            print(f"Good guess! {guess} is in the word.")
            for i in range(len(self.word)): 
                if self.word[i] == guess: 
                    self.word_guessed[i] = guess
            self.num_letters -= 1

        # when the guess is Not in the word
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
    
    def ask_for_input(self):
        while True:
            self.guess = input("guess the letter ")
            if not self.guess.isalpha() or len(self.guess)!=1 : 
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif self.guess in self.list_of_guesses:
                print("You already tried that letter!")
            else: 
                self.check_guess(self.guess)
            
            if self.num_lives == 0 or self.num_letters == 0:
                break
    
def play_game(word_list):    
    num_lives = 5
    game = Hangman(word_list, 5)
    while True:
        # 1. Check if the `num_lives` is 0. If it is, that means the game has ended and the user lost. Print a message saying 'You lost!'.
        if game.num_lives == 0:
            print('You lost!')
            break
        # 2. Next, check if the `num_letters` is greater than 0. In this case, you would want to continue the game, so you need to call the `ask_for_input` method.
        elif game.num_letters>0:
            game.ask_for_input()  
        # 3. If the `num_lives` is not 0 and the `num_letters` is not greater than 0, that means the user has won the game. Print a message saying 'Congratulations. You won the game!'.
        else:
            print('Congratulations. You won the game!')
            break

play_game(["apple", "banana"])

