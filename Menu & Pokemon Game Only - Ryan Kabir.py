# By submitting this assignment, I agree to the following:
#	"Aggies do not lie, cheat, or steal, or tolerate those who do."
#	"I have not given or received any unauthorized aid on this assignment."
#
# Names:	Ryan Kabir
#		    Hannah Roh
#		    Anna Thomas
# Section:	571
# Assignment:	ENGR 102 - Final Project
# Date:		12 06 21
#

# takes the user's preferred name for greeting
username = input("What should we call you?\n")

############### Start of the game's main menu ###############
def gamemenu():
    """This is the starting point of all three games that each game will quit back to and that will
    launch each game."""

    # initialize while loop that will serve as the menu
    ans = True
    while ans:

        # first print statement is a welcome with options to select each game
        print("\nWelcome to the menu,", username + "!" +
              """
Choose a game you would like to play:
    1. Play "The Guessing Game"
    2. Play "The Marble Game"
    3. Play "Who's that Pokemon?"
    """)

        # if-elif-else block that performs each of the menu options
        choice = input("To choose, simply type in a number with no special formatting.\n")
        if choice == "1":
            guessinggame()
            break
        elif choice == "2":
            marblegame()
            break
        elif choice == "3":
            pikachu()
            break
        else:
            print("\nPlease select a valid option.")


############### Start of the "Who's that Pokemon Game" ###############
import random
def pikachu():
    """This is the Pokemon 20 questions style guessing game."""
    # this will provide the instructions and the intro to the Pokemon game
    print("\nWelcome to \"Who\'s that Pokemon?\"\n")
    print("Instructions:\nTo play this game, you will be presented 6 different species of Pokemon"
          "\nand asked to select whichever you please. To do so, type in the name of the Pokemon you would"
          "\nlike to choose, then answer the program's true or false questions until the program guesses your"
          "\nPokemon correctly. If the program guesses correctly, please select the according option"
          "\nand the game will conclude. If the program runs out of questions before guessing your Pokemon,"
          "\nyou win!")

    # this while loop will allow the user to exit back to the game menu if they so choose
    try:
        play = True
    except:
        play = False
    while play:
        play = input("\nWould you like to play? If so, enter 'Yes'. Otherwise, enter 'Quit' to exit back to the main menu.\n")
        if play == 'Quit' or play == 'quit':
            return gamemenu()
        elif play == 'Yes' or play == 'yes':
            play = False
        else:
            print("Please respond with a valid option.")
    print("")

    # if the user continues to play the actual game content will begin here with a list of Pokemon to choose from
    pokelist = ['Pikachu', 'Charizard', 'Dragonite', 'Togepi', 'Pidgeot', 'Suicune']
    pokechoice = True
    while pokechoice:
        print("Choose from the following Pokemon: (Simply type their name)")
        print("- Pikachu\n"
              "- Charizard\n"
              "- Dragonite\n"
              "- Togepi\n"
              "- Pidgeot\n"
              "- Suicune")

        # making sure the pokemon that they choose is on the list, otherwise prompting with a classic quote
        # from the Pokemon games, telling them to choose a different option (little easter egg)!
        poke = input()
        if poke in pokelist:
            print("\nI choose you, "+poke+"!\n")
            break
        else:
            print("\nProfessor Oak's words echoed... There's a time and place for everything, but not now.")

# Beginning of the guessing game dialogue
    print("Hello? Is this thing working?")
    print("...")
    print("Ah, There we are.\n")
    print("Hello", username+"!"+" My name is Professor Oak, many people just call me the Pokemon Professor.")
    print("I am here today to guess your Pokemon! Please do me the favor of answering honestly")
    print("with 'Yes' or 'No' according to my questions! If you are unsure or would like to stop playing")
    print("you have those options as well.\n")

