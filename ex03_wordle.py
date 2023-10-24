"""A word game with 6 turns to guess the secret word!"""

secret_word = "codes"


def contains_char(string_one: str, character_search: str) -> bool:
    """Outputs whether if a single character of the second string is found on any index of the first string."""
    assert len(character_search) == 1
    i: int = 0  # Index for the while loop in contains_char
    result: bool
    while i < len(string_one):
        if (string_one[i] == character_search):
            result = True
            return result
        else:
            result = False
        i += 1
    return result


def emojified(secret_word: str, word_guess: str) -> str:
    """Returns an emoji string that indicates matching letters"""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    assert len(secret_word) == len(word_guess)
    idx: int = 0  # Index for the emojified while loop
    boxes_string: str = ""
    while idx < len(word_guess):
        if contains_char(word_guess, secret_word[idx]) == True:  # calling the contains_char function
            if word_guess[idx] == secret_word[idx]:
                boxes_string += GREEN_BOX  # if it's True and in the right place, a green box is added to boxes_string
            else:
                boxes_string += YELLOW_BOX  # if it's True but in the wrong place then it will add a yellow box to the boxes_string
        else:
            boxes_string += WHITE_BOX  # if character is not in the word, white box is added to boxes_string
        idx += 1
    return boxes_string


def input_guess(guess_length: int) -> str:
    """This is the input to enter the user into the main game."""
    player_input: str = input(f"Enter a {guess_length} character word: ")
    while len(player_input) != guess_length:
        player_input = input(f"That wasn't {guess_length} chars! Try again: ")
    return player_input


def main() -> None:
    """The entrypoint of the program and main game loop."""
    idx_2: int = 1
    playing: bool = True
    while idx_2 <= 6 and playing is True:  # we want the game to have six tries
        print(f"=== Turn {idx_2}/6 ===")
        player_guess: str = input_guess(len(secret_word))
        print(emojified(player_guess, secret_word))
        if secret_word == player_guess:
            playing = False
            print(f"You won in {idx_2}/6 turns!")
            return
        idx_2 += 1
    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()
