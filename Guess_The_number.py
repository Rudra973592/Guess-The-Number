import random as rd

rd_num = rd.randrange(1, 101)

print("-" * 50)
print("-" * 16, "GUESS THE NUMBER", "-" * 16)
print("-" * 50)

while True:
    num = input("Enter a number between 1 to 100 (Press Q to QUIT): ").strip()

    if num.upper() == "Q":
        print(f"The correct number was {rd_num}. Better luck next time!")
        break

    try:
        num = int(num)
    except ValueError:
        print("Please enter a valid number or 'Q' to quit.")
        continue

    if num < 1 or num > 100:
        print("Your number is not between 1 to 100.")
    else:
        if num > rd_num:
            print("Your number is greater than the required number.")
        elif num < rd_num:
            print("Your number is smaller than the required number.")
        else:
            print(f"Yes! You guessed it right. It's {num}.")
            break

print("-" * 20, "GAME OVER", "-" * 19)