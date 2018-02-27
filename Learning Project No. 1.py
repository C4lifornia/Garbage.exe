import random
print ("Hellooooooooo and welcome to Tim's VERY first number guessing game!!!")
print ("Wooooo!!! Alright!")
print ("Oh man this is gonna be so great!")
print("")
print("")
print("")
print("So what's your name, pal?")
name = input()
if name == '':
    print ("Ummm, I asked you for your name?")
    input (name)
else:
    print ("Happy to meet you, " + name + "! I'm your host, Python Trebek!")

print ("So, " + name + ", I need you to type 'E, M, or H' for easy, meadium or hard mode. Got that? Which difficulty would you prefer?")
difficulty = input ()
if difficulty != 'E' or 'M' or 'H':
    print ("Sorry kiddo, I need you to select either 'E, M, or H' for easy, meadium or hard mode. Got that?")
    difficulty = input ()
elif difficulty == E:
    def E():
        answer = random.randint (1, 10)
        print ("Perfect! Now, " + name + ". I'm thinking of a number between 1 and 10. you have 4 guesses to get it right, or else you lose.")
        print ("")
        print ("")
        print ("")
        print ("")
        print ("Ready..?")
        print ("")
        print ("")
        print ("Go!")
        guess = int(input("What is the number I'm thinking of?"))
        if guess != int:
            print ("Sorry, " + name + ". Could you try that again?")
            guess = int(input("What is the number I'm thinking of?"))
        else:
            for answer in range (1, 4):
                if guess < answer:
                    print ("too low! Try again!")
                elif guess > answer:
                    print ("Too high! Try again!")
                else:
                    break
elif difficulty == M:
    def M ():
        answer = random.randint (1, 80)
        print ("Perfect! Now, " + name + ". I'm thinking of a number between 1 and 80. you have 10 guesses to get it right, or else you lose.")
        print ("")
        print ("")
        print ("")
        print ("")
        print ("Ready..?")
        print ("")
        print ("")
        print ("Go!")
        guess = int(input("What is the number I'm thinking of?"))
        if guess != int:
            print ("Sorry, " + name + ". could you try that again?")
            guess = int(input("What is the number I'm thinking of?"))
        else:
            for answer in range (1, 10):
                if guess < answer:
                    print ("too low! Try again!")
                elif guess > answer:
                    print ("Too high! Try again!")
                else:
                    break
elif difficulty == H:
    def H ():
        answer = random.randint (1, 150)
        print ("Perfect! Now, " + name + ". I'm thinking of a number between 1 and 150. you have 20 guesses to get it right, or else you lose.")
        print ("")
        print ("")
        print ("")
        print ("")
        print ("Ready..?")
        print ("")
        print ("")
        print ("Go!")
        guess = int(input("What is the number I'm thinking of?"))
        if guess != int:
            print ("Sorry, " + name + ". could you try that again?")
            guess = int(input("What is the number I'm thinking of?"))
        else:
            for answer in range (1, 20):
                if guess < answer:
                    print ("too low! Try again!")
                elif guess > answer:
                    print ("Too high! Try again!")
                else:
                    break
if guess == answer:
    print ("That's it! You Won! Thanks for playing!")
else:
    print ("Better luck next time! Thanks for playing!")
