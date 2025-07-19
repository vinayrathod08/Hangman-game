import random

# Hangman ASCII art dictionary
hangman_art = {
    0: (" ", " ", " "),
    1: (" O ", " ", " "),
    2: (" O ", " | ", " "),
    3: (" O ", "/| ", " "),
    4: (" O ", "/|\\", " "),
    5: (" O ", "/|\\", "/  "),
    6: (" O ", "/|\\", "/ \\"),
}

# Words for the hangman game
words = {"apple", "orange", "banana", "coconut", "pineapple"}

def display_man(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
        print(line)

def display_hint(hint):
    print(' '.join(hint))

def display_answer(answer):
    print(answer)

def main():
    answer = random.choice(list(words))
    hint = ["_" for _ in answer]
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single alphabetical character.")
            continue

        if guess in guessed_letters:
            print(f"{guess} is already guessed.")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("You Win!")
            is_running = False

        elif wrong_guesses >= 6:
            display_man(wrong_guesses)
            display_answer(answer)
            print("You Lose!")
            is_running = False

if __name__ == "__main__":
    main()
