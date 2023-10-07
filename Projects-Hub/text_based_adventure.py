# Start of the Story.
print('''
While completing a hike trip through the woods, Martin heard a low-frequency noise from his left.
''')

# Ask the user if Martin should follow the strange voice (Yes or No).
decision1 = input("Should Martin follow the voice? (Y / N): ").upper()

if decision1 == "Y":  # If the user chooses 'Y' (Yes)...
    print('''
Martin stops and follows the strange voice.''')
    print('''
While following the strange voice, Martin finds out that the origin of the voice is from a tree right in front.
''')

    # Ask the user if Martin should investigate further (Yes or No).
    decision2 = input("Should Martin investigate further? (Y / N): ").upper()

    if decision2 == "Y":  # If the user chooses 'Y' (Yes)...
        print('''
Martin puts down his belongings and climbs the tree.
He is surprised to find his parrot named "Peter," that he lost a few years back.
''')

        # Ask the user if Martin should take the parrot back home (Yes or No).
        decision3 = input("Martin cries, should he take the parrot back home? (Y / N): ").upper()

        if decision3 == "Y":  # If the user chooses 'Y' (Yes)...
            print('''
Martin and Peter walk towards the car parked near the highway.
A slight tension can be seen on Martin's face. Who knows why?
''')

        elif decision3 == "N":  # If the user chooses 'N' (No)...
            print('''
Martin is reluctant and leaves Peter.
Peter cries Martin's name as Martin walks away with tears in his eyes.
(Reason: Martin's sister is afraid of parrots!)
''')

        else:
            print("Martin is confused!")  # Handle any other input.

    elif decision2 == "N":  # If the user chooses 'N' (No)...
        print('''
Martin walks away, without knowing what the strange voice was.''')

    else:
        print("Martin is confused!")  # Handle any other input.

elif decision1 == "N":  # If the user chooses 'N' (No)...
    print('''
Martin keeps on his track to head towards his car parked near the highway.''')
else:
    print('''
Martin is confused!''')  # Handle any other input.
