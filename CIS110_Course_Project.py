print("Hello there!  I have an exciting tale to tell you about.")
print("Before we begin. I have a few questions I need you to answer.")
print("After typing your answer be sure to press the enter key.")
input ("\nPress the enter key to continue...")

seaTurtle = input("\nWhat would you like to name your sea turtle?  ")
oceanName =input("\nCan you name an ocean?  ")
islandName = input("\nWhat is an Island you want to visit?  ")
number = input("\nWhat are last two digits of your birth year?  ")
favoriteBeach = input("\nWhat is the name of your favorite beach?  ")
turtleType = input("\nChoose a sea turtle type: green sea turtles, leatherback sea trutles, or loggerhead sea turtles.  ")

print("\nLets Go!!!  ")
print("\n")

print("\nOnce upon a time there was a beautiful", turtleType, "named", seaTurtle + ".")
print("\n", seaTurtle, "loved to play on the beach.  ")
print("\nOne day", seaTurtle, "was playing on the beach and the time passed him by quickly.  ")
print("\n", seaTurtle, "noticed he was no longer able to see his family.  ")
print("\nSo", seaTurtle, "searched all around the island and the beach. His family was nowhere around.  ")
print("\nHe then decides to go search the", oceanName, "ocean in hopes of finding his family.  ")
print("\nAfter searching the", oceanName, "ocean for", number, "days.  ")
print("\n", seaTurtle, "comes across", islandName, "Island.  ")
print("\nHe wonders if his family could be at", favoriteBeach, "beach on", islandName, "Island.  ")

checkOutbeach = input("\nShould " + str(seaTurtle)+ " go check the beach for his fmaily?  Type yes or no:")
if checkOutbeach.lower() == "yes" :
    print("\n", seaTurtle, " decides to go to ", islandName, " Island to search ", favoriteBeach, " beach in hopes of finding his family.  ")
    print("\nOnce", seaTurtle, "arrives to", favoriteBeach, "beach and starts searching for his family.  ")
    print("\n", seaTurtle, "comes across", turtleType, ",just like him, and he gets distracted by playing with them, \nand he loses track of time.  ")
    print("\nBefore he knew it", seaTurtle, "had spent", number, "days on", islandName, "Island he begins to miss his family.  ")
    print("\nSo,", seaTurtle, "sets back out to the", oceanName, "ocean to search for him family.  ")
    print("\n",seaTurtle, "has searched the", oceanName, "ocean for", number, "weeks and still no sign of his family.  ")                               
    
else:
    print("\nAfter carefully thinking about it he decides not to seach ", favoriteBeach, " on ", islandName, " because he does not thing his family would be there. ")
    print("\n", seaTurtle, " continues to search the ", oceanName, " in the hope that he will soon find his family that he has lost. ")

print("\nUntil one day while searching for his family ", seaTurtle, " sees a family of ", turtleType, " up ahead and is curious if they could be his family. ")
seaTurtlefamily =input("\nShould " + str(seaTurtle)+ " check to see if the family of " + str(turtleType)+ " is his family or not? Type yes or no:")

if seaTurtlefamily.lower() == "yes" :
    print("\n",seaTurtle, " decides to check and see if they are his family.  ")
    print("\nAs ",seaTurtle, " gets closer, he soon realized that the family of " + str(turtleType)+ " is the family he has been searching for.  ")
    print("\n",seaTurtle, " is happy he has finally found his family and is not alone anymore.  ")
else:
    print("\n", seaTurtle, " decides not to check because the family of " + str (turtleType)+ " does not look like his family. ")
    print("\n", seaTurtle, " continues his search for the family that he has lost.  ")


if checkOutbeach.lower() == "yes" and seaTurtlefamily.lower() == "yes":
    print("\nAfter traveling the " + str(oceanName)+ " ocean " + str(seaTurtle)+  " and his family decide to go to " + str(islandName)+ " Island.  ")
    print("\nTo make a home on " + str(favoriteBeach)+ " beach, and live their remaining years happy together on " + str(islandName)+ " Island.  ")
elif checkOutbeach.lower() == "yes":
    print("\nAfter playing and makeing new friends at " + str(islandName)+ " and searching the " + str(oceanName)+ " for " + str(number)+ " years. ")
    print("\nStill unable to find his family " + str(seaTurtle)+ " decides to go back to the " + str(islandName)+ " and be with his friend there on " + str(favoriteBeach)+ ".")
    print("\nSo " + str(seaTurtle)+ " is not all alone."  )
else:
    print("\nAfter deciding to not search " + str(islandName)+ " and keep searching the " + str(oceanName)+ " for his family.  ")
    print("\n", seaTurtle, " continues to search until he finds his lost family. He will search even if it takes " + str(number)+ " years.  ")
    print("\n", seaTurtle, " is not going to give up on finding his family.  " )

