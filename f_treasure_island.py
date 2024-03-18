print("Welcome to the Treasure Island!!")
print("Your Mission is to find the Treasure.")
left_or_right = input("You're at the cross road. Where do you want to go? Type 'left' or 'right'.----->").lower()
if left_or_right == 'left':
    wait_or_swim=input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.----->").lower()
    if wait_or_swim == 'wait':
        doors = input("You arrive at the island unharmed. There is a house with 3 doors. One red, One yellow and one blue. Which color do you choose?----->").lower()
        if doors == 'blue':
            print("You enter room of Beasts Game Over!")
        elif doors == 'red':
            print("It's a room full of fire. Game Over!")
        elif doors == 'yellow':
            print(" Yayyy you found the Treasure. You win !!")
        else:
            print("This Door doesn't Exist")
    else:
        print("You got attacked by a Monster..! Game Over.")
else:
    print("you fell.! Game Over.")
