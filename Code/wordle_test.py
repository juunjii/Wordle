from wordle import check_word, known_word, yes_letters, no_letters
from words import words
from easy_wordle import filter_word_list

# Test for function check_word
print("------------------------------")
print("Test for function check_word")
print("------------------------------")
print("1. check for guess = secret")
print("Guess: rossa")
print(check_word("rossa", "rossa"))  # ["green", "green", "green", "green", "green"]
print("\n2. check for grey")
print("Guess: rosst")
print(check_word("rossa", "rosst"))  # ["green", "green", "green", "green", "grey"]
print("\n3. check for yellow")
print("Guess: orssa")
print(check_word("rossa", "orssa"))  # ["yellow", "yellow", "green", "green", "green"]
print("\n4. check for green over yellow [once all green, no yellow, instead will be grey]")
print("Guess: sssss")
print(check_word("rossa", "sssss"))  # ["grey", "grey", "green", "green", "grey"]
print("\n5. check for one letter's hint, hint only the first letter yellow [first o should be yellow only]")
print("Guess: okooo")
print(check_word("rossa", "okooo"))  # ["yellow", "grey", "grey", "grey", "grey"]
print("\n6. check for two letter hints, wrong position = yellow; correct = green")
print("Guess: rsksa")
print(check_word("rossa", "rsksa"))  # ["green", "yellow", "grey", "green", "green"]
print("\n7. check for hints for two letters positioned incorrectly [both of the letters should be yellow]")
print("Guess: sskka")
print(check_word("rossa",
                 "sskka"))  # ["yellow", "yellow", "grey", "grey", "green"]
# print("\n")
# print("\n")
print("\n8. Another check, secret: robor")
print("Guess: reorg")
print(check_word("robor",
                 "reorg"))  # ["green", "grey", "yellow", "yellow", "grey"]

# Test for function known_word
print("\n------------------------------")
print("Test for function known_word")
print("------------------------------")
print("Secret Word: BIERS")
print("Clues so far from guesses")
print("1st guess")
print(known_word([('RADIO', ['yellow', 'grey', 'grey', 'yellow', 'grey'])]))  # _____
print("2nd guess")
print(known_word(
    [('RADIO', ['yellow', 'grey', 'grey', 'yellow', 'grey']),
     ('ENNUI', ['yellow', 'grey', 'grey', 'grey', 'yellow'])]))  # _____
print("3rd guess")
print(known_word(
    [('RADIO', ['yellow', 'grey', 'grey', 'yellow', 'grey']), ('ENNUI', ['yellow', 'grey', 'grey', 'grey', 'yellow']),
     ('IRKED', ['yellow', 'yellow', 'grey', 'yellow', 'grey'])]))  # _____
print("4th guess")
print(known_word(
    [('RADIO', ['yellow', 'grey', 'grey', 'yellow', 'grey']), ('ENNUI', ['yellow', 'grey', 'grey', 'grey', 'yellow']),
     ('IRKED', ['yellow', 'yellow', 'grey', 'yellow', 'grey']),
     ('FIERY', ['grey', 'green', 'green', 'green', 'grey'])]))  # _IER_
print("5th guess")
print(known_word(
    [('RADIO', ['yellow', 'grey', 'grey', 'yellow', 'grey']), ('ENNUI', ['yellow', 'grey', 'grey', 'grey', 'yellow']),
     ('IRKED', ['yellow', 'yellow', 'grey', 'yellow', 'grey']), ('FIERY', ['grey', 'green', 'green', 'green', 'grey']),
     ('TIERS', ['grey', 'green', 'green', 'green', 'green'])]))  # _IERS
print("6th guess")
print("Not utilized as secret will be printed on the 6th guess regardless of correctness")


# Test for function no_letters
print("\n------------------------------")
print("Test for function no_letters")
print("------------------------------")

lst1 = [('RADIO', ['yellow', 'grey', 'grey', 'yellow', 'grey'])]
print("")
print("No Letters:", no_letters(lst1))

lst2 = [('RADIO', ['yellow', 'grey', 'grey', 'yellow', 'grey']),
        ('ENNUI', ['yellow', 'grey', 'grey', 'grey', 'yellow'])]
print("")
print("No Letters:", no_letters(lst2))

lst3 = [('RADIO', ['yellow', 'grey', 'grey', 'yellow', 'grey']),
        ('ENNUI', ['yellow', 'grey', 'grey', 'grey', 'yellow']),
        ('IRKED', ['yellow', 'yellow', 'grey', 'yellow', 'grey'])]
print("")
print("No Letters:", no_letters(lst3))

lst4 = [('RADIO', ['yellow', 'grey', 'grey', 'yellow', 'grey']),
        ('ENNUI', ['yellow', 'grey', 'grey', 'grey', 'yellow']),
        ('IRKED', ['yellow', 'yellow', 'grey', 'yellow', 'grey']),
        ('FIERY', ['grey', 'green', 'green', 'green', 'grey'])]
print("")
print("No Letters:", no_letters(lst4))

lst5 = [('RADIO', ['yellow', 'grey', 'grey', 'yellow', 'grey']),
        ('ENNUI', ['yellow', 'grey', 'grey', 'grey', 'yellow']),
        ('IRKED', ['yellow', 'yellow', 'grey', 'yellow', 'grey']),
        ('FIERY', ['grey', 'green', 'green', 'green', 'grey']), ('TIERS', ['grey', 'green', 'green', 'green', 'green'])]
