import random

# Global variable to hold the total score
total_score = 0

def roll_dice():
    global total_score  # Tells Python to use the global variable

    # Local variables
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    round_score = die1 + die2
    total_score += round_score  # Update global total score

    print(f"Die 1: {die1}, Die 2: {die2}, Round Total: {round_score}")

def main():
    print("Rolling two dice three times:\n")
    
    for i in range(3):
        print(f"Roll {i + 1}:")
        roll_dice()
        print()

    print(f"Final Total Score after 3 rolls: {total_score}")

main()
