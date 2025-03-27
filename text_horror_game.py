import time
import random 

# Ask player if they want to continue the game
def continue_game():
    while True:
        player_input = input(f"Continue? [y or n]: ").lower().strip()
        if player_input == "y":
            return True
        elif player_input == 'n':
            print("This is all too much, I am taking a break... [y to continue]")
        else:
            print("Invalid input- please type y or n")

# Handle item pickup and update inventory
def item_pickup(item_name, item_description):
    while True:
        player_input = input(f"Should I pick up {item_name}? [y or n]: ").lower().strip()
        if player_input == "y":
            print(f"\n**I collected the {item_name}**")
            # Add item to inventory dictionary
            inventory[item_name] = item_description
            print("\nCURRENT INVENTORY:")
            inventory_print()
            return True
        elif player_input == 'n':
            print("\nI don't think I need it.")
            print("\nCURRENT INVENTORY:")
            inventory_print()
            return True
        else:
            print("Invalid input- y or n")

# Inspect clues with player input
def clue_inspect(clue_name, clue_description):
    while True:
        player_input = input(f"Should I inspect {clue_name}? [y or n]: ").lower().strip()
        if player_input == "y":
            print(f"\n**I inspected the {clue_name}**")
            print(f"{clue_name}: {clue_description}")
            return True
        elif player_input == "n":
            print("I shouldn't touch that...")
            return True
        else:
            print("Invalid input- y or n")

# Global inventory to track collected items
inventory = {}
def inventory_print():
    # Display current inventory or show it's empty
    if len(inventory) == 0:
        print("Inventory is currently empty")
    else:
        for item, description in inventory.items():
            print(f"{item}: {description}")

# Allow player to choose or randomly select a room
def choose_room():
    while True: 
        print("Which room should I go into? \n1) Parlor \n2) Basement \n3) Kitchen \n4) Bedroom")
        room_input = input(f"Choose a room [Type 1, 2, 3, 4, or random]: ").lower().strip()
        room_list = [parlor, basement, kitchen, bedroom]
        
        # Map user input to specific room functions
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
            bedroom()
            return True
        elif room_input == "random":
            # Select a random room if requested
            random_room = random.choice(room_list)
            random_room()
            return 
        else:
            print("Invalid input- type 1, 2, 3, 4, or random")

# Room-specific exploration functions
def parlor():
    # Descriptive narrative for the parlor room
    print("Just as I decided to enter the parlor, the light on my phone went out."
          "\n\"Damn, at least I carried my flashlight,\" I recalled. I was now in the parlor."
          "\nI locked the door just to be sure."
          "\nLooking around, I thought if it wasn't for this eerie atmosphere, I would've loved to spend time here."
          "\nThe room had Victorian-styled furniture- plush velvet couch in olive green, "
          "intricate wallpapers with repeating figures of tigers in various poses, and lamps with supple textures as shades."
          "\nAs I looked around the room to try to find clues, I noticed two items that seemed out of place. "
          )

    print("Which item should I inspect first?"
          "\n1) Pick up the old black-and-white photograph"
          "\n2) Flip through a tattered book without a jacket"
          )

    # Navigate clue selection in this room
    choose_clues()
    choose_room()

def basement():
    # Narrative and events in the basement
    print("The basement is damp and freezing, faint whispers echo through the air. They weren't words, but definitely voices."
          "\nA small lightbulb flickers above, the only light source in the entire basement, casting unsettling shdows on the cracked walls."
          "\nEven in the dim light, you could see movement in the corner of the room. Was that a hand? A head turning?"
    )
    print("Suddenly, the door slams shut behind you.")

    print("A low, guttural voice whispers, 'She waits below.'")
    
    print("You see movement in the shadows. Then, she appears — the woman from the paintings, bound and levitating.")
    print("Her eyes are hollow, and her body twitches unnaturally.")

    print("Crosses on the walls begin to twist, turning upside down one by one.")
    print("The temperature plummets, and the air grows heavy with dread.")
    
    # Different outcomes based on inventory
    if "Pocket knife" in inventory:
        # Successful resolution if player has pocket knife
        print("You clutch your pocket knife tightly. The entity screeches, its form contorting."
              "\nYou slash through the ropes holding the woman. She collapses, gasping for air."
              "\nThe crosses stop turning. The whispers fade."
              "\nYou've broken the curse — for now."
              "\nYou help her to her feet, and together, you escape the house."
              "\nThe nightmare is over... or is it?")
    else:
        # Bad ending if player lacks the knife
        print("You search for something, anything to fight with — but there's nothing."
              "\nThe spirit shrieks as the woman's body levitates higher."
              "\nYou're powerless. The final cross turns upside down. The room darkens."
              "\nThe entity lunges toward you. You scream, but no one hears.")

        print("EPILOGUE")
        print("4AM")
        print("\nThe glow of a phone screen illuminated a dimly lit room. My girlfriend stared at the location app, her eyes wide with fear. The blinking dot hadn't moved for hours.")
        print("\nShe had called the police, pleading for them to check the location. They assured her someone would be sent. But the minutes crawled by, each second heavy with dread.")
        print("\nBy the time the officers arrived, the forest was silent. The door creaked open to reveal the empty cabin — the lingering scent of damp wood and something… foul.")
        print("\nThe floor was scratched, as though something had been dragged. The police searched, but there was no sign of me. "
              "\nOnly the overturned chair and a single porcelain doll, its cracked face frozen in a twisted grin.")
        print("\nMy girlfriend's phone buzzed. A new notification. \"Location not found.\"")
        print("\nAnd somewhere, deep within the house, the doll somehow returned to the rocking chair...\n")
        print("GAME OVER: PRESS CONTROL + C")

