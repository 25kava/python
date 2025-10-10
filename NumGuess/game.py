import random
import os
import time
import pickle
os.system('cls' if os.name == 'nt' else 'clear')



userName = input("Enter your name: ").lower()
userFile = f"{userName}.dat"

try:
    with open(userFile, 'rb') as file:
        easyHighScore = pickle.load(file)
        mediumHighScore = pickle.load(file)
        hardHighScore = pickle.load(file)
        password = pickle.load(file)
        print(f"Welcome back, {userName}!")
        for attempt in range(3):
            enteredPassword = input("Please enter your password: ")
            if enteredPassword == password:
                print("Access granted.")
                time.sleep(1)
                break
            else:
                print("Incorrect password. Try again.")
        if enteredPassword != password:
            print("Too many incorrect attempts. Logging in as guest.")
            userName = "guest"
            userFile = f"{userName}.dat"

except FileNotFoundError:
    easyHighScore = "Inf"
    mediumHighScore = "Inf"
    hardHighScore = "Inf"
    password = input("New user detected. Please set a password: ")
    with open(userFile, 'wb') as file:
        pickle.dump(easyHighScore, file)
        pickle.dump(mediumHighScore, file)
        pickle.dump(hardHighScore, file)
        pickle.dump(password, file)

def getHighScores():
    print("Loading high scores...")
    time.sleep(1)
    try:
        with open(userFile, 'rb') as file:
            easyHighScore = pickle.load(file)
            mediumHighScore = pickle.load(file)
            hardHighScore = pickle.load(file)
    except:
        easyHighScore = "Inf"
        mediumHighScore = "Inf"
        hardHighScore = "Inf"
        time.sleep(2)

    return easyHighScore, mediumHighScore, hardHighScore

easyHighScore, mediumHighScore, hardHighScore = getHighScores()

higherLower = ""
upperNum = None


def loop():
    global attempts, i, number_to_guess, easyHighScore, mediumHighScore, hardHighScore, diff, higherLower
    i = 0
    while i < attempts:
        os.system('cls' if os.name == 'nt' else 'clear')
        if higherLower:
            print(higherLower)
        print(f"You have {attempts - i} attempt(s) remaining.")
        try:
            guess = int(input("\nTake a guess: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            time.sleep(1)
            continue

        if guess == number_to_guess:
            os.system('cls' if os.name == 'nt' else 'clear')
            used = i + 1
            print(f"Congratulations! It took you {used} attempts.")
            time.sleep(1)

            # update highscores in memory first
            if diff == "easy":
                if easyHighScore == "Inf" or used < int(str(easyHighScore).split()[0]):
                    easyHighScore = f"{used} attempts"
            elif diff == "medium":
                if mediumHighScore == "Inf" or used < int(str(mediumHighScore).split()[0]):
                    mediumHighScore = f"{used} attempts"
            elif diff == "hard":
                if hardHighScore == "Inf" or used < int(str(hardHighScore).split()[0]):
                    hardHighScore = f"{used} attempts"

            # then save the updated highscores
            with open(userFile, 'wb') as file:
                pickle.dump(easyHighScore, file)
                pickle.dump(mediumHighScore, file)
                pickle.dump(hardHighScore, file)
                pickle.dump(password, file)

            break
        elif guess < number_to_guess:
            higherLower = f"Incorrect! The number is greater than {guess}."
        else:
            higherLower = f"Incorrect! The number is less than {guess}."

        i += 1

    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Game Over! You ran out of attempts.")
        print(f"The number was {number_to_guess}.")

    print(f"\nYour high scores are:\n\nEasy: {easyHighScore}\nMedium: {mediumHighScore}\nHard: {hardHighScore}")
    print("")
    print("Play again? (yes/no)")

    play_again = input(" > ").lower()
    if play_again in ("yes", "y"):
        setup()
    else:
        print(f"Thanks for playing, {userName}!")
        exit(0)


def setup():
    global attempts, number_to_guess, diff, i, higherLower, upperNum
    higherLower = ""
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        diff = input("Choose a difficulty." \
        "\n" \
        "\n" \
        f"1: Easy, 10 attempts, 1 - 100" \
        "\n" \
        f"2: Medium, 15 attempts, 1 - 500" \
        "\n" \
        f"3: Hard, 20 attempts, 1 - 1000" \
        "\n" \
        "\n" \
        "[Type 'easy', 'medium', 'hard' or 'highscore'] : ").strip().lower()
        print("\n")

        if diff == "highscore":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"\nYour (lowest) highscores are:\n\nEasy: {easyHighScore}\nMedium: {mediumHighScore}\nHard: {hardHighScore}")
            input("\nPress Enter to continue...")
            continue

        if diff in ("easy", "1"):
            attempts = 10
            upperNum = 100
            diff = "easy"
            break
        elif diff in ("medium", "2"):
            attempts = 15
            upperNum = 500
            diff = "medium"
            break
        elif diff in ("hard", "3"):
            attempts = 20
            upperNum = 1000
            diff = "hard"
            break
        else:
            print("Invalid selection. Please choose 'easy', 'medium', 'hard' or type 'highscore'.")
            time.sleep(1)
            continue

    number_to_guess = random.randint(1, upperNum)
    loop()


print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100 / 500 / 1000.")
input("Press Enter to start...")
setup()