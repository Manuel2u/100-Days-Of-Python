print("Welcome to Treasure Isalnd.\nYour mission is to find the treasure.")

step_1 = print(input("You're at a crossroad. Where do you want to go? Type 'left' or 'right'"))

if step_1 == "left":
    step_2 = print(input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across."))
    if step_2 == "wait":
        step_3 = print(input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?"))
        if step_3 == "red":
            print("It's a room full of fire. Game Over.")
        elif step_3 == "yellow":
            print("You found the treasure! You Win!")
        elif step_3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
