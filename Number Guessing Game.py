import random
startPoint = int(input("Enter a starting value: "))
endPoint = int(input("Enter an end point: "))

def randomNumber():
    counter = 1
    x = random.randint(startPoint, endPoint)
    while(True):
        guess = int(input("Guess the number: "))
        
        if guess > endPoint or guess < startPoint:
            print("enter a number between " + str(startPoint) + " and " + str(endPoint))
        
        if guess > x:
            print("you guess too high")
        
        if guess < x:
            print("You guessed too low")
            
        if guess == x:
            return "Correct the number was " + str(x) + ", You guessed " + str(counter) + " times"
        else:
            print("Guess again")
            counter += 1

print(randomNumber())