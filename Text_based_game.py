# each room and which rooms it's connected to with directionality.
rooms = {
    "courtyard": {"N": "throne_room", "S": "lost_library", "E": "defensive_wears", "W": "weaponry"},
    "defensive_wears": {"W": "courtyard", "S": "alchemists_abode"},
    "alchemists_abode": {"N": "defensive_wears", "S": "conjurers_corner"},
    "conjurers_corner": {"W": "lost_library", "N": "alchemists_abode"},
    "lost_library": {"E": "conjurers_corner", "W": "summoners_space", "N": "courtyard"},
    "summoners_space": {"E": "lost_library", "N": "illusionists_isolation"},
    "illusionists_isolation": {"N": "weaponry", "S": "summoners_space"},
    "weaponry": {"S": "illusionists_isolation", "E": "courtyard"},
    "throne_room": {"S": "courtyard"}  # Player needs all 7 items to win the battle here,
    # they'll be given a check to see if they want to enter the throne room
}
# the items in the given rooms
room_items = {
    "courtyard": None,
    "defensive_wears": "Armor",
    "alchemists_abode": "Potion of fire resistance",
    "conjurers_corner": "Ring of binding",
    "lost_library": "Book titled 'Tipping the scales'",
    "summoners_space": "Ring of summoned companion",  # consider changing this one
    "illusionists_isolation": "Circlet of true sight",
    "weaponry": "Sword",
    "throne_room": None
}

# Player starts out in the courtyard
current_room = "courtyard"
gear = []  # Player's gear
req_items = 7  # We need all of these to defeat the dragon
outcome = ''  # how did the battle turn out

# Opening statement, pep8'd
print("The King's Bounty, a text based Dragon dungeon game.")
print("Greetings, Intrepid hero. The kingdom calls upon you in its hour of need, "
      "it appears a dragon has seized the throne room for its new lair. The monarch "
      "beseeches you to expel the mighty beast post haste. Within the walls of the keep "
      "are all that you would need to do so. You will need a sword and armor, each stored "
      "in armories adjacent to the Courtyard. Starting clockwise from the Northeasternmost "
      "room, the defensive armory, and moving downward are the following rooms: The Alchemists’ "
      "Abode, where you’ll find a potion of fire resistance; take it, lest ye be fried to a "
      "crisp. Next southbound is the Conjurer’s Corner, where you’ll find the ring of binding. "
      "This will prevent the mighty beast from taking flight, a great peril indeed. To the "
      "Conjurer’s west is The Lost Library. Here you’ll find a book about defeating dragons "
      "named ‘Tipping the Scales’; knowledge is power. Further west is the Summoner’s space, "
      "where you’ll find a ring to summon an ethereal companion to help you with your battle. "
      "North of the Summoner is the Illusionists’ isolation. Here you’ll get the Circlet of "
      "True Sight; may your swings ever ring true. This brings us to the Northwesternmost room, "
      "the Weapons Armory. Our finest steel is stored here; use it well. The center of this "
      "square is a beautiful courtyard where we’ll sneak you in from the sewers, but have "
      "caution: to travel north is to meet the Dragon! Collect all 7 quest items and you will "
      "be a force to be reckoned with! Fair thee well, hero, we’re depending on you.")


# Function to move player between rooms
def move_player(current_room, direction):
    if direction in rooms[current_room]:
        current_room = rooms[current_room][direction]
        print(f"\nYou move {direction} to the {current_room.replace('_', ' ')}.")

        # If the player reaches the throne room, trigger the battle
        if current_room == "throne_room":
            battle(gear)
            if outcome == 'Victorious':
                print(
                    "\nIt is a mighty battle! Your clash with the dragon is fierce, but with all 7 of these legendary items, "
                    "you emerge victorious! The kingdom is saved!")
                print("\nGame Over.")
                return False
            else:
                print("\nYou enter the throne room unprepared. The dragon has added your charred bones to his hoard. "
                      "You needed all 7 items to stand a chance... Who will save us now?")
                print("\nGame Over.")
                return False
        else:
            # Check if there is an item in the current room
            item = room_items[current_room]
            if item and item not in gear:
                pick_up_item(item, gear)
    else:
        print("\nAlas! We can't walk through walls!")

    return current_room


# Function to prompt player to pick up an item
def pick_up_item(item, gear):
    while True:
        choice = input(f"\nYou see {item}. Would you like to pick it up? (Y/N): ").upper()
        if choice == "Y":
            gear.append(item)
            print(f"\nYou have picked up {item}.")
            break
        elif choice == "N":
            print(f"\nYou leave the {item} behind for some reason. Your life, I suppose.")
            break
        else:
            print("Please enter 'Y' or 'N'.")


# Function to handle the final battle in the throne room
def battle(gear):
    global outcome
    user_choice = input('Are you ready? Y or N').upper()
    if len(gear) == 7:
        outcome = 'Victorious'
    # old version elif len(gear) != 7 and user_choice == 'Y':
    elif user_choice == 'Y':
        outcome = 'Dead'

    return  # End the game


def show_status():
    # what room are we in, how many and which gear items do we have
    print(f"\nYou are in the {current_room.replace('_', ' ')}.")
    if len(gear) > 1:
        print(f"Your gear: {', '.join(gear)}.")
    if current_room in rooms:
        adjacent_rooms = rooms[current_room]
        directions = ', '.join(f"{direction} to {room.replace('_', ' ')}" for direction, room in adjacent_rooms.items())
        print(f"You can go: {directions}.")


# Game loop
while True:
    # current loc, current gear
    show_status()

    # Get user input for movement
    direction = input("\nWhich direction do you want to go? (N/S/E/W or 'quit' to exit): ").upper()

    if direction == "QUIT":
        print("Come back soon, our kingdom awaits a hero!")
        break
    elif direction in ["N", "S", "E", "W"]:
        move = move_player(current_room, direction)
        if move is False:
            break
        else:
            current_room = move

    else:
        print("\nInvalid direction! Please enter N, S, E, or W.")
