from hangman import display_guessed, update_guessed, is_word_guessed


def test_display_guessed():
    word = "cambodia"
    guessed1 = {"a", "m", "d"}
    guessed2 = {"a", "m", "x"}
    guessed3 = {"a", "m", "1"}

    assert display_guessed(word, guessed1) == "_ a m _ _ d _ a"
    assert display_guessed(word, guessed2) == "_ a m _ _ _ _ a"
    assert display_guessed(word, guessed3) == "_ a m _ _ _ _ a"


def test_update_guessed():
    guess1 = "5"
    guess2 = "o"
    guess3 = "K"

    guessed = {"n", "y"}

    assert update_guessed(guessed, guess1) == {"5", "n", "y"}
    assert update_guessed(guessed, guess2) == {"5", "n", "y", "o"}
    assert update_guessed(guessed, guess3) == {"K", "n", "y", "5", "o"}


def test_word_guessed():
    # ignore upper and lower case
    word = "Surabaya".casefold()
    word2 = "Tokio".casefold()

    guessed = {"o", "a", "s"}
    guessed2 = {"o", "i", "t", "k"}

    assert is_word_guessed(word, guessed) is False
    assert is_word_guessed(word2, guessed2) is True