print("")
print("No Letters:", no_letters(lst5))

lst6 = [('RADIO', ['yellow', 'grey', 'grey', 'yellow', 'grey']),
        ('ENNUI', ['yellow', 'grey', 'grey', 'grey', 'yellow']),
        ('IRKED', ['yellow', 'yellow', 'grey', 'yellow', 'grey']),
        ('FIERY', ['grey', 'green', 'green', 'green', 'grey']), ('TIERS', ['grey', 'green', 'green', 'green', 'green']),
        ('PIERS', ['grey', 'green', 'green', 'green', 'green'])]
print("")
print("No Letters:", no_letters(lst6))

# Test for function yes_letters
print("\n------------------------------")
print("Test for function yes_letters")
print("------------------------------")

print("1st guess")
print(yes_letters([('RADIO', ['yellow', 'grey', 'grey', 'yellow', 'grey'])]))  # IR
print("2nd guess")
print(yes_letters(
    [('RADIO', ['yellow', 'grey', 'grey', 'yellow', 'grey']),
     ('ENNUI', ['yellow', 'grey', 'grey', 'grey', 'yellow'])]))  # EIR
print("3rd guess")
print(yes_letters(
    [('RADIO', ['yellow', 'grey', 'grey', 'yellow', 'grey']), ('ENNUI', ['yellow', 'grey', 'grey', 'grey', 'yellow']),
     ('IRKED', ['yellow', 'yellow', 'grey', 'yellow', 'grey'])]))  # EIR
print("4th guess")
print(yes_letters(
    [('RADIO', ['yellow', 'grey', 'grey', 'yellow', 'grey']), ('ENNUI', ['yellow', 'grey', 'grey', 'grey', 'yellow']),
     ('IRKED', ['yellow', 'yellow', 'grey', 'yellow', 'grey']),
     ('FIERY', ['grey', 'green', 'green', 'green', 'grey'])]))  # EIR
print("5th guess")
print(yes_letters(
    [('RADIO', ['yellow', 'grey', 'grey', 'yellow', 'grey']), ('ENNUI', ['yellow', 'grey', 'grey', 'grey', 'yellow']),
     ('IRKED', ['yellow', 'yellow', 'grey', 'yellow', 'grey']), ('FIERY', ['grey', 'green', 'green', 'green', 'grey']),
     ('TIERS', ['grey', 'green', 'green', 'green', 'green'])]))  # EIRS

# Test for function filter_word_list
print("\n------------------------------")
print("Test for function filter_word_list")
print("------------------------------")

print("1st guess")
print(filter_word_list(words, [('RADIO', ['yellow', 'grey', 'grey', 'yellow', 'grey'])]))
filtered_word_list = filter_word_list(words, [('RADIO', ['yellow', 'grey', 'grey', 'yellow', 'grey'])])
print(len(filtered_word_list))
print("2nd guess")
print(filter_word_list(
    filtered_word_list, [('RADIO', ['yellow', 'grey', 'grey', 'yellow', 'grey']),
     ('ENNUI', ['yellow', 'grey', 'grey', 'grey', 'yellow'])]))
filtered_word_list = filter_word_list(filtered_word_list, [('RADIO', ['yellow', 'grey', 'grey', 'yellow', 'grey']),
     ('ENNUI', ['yellow', 'grey', 'grey', 'grey', 'yellow'])])
print(len(filtered_word_list))
print("3rd guess")
print(filter_word_list(filtered_word_list,
    [('RADIO', ['yellow', 'grey', 'grey', 'yellow', 'grey']), ('ENNUI', ['yellow', 'grey', 'grey', 'grey', 'yellow']),
     ('IRKED', ['yellow', 'yellow', 'grey', 'yellow', 'grey'])]))
filtered_word_list = filter_word_list(filtered_word_list,[('RADIO', ['yellow', 'grey', 'grey', 'yellow', 'grey']), ('ENNUI', ['yellow', 'grey', 'grey', 'grey', 'yellow']),
     ('IRKED', ['yellow', 'yellow', 'grey', 'yellow', 'grey'])])
print(len(filtered_word_list))
print("4th guess")
print(filter_word_list(filtered_word_list,
    [('RADIO', ['yellow', 'grey', 'grey', 'yellow', 'grey']), ('ENNUI', ['yellow', 'grey', 'grey', 'grey', 'yellow']),
     ('IRKED', ['yellow', 'yellow', 'grey', 'yellow', 'grey']),
     ('FIERY', ['grey', 'green', 'green', 'green', 'grey'])]))
filtered_word_list = filter_word_list(filtered_word_list,[('RADIO', ['yellow', 'grey', 'grey', 'yellow', 'grey']), ('ENNUI', ['yellow', 'grey', 'grey', 'grey', 'yellow']),
     ('IRKED', ['yellow', 'yellow', 'grey', 'yellow', 'grey']),
     ('FIERY', ['grey', 'green', 'green', 'green', 'grey'])])
print(len(filtered_word_list))
print("5th guess")
print(filter_word_list(filtered_word_list,
    [('RADIO', ['yellow', 'grey', 'grey', 'yellow', 'grey']), ('ENNUI', ['yellow', 'grey', 'grey', 'grey', 'yellow']),
     ('IRKED', ['yellow', 'yellow', 'grey', 'yellow', 'grey']), ('FIERY', ['grey', 'green', 'green', 'green', 'grey']),
     ('TIERS', ['grey', 'green', 'green', 'green', 'green'])]))