# Questions
    q1 = "Can your Pokemon roam the sky?"
    q2 = "Was or is your Pokemon able to evolve?"
    q3 = "Is your Pokemon fully evolved?"
    q4 = "Does your Pokemon have feathers?"
    q5 = "Does your Pokemon have a tail?"
    q6 = "Is your Pokemon weak to electricity?"
    q7 = "Is your Pokemon weak to ice?"
    q8 = "Is your Pokemon resemble a dragon?"
    q9 = "Is your Pokemon a legendary Pokemon?"
    q10 = "Does your Pokemon walk on only two legs?"

# List of guesses for each question
    l1 = ["Charizard", "Dragonite", "Pidgeot"]
    l2 = ["Charizard", "Pidgeot", "Dragonite", "Pikachu", "Togepi"]
    l3 = ["Charizard", "Pidgeot", "Dragonite"]
    l4 = ["Pidgeot", "Togepi"]
    l5 = ["Charizard", "Dragonite", "Pidgeot"]
    l6 = ["Charizard", "Dragonite", "Pidgeot", "Suicune"]
    l7 = ["Dragonite", "Pidgeot"]
    l8 = ["Dragonite", "Charizard"]
    l9 = ["Suicune"]
    l10 = ["Charizard", "Dragonite", "Togepi", "Pidgeot"]
# Guesses
    r1 = "Is your Pokemon..."+str(random.choice(l1))+"? (Yes or No)"
    r2 = "Is your Pokemon..."+str(random.choice(l2))+"? (Yes or No)"
    r3 = "Is your Pokemon..."+str(random.choice(l3))+"? (Yes or No)"
    r4 = "Is your Pokemon..."+str(random.choice(l4))+"? (Yes or No)"
    r5 = "Is your Pokemon..."+str(random.choice(l5))+"? (Yes or No)"
    r6 = "Is your Pokemon..."+str(random.choice(l6))+"? (Yes or No)"
    r7 = "Is your Pokemon..."+str(random.choice(l7))+"? (Yes or No)"
    r8 = "Is your Pokemon..."+str(random.choice(l8))+"? (Yes or No)"
    r9 = "Is your Pokemon..."+str(random.choice(l9))+"? (Yes or No)"
    r10 = "Is your Pokemon..."+str(random.choice(l10))+"? (Yes or No)"

# Question bank with each question and question dictionary with each set of guesses
    questionbank = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
    questiondict = {0: r1, 1: r2, 2: r3, 3: r4, 4: r5, 5: r6, 6: r7, 7: r8, 8: r9, 9: r10}
# For loop that runs each question and guess response until the correct answer is guessed or all
# questions are asked.
    for question in questionbank:
        n = random.randint(0, 9)
        print(questionbank[n])
        print(""
              "1 - 'Yes'\n"
              "2 - 'No'\n"
              "3 - 'I don't know\n"
              "4 - You already asked this!\n"
              "5 - I want to stop playing."
              "")
        qresponse = input('') # Is this your pokemon response
        if qresponse == '1': # If yes
            print(questiondict[n]) # Guesses Pokemon
            isit = input("") # Is the guess correct
            if isit == 'Yes' or isit == 'yes' or isit == 'y' or isit == "Y":
                print("Ha ha! Looks like I won this round, "+ username+". Want to play again?")
                playagain = input("")
                if playagain == 'Yes' or playagain == 'yes' or playagain == 'y' or playagain == "Y":
                    return pikachu()
                else:
                    print("Thank you for playing, hope you play again!")
                    return gamemenu()
            else:
                continue
        elif qresponse == '2': # If no
            print("Is your Pokemon..."+random.choice(pokelist)+"?")
            isit = input("")  # Is the guess correct
            if isit == 'Yes' or isit == 'yes' or isit == 'y' or isit == "Y":
                print("Ha ha! Looks like I won this round, " + username + ". Want to play again?")
                playagain = input("")
                if playagain == 'Yes' or playagain == 'yes' or playagain == 'y' or playagain == "Y":
                    return pikachu()
                else:
                    print("Thank you for playing, hope you play again!")
                    return gamemenu()
            else:
                continue
        elif qresponse == '3': # If you don't know
            print("That's okay, I'll ask another question!")
        elif qresponse == '4': # If they already asked this
            print("My bad! If it makes you feel better, I can't quite remember my own grandson's name!")
        elif qresponse == '5': # If you want to stop playing
            print("Thank you for playing, hope you play again!")
            return gamemenu()
        else:
            print("Please select a valid response (1 through 5).")
    print("Looks like you won! You are quite the Pokemon Master. Thank you for playing!")
    return gamemenu()


