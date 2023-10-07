# Random Story Generator

# Import random module, to select settings for the story.
import random

# Get the reader's name.
reader_name = input("What is your name: ")

# Define random elements for the story (hero name, villain name, item, and NPC).
name_of_hero = random.choice(['Tarnished', 'Hollow', 'Wolf', 'Hunter'])
name_of_villain = random.choice(['The Nameless King', 'Orphan of Kos', 'Isshin', 'Margit'])
item = random.choice(["King's Sword", "Orphan's Ward", "Isshin's Spear", "Margit's Spells"])
npc = random.choice(["Melina", "Emma", "The Doll", "Ash"])

# Generate and display a random story.
print(f'''
Hi {reader_name},
Once upon a time in a land shrouded in mist.
A {name_of_hero} came out of a grave and set his foot in the world with the aim to remove this land's mist.
The lonely {name_of_hero} went alone to face the threat of the mist named {name_of_villain}.
A one-sided battle was fought with the victory going to the mist's ruler.
The {name_of_hero} then found {npc}, who cured & guided him to the right path.
It was told that in order to remove the mist of this land, {name_of_villain} had to be beaten,
and {item} is to be retrieved.
After relentless efforts by {name_of_hero} and with the help of {npc}, the final battle was fought between,
{name_of_hero} Vs. {name_of_villain}, after a long battle, the victory switched & {name_of_hero} won.
He retrieved {item} & the mist was all gone.
''')
