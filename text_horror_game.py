import random
import textwrap


class Game:
    """
    BEYOND THE SHADOW

    A refactored text-based horror game.

    Design notes:
    - Uses one main game loop instead of recursive room calls.
    - Tracks inventory, clues, visited rooms, and game state inside a Game class.
    - Endings stop the game cleanly by setting self.running = False.
    """

    def __init__(self):
        self.inventory = {}
        self.clues = set()
        self.visited_rooms = set()
        self.running = True

        self.rooms = {
            "1": ("Parlor", self.parlor),
            "2": ("Kitchen", self.kitchen),
            "3": ("Bedroom", self.bedroom),
            "4": ("Nursery", self.nursery),
            "5": ("Study", self.study),
            "6": ("Chapel", self.chapel),
            "7": ("Dining Room", self.dining_room),
            "8": ("Attic", self.attic),
            "9": ("Basement", self.basement),
        }

    # ------------------------------------------------------------------
    # Basic utility methods
    # ------------------------------------------------------------------

    def print_wrapped(self, text=""):
        if text:
            print(textwrap.fill(text, width=88))
        print()

    def pause(self):
        input("Press Enter to continue...")

    def divider(self):
        print("\n" + "-" * 72 + "\n")

    def ask_choice(self, prompt, choices):
        choices = [str(choice).lower() for choice in choices]

        while True:
            answer = input(prompt).lower().strip()
            if answer in choices:
                return answer
            print(f"Invalid input. Choose: {', '.join(choices)}")

    def ask_yes_no(self, prompt):
        answer = self.ask_choice(f"{prompt} [y/n]: ", ["y", "n"])
        return answer == "y"

    def add_item(self, name, description):
        if name in self.inventory:
            self.print_wrapped(f"You already have the {name}.")
            return

        self.inventory[name] = description
        print(f"\n**Collected: {name}**")
        self.print_wrapped(description)

    def add_clue(self, clue):
        self.clues.add(clue)

    def has_item(self, item):
        return item in self.inventory

    def has_clue(self, clue):
        return clue in self.clues

    def has_weapon(self):
        return self.has_item("Pocket Knife") or self.has_item("Rusted Knife")

    def show_inventory(self):
        self.divider()
        print("INVENTORY\n")

        if not self.inventory:
            print("Your inventory is empty.")
        else:
            for item, description in self.inventory.items():
                print(f"- {item}: {description}")

        print("\nCLUES FOUND\n")

        if not self.clues:
            print("No major clues found yet.")
        else:
            for clue in sorted(self.clues):
                print(f"- {clue}")

        self.divider()

    def random_house_event(self):
        events = [
            "Somewhere upstairs, a floorboard bends under a careful, patient weight.",
            "A woman's voice whispers from inside the wall: 'Not that room.'",
            "Your flashlight flickers once. In that brief darkness, something exhales nearby.",
            "The house settles around you, but the sound feels too deliberate, like a body shifting in sleep.",
            "For a second, the wallpaper pattern looks like rows of watching eyes.",
            "A cold draft brushes past your ear, carrying the faint smell of candle smoke.",
        ]

        if random.random() < 0.25:
            self.print_wrapped(random.choice(events))

    # ------------------------------------------------------------------
    # Main game flow
    # ------------------------------------------------------------------

    def start(self):
        self.introduction()

        while self.running:
            self.main_hall()

    def introduction(self):
        print("\nBEYOND THE SHADOW\n")
        print("11:43 PM\n")

        self.print_wrapped(
            "Rain fell over Harrisville, Rhode Island in thin silver lines. I was driving alone, "
            "thinking about money, health, relationships — all the usual private worries that grow "
            "teeth at night — when a loud BANG cracked behind the passenger seat."
        )

        self.print_wrapped(
            "The car lurched. I pulled over. Flat tire. No cell reception. The road behind me vanished "
            "into fog. Ahead, through the trees, a thin column of smoke rose into the dark."
        )

        self.print_wrapped(
            "Before leaving the car, I checked what I could bring with me."
        )

        if self.ask_yes_no("Take the Pocket Knife"):
            self.add_item("Pocket Knife", "A medium-sized foldable knife.")

        if self.ask_yes_no("Take the Small LED Flashlight"):
            self.add_item("Small LED Flashlight", "A small but bright rechargeable flashlight.")

        self.print_wrapped(
            "The walk toward the smoke was short, but the woods made it feel longer. Branches scratched "
            "against each other overhead. Halfway there, I found a thick branch near the path."
        )

        if self.ask_yes_no("Take the branch as a Hiking Pole"):
            self.add_item("Hiking Pole", "A sturdy wooden branch. Better than empty hands.")

        self.divider()
        print("12:26 AM\n")

        self.print_wrapped(
            "The smoke led me to an old historical house. The wood siding had rotted under peeling paint, "
            "though the roof looked strangely new. A brass plaque beside the front door read: "
            "THE ARNOLD ESTATE, BUILT 1736."
        )

        self.print_wrapped(
            "A woman's voice called from inside: 'You poor thing. Stranded in this weather? Come in, dear.' "
            "I could not see her. I could only see one dim window glowing above me."
        )

        self.print_wrapped(
            "The front door opened before I touched it."
        )

        self.print_wrapped(
            "Inside, the air smelled like damp wood, spoiled meat, and something burned. On the floor below "
            "a shoe rack sat a small wooden cross, blackened at the edges. A paper tag hung from it: "
            "Property of Ed and Lorraine Warren."
        )

        self.add_clue("Warren cross found")

        if self.ask_yes_no("Take the Warren Cross"):
            self.add_item(
                "Warren Cross",
                "A small scorched wooden cross labeled as property of Ed and Lorraine Warren."
            )

        self.print_wrapped(
            "The moment I stepped farther inside, the front door slammed shut behind me. The knob would "
            "not turn. Somewhere in the dark, the same gentle woman's voice whispered, 'She waits below.'"
        )

    def main_hall(self):
        self.random_house_event()

        print("Where should I go?\n")

        for key, room_data in self.rooms.items():
            room_name = room_data[0]
            print(f"{key}) {room_name}")

        print("i) Check inventory and clues")
        print("q) Quit game")

        choice = input("\nChoose: ").lower().strip()

        if choice == "i":
            self.show_inventory()
            return

        if choice == "q":
            if self.ask_yes_no("Are you sure you want to quit"):
                self.running = False
            return

        if choice in self.rooms:
            room_function = self.rooms[choice][1]
            room_function()
        else:
            print("Invalid choice. Try again.\n")

    def room_menu(self, room_name, options):
        while self.running:
            print(f"\n{room_name.upper()}\n")

            for index, option in enumerate(options, start=1):
                print(f"{index}) {option[0]}")

            print("0) Return to main hall")

            choice = input("\nChoose: ").lower().strip()

            if choice == "0":
                return

            if choice.isdigit():
                index = int(choice) - 1
                if 0 <= index < len(options):
                    option_function = options[index][1]
                    option_function()
                    continue

            print("Invalid choice. Try again.")

    # ------------------------------------------------------------------
    # Rooms
    # ------------------------------------------------------------------

    def parlor(self):
        if "Parlor" not in self.visited_rooms:
            self.visited_rooms.add("Parlor")
            self.print_wrapped(
                "The parlor looked almost beautiful: olive velvet couches, tiger-patterned wallpaper, "
                "amber lamps, and a marble fireplace. But the dust had been disturbed in the shape of "
                "bare feet."
            )
            self.print_wrapped(
                "Above the mantel hung a portrait of a family outside the house. Their faces were faded, "
                "except for the mother's eyes. Those had been scratched completely black."
            )

        self.room_menu(
            "Parlor",
            [
                ("Inspect the old black-and-white photograph", self.parlor_photo),
                ("Read the tattered book on the couch", self.parlor_book),
                ("Look inside the cold fireplace", self.parlor_fireplace),
            ],
        )

    def parlor_photo(self):
        if self.has_clue("Perron family photo"):
            self.print_wrapped(
                "The photograph still shows the same family. The torn space where the tallest child's face "
                "should be seems larger now."
            )
            return

        self.print_wrapped(
            "The photograph showed seven people dressed formally outside the Arnold Estate. On the back, "
            "someone had written: Perron Family, 1971."
        )
        self.print_wrapped(
            "Below that, in smaller handwriting, was one sentence: She chose the mother first."
        )

        self.add_clue("Perron family photo")

    def parlor_book(self):
        if self.has_clue("Perron haunting history"):
            self.print_wrapped(
                "You already read the marked chapter. The page now feels warm, like something alive."
            )
            return

        self.print_wrapped(
            "The book was titled Apparitions in New England. A marked chapter described the Perron family: "
            "cold rooms, voices, moving objects, and a presence that seemed especially focused on the mother."
        )
        self.print_wrapped(
            "Near the bottom of the page were the names Ed and Lorraine Warren. The final sentence had been "
            "underlined until the paper tore: The haunting did not begin with the family. It was waiting."
        )

        self.add_clue("Perron haunting history")

    def parlor_fireplace(self):
        if self.has_clue("Basement message"):
            self.print_wrapped(
                "The ash still spells the same word: BELOW. You avoid staring at it for too long."
            )
            return

        self.print_wrapped(
            "The fireplace was cold, but the ashes had been dragged into letters by something thin and "
            "careful: BELOW."
        )
        self.print_wrapped(
            "When you leaned closer, a single ember brightened under the ash, though there was no fire."
        )

        self.add_clue("Basement message")

    def kitchen(self):
        if "Kitchen" not in self.visited_rooms:
            self.visited_rooms.add("Kitchen")
            self.print_wrapped(
                "The kitchen was covered in dust, yet the sink overflowed with gray water. Pots and pans "
                "lay scattered across the floor, arranged almost like someone had tried to spell something "
                "and given up."
            )
            self.print_wrapped(
                "The refrigerator door hung open. Its bulb flickered without power. Something behind me "
                "breathed in when it flickered off."
            )

        self.room_menu(
            "Kitchen",
            [
                ("Take the rusted knife from the wall", self.kitchen_knife),
                ("Check the overflowing sink", self.kitchen_sink),
                ("Open the pantry door", self.kitchen_pantry),
            ],
        )

    def kitchen_knife(self):
        if self.has_item("Rusted Knife"):
            self.print_wrapped(
                "The empty outline of the knife remains on the wall, darker than the wallpaper around it."
            )
            return

        self.print_wrapped(
            "The knife was rusted nearly black. Along the handle, someone had carved a word so shallow "
            "you had to feel it with your thumb: CUT."
        )
        self.print_wrapped(
            "A whisper touched your ear: 'Not flesh. Rope.'"
        )

        if self.ask_yes_no("Take the Rusted Knife"):
            self.add_item("Rusted Knife", "Old, corroded, and unpleasantly heavy.")

    def kitchen_sink(self):
        if self.has_clue("Sink whisper"):
            self.print_wrapped(
                "The sink water is still. Too still. Your reflection refuses to blink."
            )
            return

        self.print_wrapped(
            "You reached toward the gray water. Something bumped the underside of your wrist from below "
            "the surface, though the basin was shallow."
        )
        self.print_wrapped(
            "A child's voice whispered from the drain: 'The key is where she sang.'"
        )

        self.add_clue("Sink whisper")

    def kitchen_pantry(self):
        if self.has_clue("Pantry warning"):
            self.print_wrapped(
                "The pantry door is still open. The smell coming from it has gotten worse."
            )
            return

        self.print_wrapped(
            "The pantry shelves were empty except for dozens of small jars. Each jar held a folded scrap "
            "of paper. Most were blank. One read: Do not answer the old woman."
        )
        self.print_wrapped(
            "From the hallway, the same kind old voice called, 'I can hear you in there.'"
        )

        self.add_clue("Pantry warning")

    def bedroom(self):
        if "Bedroom" not in self.visited_rooms:
            self.visited_rooms.add("Bedroom")
            self.print_wrapped(
                "The bedroom was colder than the hallway. Mold spread across the rose wallpaper in dark, "
                "branching veins. The bed was made perfectly, but the blanket sagged as if someone had "
                "just been lying beneath it."
            )
            self.print_wrapped(
                "On the dresser, a mirror faced the bed. Your reflection stood half a second too late."
            )

        self.room_menu(
            "Bedroom",
            [
                ("Read the journal page on the dresser", self.bedroom_journal),
                ("Look into the dresser mirror", self.bedroom_mirror),
                ("Check beneath the bed", self.bedroom_bed),
            ],
        )

    def bedroom_journal(self):
        if self.has_clue("Mother's journal"):
            self.print_wrapped(
                "The journal page has gone blank, except for a thumbprint that is not yours."
            )
            return

        self.print_wrapped(
            "The journal page was written by the Perron mother. The handwriting began neat, then shook "
            "apart line by line: She wore my face today. Roger said I looked tired. The girls asked why "
            "I was smiling at the wall."
        )
        self.print_wrapped(
            "The last line was pressed so hard into the paper that it nearly cut through: The Warrens said "
            "not to speak her name unless I was ready to make her listen."
        )

        self.add_clue("Mother's journal")

    def bedroom_mirror(self):
        if self.has_clue("Mirror apparition"):
            self.print_wrapped(
                "The mirror now reflects only the room. Somehow, that feels worse."
            )
            return

        self.print_wrapped(
            "You leaned toward the mirror. Behind your reflection, an old woman stood at the bedroom door. "
            "Her mouth moved before the words reached you."
        )
        self.print_wrapped(
            "'You came because you wanted to be chosen,' she said."
        )
        self.print_wrapped(
            "When you turned, the doorway was empty. In the mirror, she remained."
        )

        self.add_clue("Mirror apparition")

    def bedroom_bed(self):
        if self.has_clue("Scratches under bed"):
            self.print_wrapped(
                "The drag marks beneath the bed now point toward the bedroom door."
            )
            return

        self.print_wrapped(
            "Beneath the bed, the floorboards were scratched from the inside, as if someone below had tried "
            "to claw their way up."
        )
        self.print_wrapped(
            "Tucked between the boards was a torn strip of cloth. It smelled faintly of cellar damp and old smoke."
        )

        self.add_clue("Scratches under bed")

    def nursery(self):
        if "Nursery" not in self.visited_rooms:
            self.visited_rooms.add("Nursery")
            self.print_wrapped(
                "The nursery was small and pale. A crib sat in the corner beneath a mobile of wooden birds. "
                "The birds turned slowly, though the air was still."
            )
            self.print_wrapped(
                "In a rocking chair beside the crib sat a porcelain doll with a cracked smile and one painted eye. "
                "Around its neck hung a tiny locket."
            )

        self.room_menu(
            "Nursery",
            [
                ("Inspect the porcelain doll", self.nursery_doll),
                ("Search the crib", self.nursery_crib),
                ("Listen to the music box", self.nursery_music_box),
            ],
        )

    def nursery_doll(self):
        if self.has_clue("Bathsheba name"):
            self.print_wrapped(
                "The doll's broken pieces lie still. One painted eye continues to face the door."
            )
            return

        self.print_wrapped(
            "You opened the doll's locket. Inside was a slip of paper with one name written twice: "
            "Bathsheba. Bathsheba."
        )

        self.add_clue("Bathsheba name")

        self.print_wrapped(
            "The rocking chair creaked once. Then again. The doll turned its head toward you."
        )

        if self.has_weapon():
            self.print_wrapped(
                "The doll lunged for your throat. You barely got your blade up in time. Porcelain cracked "
                "against metal, and the sound it made was almost human."
            )
            self.print_wrapped(
                "When it fell, the room became silent except for the slow turning of the wooden birds above the crib."
            )
            self.add_clue("Doll survived")
        else:
            self.bad_doll_ending()

    def nursery_crib(self):
        if self.has_item("Cellar Key"):
            self.print_wrapped(
                "The crib is empty now. The blanket has been folded into the shape of a small cross."
            )
            return

        self.print_wrapped(
            "Inside the crib, beneath a yellowed blanket, you found a brass key tied to a red thread. "
            "The tag read: CELLAR."
        )
        self.print_wrapped(
            "From under the floor, something knocked twice. Then once more, softer."
        )

        self.add_item("Cellar Key", "A brass key tied to red thread. It opens the basement door.")

    def nursery_music_box(self):
        if self.has_clue("Music box warning"):
            self.print_wrapped(
                "The music box is silent now, but the melody keeps repeating in your head."
            )
            return

        self.print_wrapped(
            "The music box played three slow notes, then stopped. A child's voice finished the melody "
            "from inside the wall."
        )
        self.print_wrapped(
            "'She is not the mother,' the child whispered. 'She only wears them.'"
        )

        self.add_clue("Music box warning")

    def study(self):
        if "Study" not in self.visited_rooms:
            self.visited_rooms.add("Study")
            self.print_wrapped(
                "The study smelled of old paper and candle wax. A desk sat beneath a boarded window. "
                "Every drawer had been pulled open except one, which was nailed shut from the outside."
            )
            self.print_wrapped(
                "A tape recorder rested on the desk. Beside it lay a folder stamped WARREN — PRIVATE CASE NOTES."
            )

        self.room_menu(
            "Study",
            [
                ("Read the Warren case notes", self.study_case_notes),
                ("Play the tape recorder", self.study_tape),
                ("Open the nailed desk drawer", self.study_drawer),
            ],
        )

    def study_case_notes(self):
        if self.has_item("Warren Case Notes"):
            self.print_wrapped(
                "You already have the case notes. The folder feels colder each time you touch it."
            )
            return

        self.print_wrapped(
            "The notes described the Perron family's haunting: cold rooms, voices, apparitions, objects "
            "moving after prayer, and a presence the Warrens believed had attached itself to the land long "
            "before the family arrived."
        )
        self.print_wrapped(
            "One line was circled in Lorraine Warren's handwriting: It will answer to Bathsheba, but the name "
            "alone is not enough. Find the binding below. Cut the rope. Do not bargain."
        )

        self.add_item("Warren Case Notes", "Private notes warning that the binding is below the house.")
        self.add_clue("Binding must be cut")

    def study_tape(self):
        if self.has_clue("Lorraine tape"):
            self.print_wrapped(
                "The tape has snapped. A thin brown ribbon spills from the recorder like a dead vein."
            )
            return

        self.print_wrapped(
            "The recorder clicked on. Lorraine Warren's voice emerged beneath static: 'Ed, the house is "
            "not empty. It listens before it speaks.'"
        )
        self.print_wrapped(
            "A second voice, low and close to the microphone, whispered over her: 'I listened first.'"
        )

        self.add_clue("Lorraine tape")

    def study_drawer(self):
        if self.has_item("Single Match"):
            self.print_wrapped(
                "The drawer hangs open. The scratches inside now look fresh."
            )
            return

        self.print_wrapped(
            "You pried the drawer open. Inside, the wood was scratched with the same sentence over and over: "
            "SHE WAITS BELOW."
        )
        self.print_wrapped(
            "At the very back was a burnt matchbook from a church in Rhode Island. One match remained."
        )

        self.add_item("Single Match", "One dry match from an old church matchbook.")

    def chapel(self):
        if "Chapel" not in self.visited_rooms:
            self.visited_rooms.add("Chapel")
            self.print_wrapped(
                "The chapel was barely more than a converted sitting room. Crosses covered the walls, but "
                "several had been turned upside down. The pews faced a small altar where melted candles had "
                "hardened into shapes like bent fingers."
            )
            self.print_wrapped(
                "Something tapped from inside the confessional booth. Three taps. A pause. Three more."
            )

        self.room_menu(
            "Chapel",
            [
                ("Approach the altar", self.chapel_altar),
                ("Open the confessional booth", self.chapel_confessional),
                ("Study the upside-down crosses", self.chapel_crosses),
            ],
        )

    def chapel_altar(self):
        if self.has_item("Blessed Candle"):
            self.print_wrapped(
                "The altar is bare now. The wax stains look like fingerprints."
            )
            return

        self.print_wrapped(
            "A single candle remained unburned on the altar. Its label read: For the living, not the dead."
        )

        if self.ask_yes_no("Take the Blessed Candle"):
            self.add_item("Blessed Candle", "An unburned chapel candle.")

    def chapel_confessional(self):
        if self.has_clue("Confessional warning"):
            self.print_wrapped(
                "The confessional is empty now. A wet handprint remains on the inside of the door."
            )
            return

        self.print_wrapped(
            "Inside the booth, someone had carved a message into the kneeler: She confesses with other "
            "people's mouths."
        )
        self.print_wrapped(
            "A voice on the other side of the screen whispered, 'I forgive you.' Then, after a pause: "
            "'Now forgive me.'"
        )

        self.add_clue("Confessional warning")

    def chapel_crosses(self):
        if self.has_clue("Crosses point below"):
            self.print_wrapped(
                "The crosses remain still, but none of them cast shadows in the right direction."
            )
            return

        self.print_wrapped(
            "The upside-down crosses were not random. They pointed toward the floorboards, all angled "
            "slightly toward the basement door."
        )
        self.print_wrapped(
            "When you touched one, it corrected itself with a small wooden click. Somewhere below, something "
            "clicked back."
        )

        self.add_clue("Crosses point below")

    def dining_room(self):
        if "Dining Room" not in self.visited_rooms:
            self.visited_rooms.add("Dining Room")
            self.print_wrapped(
                "The dining room table was set for seven. Each plate held nothing but a ring of gray dust. "
                "At the head of the table sat an eighth chair, older than the rest."
            )
            self.print_wrapped(
                "The chandelier above the table swayed slightly, though the room had no breeze."
            )

        self.room_menu(
            "Dining Room",
            [
                ("Inspect the place cards", self.dining_place_cards),
                ("Look under the table", self.dining_under_table),
                ("Touch the eighth chair", self.dining_eighth_chair),
            ],
        )

    def dining_place_cards(self):
        if self.has_clue("Seven place cards"):
            self.print_wrapped(
                "The place cards are blank now, except for one that says YOUR SEAT."
            )
            return

        self.print_wrapped(
            "The place cards listed the Perron family members. The eighth card had no name. Instead, it said: "
            "The one who stayed."
        )

        self.add_clue("Seven place cards")

    def dining_under_table(self):
        if self.has_clue("Rope marks"):
            self.print_wrapped(
                "The rope marks are still there, cut deep into the underside of the table."
            )
            return

        self.print_wrapped(
            "Under the table, the wood was scarred by rope marks. Someone had tied something here for a long time."
        )
        self.print_wrapped(
            "The marks looked old, but a few splinters were fresh."
        )

        self.add_clue("Rope marks")

    def dining_eighth_chair(self):
        if self.has_clue("Eighth chair voice"):
            self.print_wrapped(
                "You keep your distance from the eighth chair. It seems to approve."
            )
            return

        self.print_wrapped(
            "You touched the eighth chair. The room went completely silent."
        )
        self.print_wrapped(
            "A voice spoke from the seat beside your ear: 'You may leave whenever you want. You simply will not.'"
        )

        self.add_clue("Eighth chair voice")

    def attic(self):
        if "Attic" not in self.visited_rooms:
            self.visited_rooms.add("Attic")
            self.print_wrapped(
                "The attic stairs groaned under your weight. The air up here was dry and close, packed "
                "with old trunks, rolled rugs, and furniture covered in white sheets."
            )
            self.print_wrapped(
                "At the far end, a small round window looked down over the driveway. For a moment, you saw "
                "your own car outside with its headlights on. Then lightning flashed, and it was gone."
            )

        self.room_menu(
            "Attic",
            [
                ("Look through the family trunk", self.attic_trunk),
                ("Inspect the covered furniture", self.attic_furniture),
                ("Read the child's drawing on the floor", self.attic_drawing),
            ],
        )

    def attic_trunk(self):
        if self.has_clue("They left, she stayed"):
            self.print_wrapped(
                "The trunk is empty now, but you hear something shifting beneath its false bottom."
            )
            return

        self.print_wrapped(
            "The trunk held old children's clothes and a newspaper clipping about the Perron family leaving "
            "the Arnold Estate. The article was normal, but the margin was not."
        )
        self.print_wrapped(
            "Someone had written: They left. She stayed."
        )

        self.add_clue("They left, she stayed")

    def attic_furniture(self):
        if self.has_clue("Stick figure bundle"):
            self.print_wrapped(
                "You leave the sheets alone. One of them rises and falls as if breathing."
            )
            return

        self.print_wrapped(
            "You pulled a sheet from a chair. Beneath it sat a woman-shaped bundle of sticks tied together "
            "with black thread."
        )
        self.print_wrapped(
            "It faced the basement door, though there was no way to see that door from here."
        )

        self.add_clue("Stick figure bundle")

    def attic_drawing(self):
        if self.has_clue("Child's drawing"):
            self.print_wrapped(
                "The drawing has changed. The stick figure at the cellar door is now holding a knife."
            )
            return

        self.print_wrapped(
            "The drawing showed the house as a child might draw it: square windows, crooked chimney, seven "
            "little figures outside. Beneath the house was an eighth figure, much taller than the rest."
        )
        self.print_wrapped(
            "It had no face. Above it, in red crayon, someone had written: Do not let her borrow your voice."
        )

        self.add_clue("Child's drawing")

    def basement(self):
        if not self.has_item("Cellar Key"):
            self.print_wrapped(
                "The basement door is locked. The keyhole is packed with red thread."
            )
            self.print_wrapped(
                "From the other side, a woman whispers, 'You found the house. Now find the key.'"
            )
            return

        self.print_wrapped(
            "The Cellar Key turned by itself before your hand finished moving. The basement door opened "
            "onto a stairway descending into cold, wet darkness."
        )
        self.print_wrapped(
            "Halfway down, your light caught old rope marks carved into the wall. At the bottom, crosses hung "
            "from the beams, turning slowly as if moved by underwater currents."
        )

        self.pause()

        if self.qualifies_for_good_ending():
            self.good_ending()
        elif self.qualifies_for_neutral_ending():
            self.neutral_ending()
        else:
            self.bad_basement_ending()

    # ------------------------------------------------------------------
    # Ending requirements
    # ------------------------------------------------------------------

    def qualifies_for_good_ending(self):
        required_clues = [
            "Perron family photo",
            "Perron haunting history",
            "Bathsheba name",
            "Binding must be cut",
            "Basement message",
        ]

        return (
            self.has_weapon()
            and self.has_item("Cellar Key")
            and self.has_item("Warren Case Notes")
            and all(self.has_clue(clue) for clue in required_clues)
        )

    def qualifies_for_neutral_ending(self):
        return (
            self.has_weapon()
            and self.has_item("Cellar Key")
            and self.has_clue("Bathsheba name")
        )

    def end_game(self, title, paragraphs):
        self.divider()
        print(title.upper())
        print()

        for paragraph in paragraphs:
            self.print_wrapped(paragraph)

        self.running = False

    def good_ending(self):
        extra = ""

        if self.has_item("Blessed Candle") and self.has_item("Single Match"):
            extra = (
                " You lit the chapel candle with the last match, and the flame burned blue instead of orange."
            )

        self.end_game(
            "Good Ending: The Binding Cut",
            [
                "In the basement, the woman from the portrait hung above the dirt floor, bound in ropes "
                "that vanished into the beams. Her eyes opened when you said the name from the doll's locket: "
                f"Bathsheba.{extra}",
                "The Warren notes were right. The name made the house listen, but the blade made it let go. "
                "You cut the ropes. The woman fell into your arms, gasping as if she had been drowning for years.",
                "The crosses stopped turning. The old woman's voice retreated into the walls, no longer sweet, "
                "no longer pretending.",
                "By dawn, you and the woman escaped through the front door as the Arnold Estate stood silent behind you.",
                "The nightmare is over — or at least, it has learned your name.",
                "THE END",
            ],
        )

    def neutral_ending(self):
        self.end_game(
            "Neutral Ending: You Escaped Alone",
            [
                "You had a blade, and you knew the name Bathsheba, but you did not fully understand the binding.",
                "When you spoke the name, the basement answered with every voice in the house.",
                "You slashed at the ropes, but the wrong ones. The woman screamed. The house screamed louder.",
                "The basement door flew open behind you, and you ran before the dark could choose a new shape.",
                "At sunrise, you stumbled onto the road alone. The police later found the Arnold Estate empty.",
                "No woman. No doll. No Warren notes. Just a basement full of cleanly cut rope.",
                "You survived, but something followed your voice home.",
                "THE END",
            ],
        )

    def bad_basement_ending(self):
        self.end_game(
            "Bad Ending: She Waits Below",
            [
                "The basement was colder than the rest of the house. At the center of the room, the woman "
                "from the portrait hung bound above the floor, her body twitching with each turn of the crosses.",
                "You searched for a way to help her, but you did not have what you needed.",
                "The old woman's voice came from directly behind you: 'You should not enter a house without "
                "learning who owns it.'",
                "The final cross turned upside down. Your flashlight died.",
                "By morning, the police found only your phone on the basement floor, still open to a map that "
                "showed no location.",
                "Somewhere upstairs, a porcelain doll began to rock.",
                "GAME OVER",
            ],
        )

    def bad_doll_ending(self):
        self.end_game(
            "Bad Ending: The Doll",
            [
                "The doll struck your chest with impossible weight. Its porcelain fingers tightened around "
                "your throat.",
                "You reached for a weapon that was not there.",
                "At 4:00 AM, your girlfriend stared at your unmoving location dot until it disappeared.",
                "The police found the house empty, except for a porcelain doll sitting upright in the rocking chair.",
                "GAME OVER",
            ],
        )


if __name__ == "__main__":
    game = Game()
    game.start()