############### Start of "The Guessing Game" ###############
def guessinggame():
    print("\nThis is a guessing game in which the computer generates a number"
          "\nand the user attempts to guess it using hints provided by the computer, this will implement "
          "\nan if-elif-else statement as well as various other functions to validate the user’s response"
          "\nversus the random number generated by the program")

    print("\nTo stop playing the game at any time, type in 'Quit'.")

    # a player against a computer
    import random
    n = random.randint(1, 99) #this is the range: from 1 to 99

    # ask the player for their name and ask them to guess
    print("\nHello", username) # a brief introduction and explanation
    print("You will be playing the guessing game.")
    print("I will choose a number and you will try to guess it.")

    try:
        guess = int(input("\nEnter an integer from 1 to 99:\n"))
        guesscount = 0
        listofguesses = []
        while n != "guess":
            if guess < n:
                print("Nope! Too low") #if the guess is less than the secret number, the following response will be printed
                guess = int(input("Enter an integer from 1 to 99: "))
                guesscount += 1
                listofguesses += str(guess)
            elif guess > n:
                print("Try again. It's too high")
                guess = int(input("Enter an integer from 1 to 99: "))
                guesscount += 1
                listofguesses += str(guess)
            else:
                guesscount += 1
                listofguesses += str(guess)
                print("Congratulations, you got it right!")
                print("Thank you for playing the guessing game!")
                print("It took you", guesscount, "guesses to guess the number!")
                print("Here were your guesses (10 will be shown as 1, 0 separately):", print(listofguesses))
                break
    except ValueError:
        print("Please enter a valid input")
        guessinggame()
    gamemenu()
############### Start of the "Marbles" ###############
def marblegame():
    # a player against a computer
    # ask the player for their name and ask them to guess
    import random
    print("Hello " + username) # a brief introduction and explanation
    print("You will be playing The Marble Game!")
    print("You will start out with ten marbles.")
    print("Enter an integer and I will try to guess if it is even or odd.")
    print("If I am correct I will take a marble. If I am wrong you get a marble.")
    print("When you run out, you lose.")

    print("\nIf you would like to exit the game at any point, type 404.")

    try:
        # start w ten marbles
        marbles = 10
        turncountlist = []
        while marbles > 0:
            guess = int(input("Enter an integer: "))
            turncountlist += str("1")
            # computer guesses in terms of 1 or 2
            n = random.randint(1, 2)
            if n==1 and guess % 2 == 0:
                print("The number is even!")
                print("I was correct!")
                marbles-=1
            elif n==1 and guess % 2 != 0:
                print("The number is even!")
                print("I was wrong!")
                marbles+=1
            elif n==2 and guess % 2 != 0:
                print("The number is odd!")
                print("I was correct!")
                marbles-=1
            else:
                print("The number is odd!")
                print("I was wrong!")
                marbles+=1
            print("You have", marbles, "marbles.")
            if marbles >= 20:
                print("You reached 20 marbles! You win!")
                print("It took you:", turncountlist, "turns!")
            break
        # out of marbles
        if marbles == 0:
                print("You're out of marbles! I win!")
                print("It took you:", str(len(turncountlist)), "turns!")
    except ValueError:
        print("Thank you for playing!")
        gamemenu()

# Runs the game
gamemenu()