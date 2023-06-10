# TextBasedGame.py
# Zachary Nicholas
rooms = {
        'Castle Courtyard': {'West': 'Kings room','North': 'Town Square'}, # First Room
        'Kings room': {'East': 'Castle Courtyard', 'item':'Kings Orders'},
        'Town Square': {'South': 'Castle Courtyard', 'North': 'Country Road', 'West': 'Butcher shop', 'East': 'Armory', 'item': 'Health Potion'},
        'Country Road': {'South': 'Town Square', 'East': 'Dragon Den', 'item': 'Bow'},
        'Butcher shop': {'East': 'Town Square', 'item': 'Meat'},
        'Armory': {'North': 'Sparring Grounds','West': 'Town Square', 'item': 'Shield'},
        'Sparring Grounds': {'South': 'Armory', 'item': 'Sword'},
        'Dragon Den': {'West': 'Country Road'} #Last Room
}

#defining the game instructions
def introduction():
    print('')
    print('Tale of the Heroic Knight \n')
    print('\nThere are 8 rooms to move between and 6 items to pick up\n')
    print('that you will require to complete your adventure.\n')
    print('Directions: You can go North, South, East, or West\n')
    print('to navigate between rooms. If the room has an item\n')
    print('it will be picked up and added to your inventory.\n')
    print('You can also type exit to leave the game. Good Luck!\n')


# Defining player status, prints
def player_status():
    print('=========================================')
    print('\nYou are currently in the {}'.format(currentRoom))
    print('\nYour current inventory: {}'.format(inventory))
    #print('You see a {}'.format(currentItem))
    print('\n=========================================')
    print('\n')

# Inventory list to hold inventory as it's added in each room
inventory = []

user_item = ''
# defining Inventory carried to add to inventory list
def game(item):
    #user_item = input('')

    if item in inventory:  # use in operator to check membership
        print("you already have got this")
        print(" ".join(inventory))

    elif item not in inventory:
        print('You see a', item)
        print('Would you like to pick it up? \n')
        user_item = input('')
        if user_item == 'Y':
            print('item has been added\n')
            inventory.append(item)
        else:
            print('You leave the item behind.')



# Current Room, starts off in Castle Courtyard
currentRoom = 'Castle Courtyard'

# Players Move
player_move = ''

# Calling the Introduction function
introduction()

# While Loop for moving between rooms
while True:
    player_status()

    player_move = input('Enter a move: \n')

    if player_move == 'Exit':
        print('Thanks for playing.')
        # break statement for exiting
        break

    if player_move in rooms[currentRoom]:
        currentRoom = rooms[currentRoom][player_move]

        addItem = input(' \n')

        if 'item' in rooms[currentRoom]:
            game(rooms[currentRoom]['item'])

        #if/else statements with break statement for final room/finishing the game
        if currentRoom == 'Dragon Den':
            if len(inventory) == 6:
                print('\nCongratulations!')
                print('\nYou have made it to the Dragons Den with all of the items to ')
                print('kill the dragon. You used the items you collected to kill')
                print('the dragon, and Saved the City! You are a Hero to your Country!\n')
                print('Thanks for playing! \n\n')
                break

            else:
                print('\nYou Failed!')
                print('\nYou are missing items needed to kill the dragon')
                print('& the dragon has killed everyone in the castle.')
                print('time to choose a new town and job')
                print('Please play again')
                break

    # else statement for input validation/invalid move
    else:
        print('\nYou walk in to a wall, try again.\n')