def kitchen():
    # Descriptive narrative for the kitchen
    print("Like the rest of the house, the kitchen was furnished by the same Victorian decor and appliances."
          "\nUsing the light to look around, noticed the kitchen was a mess- pots and pans were scattered on the floor, the fridge was left open, and the sink was overflowing with dirty dishes."
          "\nHowever, everything had a thick layer of dust, as if nothing's been touched for years."
          "\nI noticed a faint smell of rotten eggs, but couldn't find the source."
          "\nI saw an item that seemed strange."
          )

    print("Should I pick up the item?"
          "\n3) An old, rusted knife stuck to the wall"
          )
    # Navigate clue selection in this room
    choose_clues()
    choose_room()

def bedroom():
    # Descriptive narrative for the bedroom
    print("Just like the foyer, the air in the bedroom felt unnaturally cold as I entered. "
          "\nThe walls were adorned with once-beautiful roses, but now wet stains seep through, forming moldy textures like a parsitic growth."
          "\nThere was a crib in the corner, next to a huge dresser. I walked over to peek inside. Just one toy, nothing else. It was like there was never a baby inside"
          "\nSomething about the doll that was inside the crib was so tantilizin, as if calling me over to pick it up. It looked benevolent, so why not?"
    )

    print("Should I pick up the item?"
          "\n4 A dusty old doll, its eyes seems to stare straight into my soul"
          )
    # Navigate clue selection in this room
    choose_clues()
    choose_room()

# Allow player to choose or randomly select a clue
def choose_clues():
    while True: 
        player_input = input(f"[Type number to investigate clue or r for random]: ").lower().strip()
        clue_list = [clue_1, clue_2, clue_3, clue_4]
        
        # Map user input to specific clue functions
        if player_input == "1":
            clue_1()
            return True
        elif player_input == "2":
            clue_2()
            return True
        elif player_input == "3":
            clue_3()
            return True
        elif player_input == "4":
            clue_4()
            return True
        elif player_input == "random":
            # Select a random clue if requested
            random_clue = random.choice(clue_list)
            random_clue()
            return 
        else:
            print("Invalid input- please type 1, 2, 3, 4, etc. or random")

# Specific clue inspection functions
def clue_1():
    # Inspect the old photograph
    clue_inspect("old photograph" , "I stepped closer to the photograph on the floor underneath the couch and picked it up."
                 "\nThe photo showed a family of seven, dressed in formal outfits. "
                 "I don't know if it was just the lighting, but the mom's eyes could not be seen, as it was replaced by two dark shadows. "
                 "\nCoincidentally, the photo didn't show the tallest child's head, as it had been torn. Strange."
                 "\nThere was a handwritten note scribbled on the back: **'Perron Family, 1971'**"
                 )
    
    # Ask to continue exploring or choose another room
    while True: 
        player_input = input("Continue to explore other items in this room? [y or n]").lower().strip()
        if player_input == 'y':
            parlor()
            return True
        elif player_input == 'n':
            choose_room()
            return True
        else:
            print("Invalid input- type y or n")

