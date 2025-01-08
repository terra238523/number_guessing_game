import random
from ascii import get_fonts

personalities = {
    "default": {
        "intro": "hey! i'm thinking of a number between {min_number} and {max_number}. can you guess it?",
        "help": "type 'help' for every command",
        "too_low": "that's too low!",
        "too_high": "that's too high!",
        "congrats": "congratulations! you guessed the number! it took you {attempts} attempts!",
        "invalid": "enter a valid number.",
    },
    "rude": {
        "intro": "hey dumbass. im thinking of a number between {min_number} and {max_number}. guess.",
        "help": "",
        "too_low": "too low, dumbass",
        "too_high": "too high, dumbass",
        "congrats": "finally... i was getting sleepy. you're slow. it took you {attempts} attempts.",
        "invalid": "do you have a dent in your head?",
    },
    "mother": {
        "intro": "hey sweetiee. i missed you so much! if you want some cookies, guess the number im thinking between {min_number} and {max_number}.",
        "help": "",
        "too_low": "oh sweetie, that's too low.",
        "too_high": "oh sweetie, that's too high",
        "congrats": "YESSSSSSSSSSSSSS i am SO proud of you my little baby. and it only took you {attempts} attempts!",
        "invalid": "that's not valid sweetie",
    },
    "commander": {
        "intro": "I NEED YOU TO GUESS THE NUMBER IN MY MIND SOLDIER. IT'S BETWEEN {min_number} AND {max_number}. NOW!",
        "help": "",
        "too_low": "TOO LOW, SOLDIER!",
        "too_high": "TOO HIGH, SOLDIER!",
        "congrats": "GOOD JOB SOLDIER. IT TOOK YOU {attempts} ATTEMPTS.",
        "invalid": "*looks at you angrily*",
    }

}



def number_guessing_game(min_number=1, max_number=10_000_000, selected_font="default", selected_personality="default"):
    def display_ascii(font_name):
        fonts = get_fonts()
        if font_name in fonts:
            print(fonts[font_name])
        else:
            print(fonts["default"])


    display_ascii(selected_font)

    dialogue = personalities[selected_personality]

    # Game
    print(dialogue["intro"].format(min_number=min_number, max_number=max_number))
    print(dialogue["help"])

    # Number gen
    number_to_guess = random.randint(min_number, max_number)
    attempts = 0

    while True:

        guess = input("Enter your guess: ").strip()
        # Restart
        if guess.lower() in ["settings", "configure", "set"]:
            return "settings", min_number, max_number, selected_font, selected_personality

        if guess.lower() == "restart":
            return "restart", min_number, max_number, selected_font, selected_personality

        if guess == "help":
            print("""
            Type 'info' if you want info about the game
            Type 'settings' if you want to configure some stuff (like the number range)
            """)
            continue

        if guess == "info":
            print("""
            Made in Turkey!
            Made by terra238523
            Beginner project
            """)
            continue
        # Guessing
        try:
            guess = int(guess)
            attempts += 1

            if guess < number_to_guess:
                print(dialogue["too_low"])
            elif guess > number_to_guess:
                print(dialogue["too_high"])
            else:
                print(dialogue["congrats"].format(attempts=attempts))
                return "finished", min_number, max_number, selected_font, selected_personality

        except ValueError:
            print(dialogue["invalid"])

def settings(min_number, max_number, selected_font, selected_personality):
    while True:
        print("\nSettings")
        print("1. Change number range")
        print("2. Change ASCII font")
        print("3. Change personality")
        print("4. Go back")

        choice = input("Choose an option (by the numbers): ").strip()

        if choice == "1":
            min_number, max_number = change_number_range(min_number, max_number)
        elif choice == "2":
            selected_font = change_ascii_font(selected_font)
        elif choice == "3":
            selected_personality = change_personality(selected_personality)
        elif choice == "4":
            return min_number, max_number, selected_font, selected_personality
        else:
            print("Invalid choice.")

def change_personality(current_personality):
    print("/nAvailable personalities: ")
    for personality in personalities.keys():
        print(f"- {personality}")

    while True:
        new_personality = input("Enter personality: ").strip().lower()
        if new_personality in personalities:
            print(f"Personality changed to '{new_personality}'.")
            return new_personality
        else:
            print("Invalid personality.")


def change_number_range(current_min, current_max):
    print(f"\nCurrent range: {current_min} to {current_max}")
    while True:
        try:
            min_number = int(input("Minimum number: "))
            max_number = int(input("Maximum number: "))
            if min_number >= max_number:
                print("Min number must be less than the max number!")
            else:
                print(f"Range updated")
                return min_number, max_number
        except ValueError:
            print("Enter a valid number.")

def change_ascii_font(current_font):
    fonts = get_fonts()
    print("\nAvailable fonts:")
    for font_name in fonts.keys():
        print(f"- {font_name}")

    while True:
        new_font = input("Enter font: ").strip()
        if new_font in fonts:
            print(f"font changed to '{new_font}'.")
            return new_font
        else:
            print("invalid")




# Loop
min_number, max_number = 1, 10_000 #default range
selected_font = "default"
selected_personality = "default"
while True:
    result, min_number, max_number, selected_font, selected_personality = number_guessing_game(min_number, max_number, selected_font, selected_personality)

    if result == "settings":
        min_number, max_number, selected_font, selected_personality = settings(min_number, max_number, selected_font, selected_personality)


    if result == "restart":
        continue