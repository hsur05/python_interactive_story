import time
import random 


#PICKUP ITEM:
def item_pickup(item_name, item_description):
    while True:
        player_input = input(f"Should I pick up {item_name}? [Type yes or no]: ").lower()
        if player_input == "yes":
            print(f"\n**I collected the {item_name}, who knows what I'll need it for**")
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
            print("invalid choice, please type yes or no")

#INVENTORY:
inventory = {}
def inventory_print():
    if len(inventory) == 0:
        print("inventory is currently empty")
    else:
        for item, description in inventory.items():
            print(f"{item}: {description}")


# STORY INTRODUCTION
print("What's Next?\n")
#time.sleep(1)
print("11:43PM")
#time.sleep(1)

print("I was driving in quiet and rainy Harrisville, Rhode Island, my mind drifting toward recent life troubles...financial...health...relationships... "
"when I was jolted back into the present by a loud BANG behind the back passenger's seat...")
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
      "\nTurns out it was a historcal house, like it was built in the 1700s. \nThe sidings were showing its rotted-wooden color, as the paint has peeled off. \nThe roof looked to be newly restored with the typical grey shingles. "
      "\nIt was a pretty big house, maybe 4 or 5 bedrooms? It sat on a spacious lot with overgrown weeds. "
      "\nWalking around the property from the back to find the main entrance, I noticed that only one window was dimly lit, the others pitch black."
      "\nWhen I reached the front door, I noticed that historic plaque nailed right next to it, which read \"THE PERRON HOUSE, BUILT 1736\""
      "\n\"hmmmmm sounds familiar, I've definitely heard the name Perron before, but from where?\""
      )
#time.sleep(10)

print("\nJust as I was still pacing and looking around the main entrance for anyone in the house, I hear a women from the house shouted in a high pitch \"Do you need help? Come in!\""
      "\nThe old lady didn't excatly sound unfriendly, plus in that moment I remembered my conversation with my friend about the \"sunk cost fallacy\"."
      "\n\"I have no other choice,\" I thought as I suspiciously stepped into the foyer."
      )
