import random
import time

#This program simulates the card game War

print("================================")
print("Python Game of War")
print("================================")

# Declarations
p1_card = 0
p2_card = 0
p1_score = 0
p2_score = 0

game_status = input("Type PLAY and press ENTER:")
if (game_status == "PLAY"):
    for x in range(20):

        # Regular round
        p1_card = random.randint(0, 9)
        p2_card = random.randint(0, 9)
        print("\nYour card:", p1_card, "Opponent's card:", p2_card)
        if (p1_card > p2_card):
            print("You won this round!")
            p1_score += 2
        elif (p1_card < p2_card):
            print("Your opponent won this round!")
            p2_score += 2

        # War round (on both players drawing same value card)
        else:
            print("War! Each player draws three cards.")
            time.sleep(2)
            p1_card = random.randint(0, 9)
            p2_card = random.randint(0, 9)
            print("Your card:", p1_card, "Opponent's card:", p2_card)
            if (p1_card > p2_card):
                print("You won the war!")
                p1_score += 8
            elif (p1_card < p2_card):
                print("Your opponent won the war!")
                p2_score += 8
        input("Press ENTER to continue")

    # Determining winner
    print("\nFinal Score\n===========\nYou:", p1_score, "Opponent:", p2_score)
    if (p1_score > p2_score):
        print("\nYou won! Play again?")
    elif (p1_score < p2_score):
        print("\nYou lost! Play again?")
    else:
        print("\nDraw! Play again?")

# If PLAY is not entered
else:
    print("\nPLAY not entered; program ended.")
