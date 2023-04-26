#Creating a menu where user chooses the game
print("************************************************") 
print("*                     Menu                     *") 
print("************************************************") 
print("*  1) Rock, Paper, Scissors, Lizard, Spock     *") 
print("*  2) Play Hangman                             *") 
print("*  3) Exit                                     *") 
print("************************************************")

#input to run the user selection
userChoice = int(input("What game would you like to play? "))

#This block code processes the entered choice. A While loop is used so that the sentinel controlled group can execute the Exit option
while userChoice != 3:

#start of game 1:
    if userChoice == 1:

#display of options so players choose their option
        print("____________________________________________________")
        print("Welcome to 'Rock, Paper, Scissors, Lizard, Spock'")
#variables to run in the code which will be later used to display results
        player1score = 0
        player2score = 0
        ties = 0
        games = 0
# using a for loop to run the game 5 times
        for i in range(5):
# correct inputs
            options = ["rock", "paper", "scissors", "lizard", "Spock"]
# the pairs composed by the options, these will help to make more compact the if/elif code block which processes the choices
            win_and_lose_pairs = [("rock", "scissors"), ("rock", "lizard"), ("paper", "rock"), ("paper", "Spock"), ("scissors", "paper"), ("scissors", "lizard"), ("lizard", "Spock"), ("lizard", "paper"), ("Spock", "rock"), ("Spock", "scissors")]
# this code block counts the number of games up to 5
            games += 1
            print("Playing game: ", games)
# user input, numbers were used to indexing the options list and make the input more practical for the user rather than typing words
            print("Please, choose from the following options:")
            print(" --> 0 for Rock\n --> 1 for Paper\n --> 2 for Scissors\n --> 3 for Lizard\n --> 4 for Spock")
            player1 = int(input("Player 1, please enter your choice: "))
            player2 = int(input("Player 2, please enter your choice: "))
# a variable for the choices is created to use it in the conditional statements and to contain the options list index
            p1choice = options[player1]
            p2choice = options[player2]
# the conditional statement that processes the choices. The variables 'ties', 'player1score' and 'player2score' are used here to compile the ties, wins and losses that will be displayed once the 5 games are over
            if p1choice == p2choice:
                result = "It's a tie!"
                ties += 1
            elif (p1choice, p2choice) in win_and_lose_pairs:
                result = "Player 1 wins!"
                player1score += 1
            elif (p2choice, p1choice) in win_and_lose_pairs:
                result = "Player 2 wins!"
                player2score += 1
            else:
                print("Please, enter a valid choice")
# to present the results of each game, a small display is printed
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            print(" -> Player 1 : ", p1choice)
            print(" -> Player 2 : ", p2choice)
            print(" -> Result   : ", result)
            print(" -> Player 1 score: ", player1score)
            print(" -> Player 2 score: ", player2score)
            print(" -> Number of ties: ", ties)
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

            



# code for declaring a winner:


#start of game 2
    elif userChoice == 2:
        pass
    else:
        print("Oops, that option isn't available! Please try again:")
        print("************************************************") 
        print("*                     Menu                     *") 
        print("************************************************") 
        print("*  1) Rock, Paper, Scissors, Lizard, Spock     *") 
        print("*  2) Play Hangman                             *") 
        print("*  3) Exit                                     *") 
        print("************************************************")
        userChoice = int(input("What game would you like to play? "))