# Remaining clue inspection functions follow a similar pattern
def clue_2():
    # Inspect the tattered book
    clue_inspect("tatted book without a jacket" , "I carefully opened the book. The first page was titled: \"Apparitions in New England\"."
                 "\nAs I continued to flip through the book, a particular chapter that was bookmarkred stood out: "
                 "\n\"1971, The Perron Family asked the Catholic Church for aide as they were experiencing strange phenomena at home...\""
                 "\nThe words felt so heavet, like they carried some kind of dark power with them. My heart raced as I read on."
                 "\nIt described how the family claimed to witness apparitions soon after moving in- "
                 "doors being opened even though the mom closed it, heading disembodied voices, and finding objects that seemed to be misplaced."
                 "\nI felt a chill down my spine as I read the  line: \"With no other choice, the Perron Family asked Ed and Lorraine Warren to investigate the home.\""
                 "\nEd and Lorraine! Now I remembered- the paranormal investigators, whose names were on the cross I found earlier."
                 "\nSuddenly, the room felt colder, like a draft was coming from the walls, but all the windows were closed."
                 "\nI quickly tossed the book onto the couch, and it landed with a thud."
                 )

    # Ask to continue exploring or choose another room
    while True: 
        player_input = input("Continue to explore other items in this room? [y or n]").lower().strip()
        if player_input == 'y':
            parlor()
            return True
        elif player_input == 'n':
            choose_room()
            return True
        else:
            print("Invalid input- type y or n")

# Remaining clue_3 and clue_4 functions similar to above
def clue_3():
    clue_inspect("Rusty knife" , "The knife was covered in rust, its once-sharpened blade dulled and corroded. But there was an energy emanating from it, like it was used for something evil."
          "\nI felt a chill down my spine as I picked it up. The blade was heavy, and the handle was cold to the touch."
          "\nAlong the blade, there were traces of brown stains. Was it dried blood? Maybe. It smelled faintly like metal."
          "\nAnd then, just as I was putting hte knife down, I swear I heard a whisper from behind me, like a breatheless plea."
          "\n\"cel....\" is what I heard. What was it trying to say? Spell? Cell? Sale? Is it trying to tell me to go somewhere inside the house?"
          )
    #time.sleep(10)

def clue_4():
    clue_inspect("A dusty doll" , "The old doll was small, but unsettling. It's porceline face had a rigid and stretched smile, and one of the eye's paint was peeling off."
                 "\n The light from the window hit just right, and I could see my own reflection in the other  pitch black eye."
                 "\n What was the most unsettling was that it had a small locket necklace. When I opened the rusted locked, a very small slip of paper was inside..."
                 "\nWritte on it was \"Bethsheba, Bethsheba\""
                 )
    #time.sleep(10)

    print("I placed the doll back in its rocking chair, but as I turned awa, I heard a soft creakign sound. The crib was swaing lightly- or so I thought."
          "\nMy hands were trembling, and I frozen in horror. Was that just the wind? Just as I was trying to convince myself that it was nothing, the doll seemingly lost balance, and fell off the rocking chair."
          "\nJust when I came to my senses, The doll started moving its head slowly toward my direction."
          "\nBefore I could react, the doll lunged at me, its cracked arms wrapping around my neck. Its porcelain fingers dug into my skin like jagged claws. "
          "\nIt was heavier than it should be, as if something far more sinister was weighing it down. "
          "\nI gasped, struggling to pry it off, but its grip only tightened. My chest pounded. I could feel its cold presence — it wasn’t just a toy anymore."
          "\nAnd then I remembered — the pocket knife!"
          )

    if "Pocket knife" in inventory:
        print("\nWith trembling hands, I fumbled for the pocket knife in my bag. I barely managed to flip the blade open before slashing wildly at the doll. "
              "\nThe blade sliced through its arm, porcelain shards scattering across the floor. The doll screeched — an inhuman wail that rang in my ears. "
              "\nIt flailed, its body twitching as if resisting, but I didn’t stop. Another slash, then another. The lifeless grin remained, but it no longer moved.")
        
        print("\nPanting, I stumbled back, my hands trembling as I dropped the knife to the floor. The room was silent. The doll’s shattered pieces lay scattered — but I knew this wasn’t over.")
        choose_room()
    else:
        print("\nI reached for my bag in desperation, but I had no weapon. The doll’s grip tightened, and I could feel my body weaken. My vision blurred. I screamed — but it was no use.")
        print("\nAnd then... everything went black.")
        #time.sleep(15)

        print("EPILOGUE")
        #time.sleep(5)
        print("4AM")
        #time.sleep(2)
        print("\nThe glow of a phone screen illuminated a dimly lit room. My girlfriend stared at the location app, her eyes wide with fear. The blinking dot hadn’t moved for hours.")
        #time.sleep(4)
        print("\nShe had called the police, pleading for them to check the location. They assured her someone would be sent. But the minutes crawled by, each second heavy with dread.")
        #time.sleep(4)
        print("\nBy the time the officers arrived, the forest was silent. The door creaked open to reveal the empty cabin — the lingering scent of damp wood and something… foul.")
        #time.sleep(4)
        print("\nThe floor was scratched, as though something had been dragged. The police searched, but there was no sign of me. "
              "\nOnly the overturned chair and a single porcelain doll, its cracked face frozen in a twisted grin."
        )
        #time.sleep(5)
        print("\nMy girlfriend's phone buzzed. A new notification. \"Location not found.\"")
        #time.sleep(5)
        print("\nAnd somewhere, deep within the house, the doll somehow returned to the rocking chair...\n")
        print("GAME OVER: PRESS CONTROL + C")


