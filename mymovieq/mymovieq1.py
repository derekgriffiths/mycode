#!/usr/bin/env python3

print("Welcome to the 70's & 80's movie questionnaire!")

print("We'd like to ask you a few questions about movies in those two decades.")

print("Which decade do you prefer?")

# Asks the user, which decade they prefer
round = 0
decade = " "
seventy = " "

while round < 4 and decade !="a" and decade !="b":
    decade = input("For the 1970's type 'A'; for the 1980's type 'B':  ")   
    decade = decade.lower()
    round += 1
    if decade == "a":
        print("Great, I also liked the 70's for movies!")
    elif decade == "b":
        print("Awesome! That's my favourite decade in film too!")
    elif round == 4:
        print("Sorry. I think you're having troubles. Please try again later")
    else:
        print("Sorry, that's not one of the options. Please try again.")

if decade == "a":
    print("Of the following four films from the 70's, which one do you prefer?")
    print("1: Star Wars")
    print("2: The Exorcist")
    print("3: All the President's Men")
    print("4: Patton")
    round = 0
    while round < 4 and seventy !="1" and seventy !="2" and seventy !="3" and seventy !="4":
        seventy = input("Pick a number:  1 through 4:  ")
        round += 1
        if seventy == "1":
            print("Star Wars ... George Lucas' greatest accomplishment")
        elif seventy == "2":
            print("The Exorcist ... one of the scariest movies of all time")
        elif seventy == "3":
            print("All the President's Men ... Dustin Hoffman at his best")
        elif seventy == "4":
            print("Patton ... George C. Scott's deserving Oscar")
        elif round == 4:
            print("Sorry. I think you're having troubles. Please try again later.")
        else:
            print("Sorry, please pick a number, 1 through 4")
elif decade == "b":
    print("Of the following four films from the 80's, which one do you prefer?")
    print("1: Back to the Future")
    print("2: Return of the Jedi")
    print("3: Raiders of the Lost Ark")
    print("4: Poltergeist")
    round = 0
    while round < 4 and seventy !="1" and seventy !="2" and seventy !="3" and seventy !="4":
        seventy = input("Pick a number:  1 through 4:  ")
        round += 1
        if seventy == "1":
            print("Back to the Future ... classic!")
        elif seventy == "2":
            print("Jedi ... Lucas' last good movie")
        elif seventy == "3":
            print("Raiders ... one of the greatest!")
        elif seventy == "4":
            print("Poltergeist ... a personal favorite")
        elif round == 4:
            print("Sorry. I think you're having troubles. Please try again later.")
        else:
            print("Sorry, please pick a number, 1 through 4") 

