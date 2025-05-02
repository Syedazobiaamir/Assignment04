import random  # to generate random numbers for dice rolls

def roll_two_dice():
    # Roll the first die (random number between 1 and 6)
    die1 = random.randint(1, 6)

    # Roll the second die
    die2 = random.randint(1, 6)

    # Calculate the total of both dice
    total = die1 + die2

    # Print the results
    print(f"Die 1 rolled: {die1}")
    print(f"Die 2 rolled: {die2}")
    print(f"Total of both dice: {total}")

# Run the simulation
roll_two_dice()
