from words import words
from random import choice, sample
from display_utility import *
from wordle import check_word


def filter_word_list(word_list, clue_list):
    """
    This function filters out the words in the word list to return a new word list containing only the words in the input
    word list which could be the secret word.
    :param word_list: a list of words
    :param clue_list: a list of tuples containing the user guess (string) and the clues (list)
    :return: returns a new word list containing only the words in the input word list which could be the secret word.

    """
    if not clue_list:
        return word_list

    # Capitalize the input word_list
    upper_word = [k.upper() for k in word_list]
    possible_word = ""
    possible_word_list = []

    # Loop within the number of guesses taken so far
    for j in range(len(upper_word)):
        count = 0
        for i in range(len(clue_list)):
            # Compare the generated clue of words in the word list with the all the clues of user's previous guesses

            if check_word(upper_word[j], clue_list[i][0]) == clue_list[i][1]:
                # Keeps track of the possible word that matches with all the clues of user's previous guesses
                possible_word = upper_word[j]
                count += 1

        # Only append the possible words that matches with all the clues of previous guesses into the list
        if count == len(clue_list):
            possible_word_list.append(possible_word)


    possible_word_list = [l.lower() for l in possible_word_list]

    return possible_word_list


def print_clues(guess_list):
    """
    :param guess_list: a list of tuples containing the user guess (string) and the clues (list)
    :return: no return
    """
    for i in range(len(guess_list)):
        for j in range(5):
            if guess_list[i][1][j] == "green":
                green(guess_list[i][0][j])  # Print green clue
            elif guess_list[i][1][j] == "yellow":
                yellow(guess_list[i][0][j])  # Print yellow clue
            else:
                grey(guess_list[i][0][j])  # Print grey clue
        print("")  # Prompt and clue will be in new line


if __name__ == "__main__":
    filtered_word = []
    upper_words = []
    guess_record = []
    new_word_list = []
    guess = 0

    # Capitalize word list and store them in a new list
    for w in range(len(words)):
        upper_words.append(words[w].upper())
    secret_word = choice(upper_words)  # A secret word is picked at random

    while guess < 6:
        # Prompt user for guess
        while True:
            user_guess = input("> ")
            user_guess = user_guess.upper()  # Capitalize user input

            # Continuously prompts user for guess if guess is invalid
            if user_guess not in upper_words or len(user_guess) != 5:
                continue
            else:
                break

        # Check word function called to generate output clue according to guess
        clues = check_word(secret_word, user_guess)
        # Append tuples of user guesses and respective clues into guess_record list
        guess_record.append((user_guess, clues))
        print_clues(guess_record)  # Display wordle characters

        # Generate possible words that match all the clues of previous guesses
        filtered_word = filter_word_list(upper_words, guess_record)

        guess += 1

        print(len(filtered_word), "words possible:")
        if len(filtered_word) <= 5:
            for k in filtered_word:
                print(k)
        else:
            # Assign the randomly selected 5 words from the possible word list into a new list
            five_words = sample(filtered_word, 5)

            for five in five_words:
                print(five)

        # Ends the game if user guesses the secret word
        if user_guess == secret_word:
            break

    print("Answer:", secret_word)
