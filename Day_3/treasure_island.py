print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input(
    "You are in a cross road. Enter which direction you want to go? (left or right) \n").lower()
if(direction == "left"):
    print("You have come to a lake. There is an island in the middle of the lake\n")
    decision = input(
        "Type wait to 'wait' for a boat or 'swim' to swim across \n").lower()
    if(decision == "wait"):
        print("You have arrived at the island \n")
        door = input(
            "There is a house with 3 doors with colours red,blue and yellow. Choose one color. \n").lower()
        if door == "red":
            print("Room full of fire! Game over!\n")
        elif door == "blue":
            print("Room full of demons! Game over! \n")
        else:
            print("You've found the treasure! You Win! Congrats!\n")
    else:
        print("You tried swimming and got attacked by crocodile! Game over!\n")

else:
    print("You turned right and fell inside a well! Game over!\n")

