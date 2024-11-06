import random

def guess_number():
    """
    Permite utilizatorului să ghicească un număr generat aleatoriu între 1 și 10.
    """
    number_to_guess = random.randint(1, 10)
    guess = None
    while guess != number_to_guess:
        guess = int(input("Ghiceste numarul (intre 1 si 10): "))
        if guess < number_to_guess:
            print("Prea mic!")
        elif guess > number_to_guess:
            print("Prea mare!")
        else:
            print("Felicitari! Ai ghicit numarul.")

# Testează funcția
guess_number()
