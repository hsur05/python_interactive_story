import time
import random 


#PICKUP ITEM:
def item_pickup(item_name, item_description):
    while True:
        player_input = input(f"Should I pick up {item_name}? [Type yes or no]: ").lower().strip()
        if player_input == "yes":
            print(f"\n**I collected the {item_name}**")
            #add to inventory list:
            inventory[item_name]= item_description
            print("\nCURRENT INVENTORY:")
            inventory_print()
            return True
        elif player_input == 'no':
            print("\nI don't think I need it.")
            print("\nCURRENT INVENTORY:")
            inventory_print()
            return True
        else:
            print("Invalid input- please type yes or no")

#CLUE INSPECT:
def clue_inspect(clue_name, clue_description):
    while True:
        player_input = input(f"Should I inspect {clue_name}? [Type yes or no]: ").lower().strip()
        if player_input == "yes":
            print(f"\n**I inspected the {clue_name}**")
            print(f"{clue_name}: {clue_description}")
            return True
        elif player_input == "no":
            print("I shouldn't touch that...")
            return True
        else:
            print("Invalid input- please type yes or no")

#INVENTORY:
inventory = {}
def inventory_print():
    if len(inventory) == 0:
        print("Inventory is currently empty")
    else:
        for item, description in inventory.items():
            print(f"{item}: {description}")

#CHOOSING ROOM
def choose_room():
    print("Which room do I want to go into? \n1) Parlor \n2) Basement \n3) Kitchen \n4) Bathroom")

    while True: 
        room_input = input(f"choose a room: [Type 1, 2, 3, 4, or 'random'] ").lower().strip()
        room_list = [parlor, basement, kitchen, bathroom]
        if room_input == "1":
            parlor()
            return True
        elif room_input == "2":
            basement()
            return True
        elif room_input == "3":
            kitchen()
            return True
        elif room_input == "4":
            bathroom()
            return True
        elif room_input == "random":
            random_room = random.choice(room_list)
            random_room()
            return 
        else:
            print("Invalid input- please type 1, 2, 3, 4, or random")

def parlor():
    print("test parlor")

def basement():
    print("test basement")
    #where the plot continues, like the movie

def kitchen():
    print("test kitchen")

def bathroom():
    print("test bathroom")


#PLOT
print("What's Next?\n")
#time.sleep(1)

print("11:43PM")
#time.sleep(1)

print("I was driving in quiet and rainy Harrisville, Rhode Island, my mind drifting toward recent life troubles...financial...health...relationships... "
      "\nwhen I was jolted back to the present by a loud *BANG* behind the back passenger's seat...")
#time.sleep(3)

print("I got out of the car with my phone light to peek at what's going on, only to notice that not only did I have a flat tire, but there was also no cellular reception... \n")
#time.sleep(3)

print("I was cold and alone. And I didn't know what to do..."
      "\nI started to feel my heart sink into my stomach. my breathing was so fast, but I seemed to see better and think clearer.\n"
      "\"What should I do?\" I thought to myself as I paced around the car.\n"
      "\"Before I left the car, that there are some things I should probably grab with me."
)

item_pickup('Pocket knife', 'A medium-sized foldable knife')
#time.sleep(3)

print("12:05AM"
      "\nIn the short distance, I saw in a forest a dim light and smoke rising into the sky. Is that a campfire? or a house?"
      "\n\"Do I have any other choice than to go in?\" I thought to myself as I tried to find any other possible solution."
      "\nI looked around for the faintest possibility of not having to go toward the smoke...\n"
)
#time.sleep(7)

print("But there was nothing- It was all just trees on one side, and walking along the road would take hours to reach anything."
      "\nBegrudgingly, I decided I had no other choice but to go see what the light was. \n"
)
#time.sleep(10)

print("Thankfully, the hike to the smoke more like a brisk walk. And on the way I found a big branch...")
item_pickup('Hiking pole', 'A large wooden stick that can also double as a blunt weapon if needed')
#time.sleep(5)

print("\n12:26AM"
      "\nI reached the location of the smoke pretty soon afterwards."
      "\nTurns out it was a historcal house, like it was built in the 1700s. \nThe sidings were showing its rotted wooden color, as the paint has peeled off. "
      "\nThe roof looked to be newly restored with the typical grey shingles. "
      "\nIt was a mansion, maybe 6 or 7 bedrooms? It sat on a spacious lot with overgrown weeds. "
      "\nWalking around the property from the back to find the main entrance, I noticed that only one window was dimly lit, the others pitch black."
      "\nWhen I reached the front door, I noticed that historic plaque nailed right next to it, which read \"THE PERRON ESTATE, BUILT 1736\""
      "\n\"hmm sounds familiar, I've definitely heard the name Perron before, but from where?\""
)
#time.sleep(15)

print("\nJust as I was still pacing and looking around the main entrance for anyone in the house, I hear a women from the house shouted in a high pitch \"Do you need help? Come in!\""
      "\nThe old lady didn't sound unfriendly per se, plus in that moment I remembered my conversation with my friend about the \"sunk cost fallacy\"..."
      "\n\"I've come this far and have no other choice...,\" I thought as I suspiciously stepped into the Perron House."
)
#time.sleep(5)

print("\nAs soon as I stepped foot into the dark house, I noticed a faint smell, like a trash can that's been left out for too long"
      "\nRight next to me, on the floor below the shoe rack, there was an item that looked like a wooden cross."
)
#time.sleep(3)

clue_inspect("Small cross", "A wooden cross no bigger than my palm that looks like an heirloom treasure. The wood is scratched and blackened, as if it had been scorched. "
"\nOn it is a paper tag hanging from the bottom. The faded ink read: \"Property of Ed and Lorraine Warren\""
"\n")
#time.sleep(2)

print("Is my mind playing tricks with me? Ed and Lorraine Warren...I've definitely heard of those names before. Where?"
      "\nMy stomach turns. I swear, for a moment the scratches on the cross seemed like they were moving to form the letters \"t rtur \""
      "\nJust as I was staring down the dark hallway, trying with all my might to remember who Ed and Lorraine were, when suddenly..."
      "\na strong breeze almost pushed me over. It was from behind me, shutting the door closed. I tried to open it, but the knob wouldn't turn."
      "\nThen, I heard a door shut from somewhere within the house. "
      "\nThe hair on my back immediately stood up, and I sought to hide in a room"
      "\nBut which room should I go? I was sure that the clues about what was happening was somewhere in the house...\n"
)
#time.sleep(10)

choose_room()
