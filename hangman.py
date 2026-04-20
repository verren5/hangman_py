import random
from collections import Counter

def choose_word(word):
    #Casefold to ignore upper and lowercase!
    return random.choice(word).casefold()

def update_guessed(guessed, guess):
    # input all the letter appear in the word. e.g if apple has double p then guessed will have pp 
    guessed.add(guess)
    return guessed
    
def display_guessed(word, guessed):
    result = []
    for letter in word:
        if letter in guessed:
            result.append(letter)
        else:
            result.append("_")
    return " ".join(result)

def is_word_guessed(word, guessed):
    return all( letter in guessed for letter in word)

