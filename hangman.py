import random

def choose_word(word):
    # Casefold to ignore upper and lowercase!
    return random.choice(word).casefold()

def update_guessed(guessed, guess):
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

