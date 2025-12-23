import random

#    generate a random number
num = random.randint(1, 100)

while True :
#    ask user to guess a number
    guess = int(input("guess a number between 1 and 100..." ))
    
    if (guess > num) :
        print ("Too High")
    elif (guess < num) :
        print ("Too Low")
    elif (guess > 100 or guess < 1) :
        print ("Outside linmit")
    elif (guess == num) :
        print ("Congratulations! You guessed the number")
        break