import random


def get_word():
    lines = open('dict.txt').read().splitlines()
    myline = random.choice(lines)
    return myline


def game_instruction():
    print("""Wordle is a single player game
    A player has to guess a five letter hidden word
    You have six attempts
    Your Progress Guide "✅❌❌✅❕"
    "✅" — letter at that position was guessed correctly
    "❕" — letter at that position is in the hidden word, but in an other position
    "❌" — letter at that position is wrong, and isn't in the hidden word""")


def check_word():
    hidden_word = get_word()
    tries = []
    attempt = 6
    while attempt > 0:
        guess = str(input("Guess the word: "))
        if len(guess) != 5:
            print("The word should consist of 5 letters")
        elif guess in tries:
            print("You already used this word")
        elif guess not in open('dict.txt').read():
            print("No such word, sorry")
        elif guess == hidden_word:
            print("You guessed the word correctly! Congrats! 🕺🕺🕺 ")
            break
        else:
            tries.append(guess)
            attempt = attempt - 1
            print(f"you have {attempt} attempt(s) \n ")
            for char, word in zip(hidden_word, guess):
                    if word in hidden_word and word in char:
                        print(word + " ✅ ")

                    elif word in hidden_word:
                        print(word + " ❕ ")
                    else:
                        print(" ❌ ")
            if attempt == 0:
                print("Ooops! You lost. The hidden word was", '"'+hidden_word+'"')


def main():
    game_instruction()
    check_word()


if __name__ == "__main__":
    main()