# Main game introduction
print("BEYOND THE SHADOW\n")

print("11:43PM")

print("I was driving in quiet and rainy Harrisville, Rhode Island, my mind drifting toward recent life troubles...financial...health...relationships... "
      "\nwhen I was jolted back to reality by a loud *BANG* behind the back passenger's seat...")

print("I got out with my phone light to peek at what's going on, only to notice that not only did I get a flat tire, but there was also no cellular reception... \n")

print("I was cold and alone. And I didn't know what to do..."
      "\nI started to feel my heart sink into my stomach. my breathing was so fast, but I seemed to see better and think clearer.\n"
      "\"What should I do?\" I thought to myself as I paced around the car.\n"
      "\"Before I left the car, I thought there were things I should probably grab with me."
)

# Initial item pickups
item_pickup('Pocket knife', 'A medium-sized foldable knife')
item_pickup('Small LED flashlight', 'A small but bright rechargable flashlight')

print("12:05AM"
      "\nIn the short distance, I saw in a forest a dim light and smoke rising into the sky. Is that a campfire? or a house?"
      "\n\"Do I have any other choice than to go in?\" I thought to myself as I tried to find any other possible solution."
      "\nI looked around for the faintest possibility of not having to go toward the smoke...\n"
)

print("But there was nothing else close by- It was a dense forest on one side, and walking along the road would take hours to reach anybody."
      "\nBegrudgingly, I thought I had no other choice but to go see what the light was. \n"
)

print("Thankfully, the hike to the smoke was more like a brisk walk. And on the way I found a big branch...")
item_pickup('Hiking pole', 'A large wooden stick that can also double as a blunt weapon if needed')

# Rest of the game narrative and initial setup continues...
print("\n12:26AM"
      "\nI reached the location of the smoke soon afterwards."
      "\nTurns out it was a historcal house, like it was built in the 18th century. \nThe sidings were showing its rotted wooden color, as the paint has peeled off. "
      "\nThe roof looked to be newly restored with the typical grey shingles. "
      "\nIt was a mansion, maybe 6 or 7 bedrooms? It sat on a spacious lot with overgrown weeds. "
      "\nWalking around the property from the back to find the main entrance, I noticed that only one window was dimly lit, the others pitch black."
      "\nWhen I reached the front door, I noticed that historic plaque nailed right next to it, which read \"THE ARNOLD ESTATE, BUILT 1736\""
      "\n\"hmm sounds familiar, I've definitely heard the name Perron before, but from where?\""
)

# Final setup for game start
print("\nJust as I was still pacing and looking around the main entrance for anyone in the house, I hear a women from inside the house speak in a high pitch "
      "\"Do you need help? Come on in! You must be stranded\""
      "\nI couldn't see her, but the old lady didn't sound unfriendly per se, plus in that moment I remembered my conversation with my friend about the \"sunk cost fallacy\"..."
      "\n\"I've come this far and have no other choice...,\" I thought as I suspiciously stepped into the Perron House."
)

print("\nAs soon as I stepped foot into the dark house, I noticed a faint smell, like a trash can that's been left out for too long"
      "\nRight next to me, on the floor below the shoe rack, there was an item that looked like a wooden cross."
)

# Initial clue inspection
clue_inspect("Small cross", "A wooden cross no bigger than my palm that looks like an heirloom treasure. The wood is scratched and blackened, as if it had been scorched. "
    "\nOn it is a paper tag hanging from the bottom. The faded ink read: \"Property of Ed and Lorraine Warren\"\n"
)

print("Is my mind playing tricks with me? Ed and Lorraine Warren...I've definitely heard of those names before. Where?"
      "\nMy stomach turned. I could've sworn for a moment the scratches on the cross seemed like they were moving to form the letters \"t rtur \""
      "\nJust as I was staring down the dark hallway, scratching my head to remember who Ed and Lorraine were, when suddenly..."
      "\na strong breeze almost pushed me over. It was from behind me, shutting the door closed. I tried to open it, but the knob wouldn't turn."
      "\nThen, I heard a someone speak from within the house. "
      "\nThe hair on my back immediately stood up, and I sought to hide in a room"
      "\nBut which room should I go? I was sure that the clues about what was happening and how to get out were somewhere in the house...\n"
)

# Start the game by allowing room selection
choose_room()
