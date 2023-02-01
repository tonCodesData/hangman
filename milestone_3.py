Write code that will continuously ask the user for a letter and validate it.

# Step 1. Create a while loop and set the condition to True. Setting the condition to True ensures that the code run continuously.
while True: 
  # In the body of the loop, write the code required for the following steps.
  # Step 2: Ask the user to guess a letter and assign this to a variable called guess.
  guess = input("guess the letter ")
  # Step 3. Check that the guess is a single, alphabetical character.
  if len(guess) == 1 and guess.isalpha(): 
    # Step 4. If the guess passes the checks, break out of the loop.
    break
  else: 
    # Step 5: If the guess does not pass the checks, then print a message saying "Invalid letter. Please, enter a single alphabetical character."
    print("Invalid letter. Please, enter a single alphabetical character.")
