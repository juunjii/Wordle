from words import words
from random import choice
from display_utility import *


def check_word(secret, guess):
    """
    The function takes a word and generates the output clue.

    :param secret: secret word for the Wordle game
    :param guess: guess input by the user
    :return: length-5 list containing the strings ”grey”, ”yellow”, and ”green”.
    """

    clue = ["grey"] * 5
    secret_list = list(secret)  # Converts the string secret into a list

    # Check for letters that receive the green clue in the guess
    for i, letter in enumerate(guess):
        if letter == secret_list[i]:
            secret_list[i] = "!"  # Letters of guess that are in the right position will be marked with "!"
            clue[i] = "green"

            # Check for letters that receive the yellow clue in the guess
    for i in range(len(guess)):
        for j in range(len(secret_list)):
            # Ensures that yellow does not overwrite existing green
            if guess[i] == secret_list[j] and secret_list[i] != "!":
                secret_list[j] = "?"  # To mark the letter in the secret_list when the guess has that letter but in
                # the wrong position
                clue[i] = "yellow"
                break

    return clue


def known_word(clues):
    """
    This functions keep track of which positions have seen green clues, where
    positions which have not seen a green clue are presented as _ and positions
    which have received a green clue are the known letters.
    :param clues: a list containing a record of guesses (string) taken and clues(s received so-far in the form of tuples
    :return: a String indicating what we know about the secret word according to green hints seen so-far
    """
    known_letters = ["_"] * 5  # List initialized to [_____]

    # Letters that receives green clue will be shown
    for i in range(len(clues)):
        for j in range(5):
            if clues[i][1][j] == "green":
                known_letters[j] = clues[i][0][j]

    known_word_string = ''.join(known_letters)  # Converts the list to string

    return known_word_string


def no_letters(clues):
    """
    This function helps with "basic record-keeping" for the end-user of the code, by telling the user
    which letter guessed so far is not in the word according to the grey hints.
    :param clues:  a list containing a record of guesses taken and clues received so-far.
    :return: a String indicating which letters we know are not in the word according to grey hints seen so-far.

    """
    absent_letters = set()  # No duplicates are allowed in set

    # Add letters that receive grey clue into a set
    for i in range(len(clues)):
        for j in range(5):
            if clues[i][1][j] == "grey" and clues[i][0][j] not in yes_letters(clues):
                absent_letters.add(clues[i][0][j])

    no_letters_list = list(absent_letters)  # Convert the set to list
    no_letters_list.sort()  # Sort the list
    no_letters_string = "".join(no_letters_list)  # Convert the list to string

    return no_letters_string


def yes_letters(clues):
    """
    This function helps with "basic record-keeping" for the end-user of the code, by telling the user
    which letter guessed so far are in the word based on the yellow and green hints.
    (Yellow - indicates wrong position but in the word)
    (Green - indicates right position in the word)
    :param clues: a list containing a record of guesses taken and clues received so-far
    :return: string indicating what letters are in the word based on yellow and green hints we’ve seen so-far.
    """
    letters_in_word = set()  # No duplicates are allowed in set

    # Add letters that receive green and yellow clue into a set
    for i in range(len(clues)):
        for j in range(5):
            if clues[i][1][j] == "green":
                letters_in_word.add(clues[i][0][j])
            if clues[i][1][j] == "yellow":
                letters_in_word.add(clues[i][0][j])

    yes_letters_list = list(letters_in_word)  # Convert the set to list
    yes_letters_list.sort()  # Sort the list
    yes_letters_string = "".join(yes_letters_list)  # Convert the list to string

    return yes_letters_string


def print_clues(guess_list):
    """
    This function takes the list of user guess and the clue generated, and displays the wordle characters
    according to the clues (green, yellow, grey) given.
    :param guess_list: a list of tuples containing the user guess (string) and the clues (list)
    :return: no return
    """

    for i in range(len(guess_list)):
        for j in range(5):
            if guess_list[i][1][j] == "green":
                green(guess_list[i][0][j])  # Prints letter that receive green clue
            elif guess_list[i][1][j] == "yellow":
                yellow(guess_list[i][0][j])  # Prints letter that receive yellow clue
            else:
                grey(guess_list[i][0][j])  # Prints letter that receive grey clue
        print("")  # Prompt and clue will be in new line


if __name__ == "__main__":
    upper_words = []
    guess_record = []
    guess = 0
    # Capitalize word list and store them in a new list
    for w in range(len(words)):
        upper_words.append(words[w].upper())
    secret_word = choice(upper_words)  # A secret word is picked at random
    print("Known: _____")
    print("Green/Yellow Letters: ")
    print("Grey Letters: ")

    # Prompt user for input (6 guesses)
    while guess < 6:
        # Continuously prompts if user enters invalid input
        while True:
            user_guess = input("> ")
            user_guess = user_guess.upper()

            if user_guess not in upper_words or len(user_guess) != 5:
                continue
            else:
                break

        # Check word function called to generate output clue according to guess
        clues = check_word(secret_word, user_guess)
        # Append tuples of user guesses and respective clues into guess_record list
        guess_record.append((user_guess, clues))
        print("Known:", known_word(guess_record))
        print("Green/Yellow Letters:", yes_letters(guess_record))
        print("Grey Letters:", no_letters(guess_record))
        print_clues(guess_record)  # Display wordle characters

        guess += 1

        # Ends the game if user guesses the secret word
        if user_guess == secret_word:
            break

    print("Answer:", secret_word)
