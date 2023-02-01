# task 1
while True: 
  guess = input("guess the letter ")
  if len(guess) == 1 and guess.isalpha(): 
    break
  else: 
    print("Invalid letter. Please, enter a single alphabetical character.")

# task 2
word = "apple"
guess = "a"
if guess in word: 
  print(f"Good guess! {guess} is in the word.")
else:
  print(f"Sorry, {guess} is not in the word. Try again.")
