import random     #Importing the random Module
answer = random.randint(1, 15)     #assigning a single random value between 1 and 15 inclusive to the variable answer

while True:     #loop runs as long as tries is not greater than or equal to 5
    guess = int(input("Guess: "))   #requests a user to input a guess and converts that value from a string to an integer before assigning it to the variable guess
    if guess == answer:
        print("You win!")  #Prints "You win!" if the guess and answer are the same
        break     #Ends the loop when the condition is met
    else:
        print("Try Again!")  #Displays "You lose!" when all of the above are false 
