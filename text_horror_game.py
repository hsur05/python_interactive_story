import time
import random 

#INVENTORY:
inventory = {}
def inventory_print():
    for item, description in inventory.items():
        print(f"{item}: {description}")


# STORY INTRODUCTION
print("What's Next?\n")
#time.sleep(1)
print("11:43PM")
#time.sleep(1)

print("I am driving in rainy Harrisville, Rhode Island in the middle of the night, my mind drifted to recent life troubles...financial...health...relationships, when I hear a loud pop behind the back passenger's seat...")
#time.sleep(3)
print("I get out of the car with my phone light to peek at what's going on, only to notice that not only do I have a flat tire, but there is also no cellular reception... \n")

#time.sleep(3)
print("I am cold and alone. And I don't know what to do..."
    "\nI start to feel my heart sink into my stomach. my breathing is so fast, but I seem to see better, think clearer.\n")

#time.sleep(3)
print("\"What should I do?\" I thought to myself as I paced around the car."
    "\nIn the short distance, I saw in a forest a dim light and smoke rising into the sky. Is that a campfire? or a house?"
    "\n\"Do I have any other choice than to go in?\" I thought to myself as I tried to find any other possible solution."
    "\nI looked around for the faintest possibility of not having to go toward the smoke...\n")
#time.sleep(7)
print("But there was nothing- It's all just trees on one side, and walking along the road will take hours to reach anything."
    "\nBegrudgingly, I decided I have no other choice but to go see what the light is. \n")
#time.sleep(10)

print("Thankfully, the hike to the smoke more like a brisk walk. And on the way I even found a big branch, which I used as a hiking pole, or if something dangerous comes my way... I could use it somehow to defend myself...")
#time.sleep(3)
print("**I collected the hiking pole**")
#add to inventory list:
inventory['Hiking pole']= 'A large wooden stick that can also double as a blunt weapon if needed'
print("Current inventory:")
inventory_print()

#time.sleep(5)
print("\nI reached the location of the smoke pretty soon afterwards."
    "\nTurns out it was a historcal house, like it was built in the 1700s. \nThe sidings is showing its rotted-wooden color, as the paint has peeled off. \nThe roof looks to be newly restored with the typical grey shingles. "
    "\nIt's a pretty big house, maybe 4 or 5 bedrooms? It sits on a spacious lot with overgrown weeds. "
    "\nWalking around the property from the back to find the main entrance, I noticed that only one window was dimly lit, the others pitch black."
    "\nWhen I reached the front door, I noticed that historic plaque nailed right next to it, which read \"THE PERRON HOUSE\""
    "\n\"hmmmmm sounds familiar, I've definitely heard the name before, but from where?\"")
#time.sleep(10)

print("\n Just as I was still pacing and looking around the main entrance for any signs of life, I hear a women from the house shouted in a high pitch \"come in!\"")

