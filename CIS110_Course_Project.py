print("Hello there!  I have an exciting tale to tell you about.")
print("Before we begin. I have a few questions I need you to answer.")
print("After typing your answer be sure to press the enter key.")
input ("\nPress the enter key to continue...")

seaTurtle = input("\nWhat would you like to name your sea turtle?  ")
oceanName =input("\nCan you name an ocean?  ")
islandName = input("\nWhat is an Island you want to vistit?  ")
number = input("\nWhat are last two digits of your birth year?  ")
favoriteBeach = input("\nWhat is the name of your favorite beach?  ")
turtleType = input("\nChoose a sea turtle type: green sea turtles, leatherback sea trutles, or loggerhead sea turtles.  ")

print("\nLets Go!!!  ")
print("\n")

print("\nOnce upon a time there was a beautiful", turtleType, "named", seaTurtle + ".")
print("\n", seaTurtle, "loved to play on the beach.  ")
print("\nOne day", seaTurtle, "was playing on the beach and the time passed him by quickly.  ")
print("\n", seaTurtle, "noticed he was no longer able to see his family.  ")
print("\nSo", seaTurtle, "searched all around the island and the beach. His family was no where around.  ")
print("\nHe then decideds to go search the", oceanName, "ocean in hopes of finding his family.  ")
print("\nAfter searching the", oceanName, "ocean for", number, "days.  ")
print("\n", seaTurtle, "comes across", islandName, "Island.  ")
print("\nHe wonders if his family could be at", favoriteBeach, "beach on", islandName, "Island.  ")

checkOutbeach = input("\nShould " + str(seaTurtle)+ " go check the beach for his fmaily?  Type yes or no:")
if checkOutbeach.lower() == "yes" :
    print("\n", seaTurtle, "decides to go to", islandName, "Island to search", favoriteBeach, "beach in hopes of finding his family.  ")
    print("\nOnce", seaTurtle, "arrives to", favoriteBeach, "beach and starts searching for his family.  ")
    print("\n", seaTurtle, "comes across", turtleType, ",just like him, and he gets distracted by playing with them, \nand he looses track of time.  ")
    print("\nBefore he knew it", seaTurtle, "had spent", number, "days on", islandName, "Island he begins to miss his family.  ")
    print("\nSo,", seaTurtle, "sets back out to the", oceanName, "ocean to search for him family.  ")
    print("\n",seaTurtle, "has searched the", oceanName, "ocean for", number, "weeks and still no sign of his family.  ")                               
    
else:
    print("\nAfter carefully thinking about it he decides not to seach", favoriteBeach, "on", islandName, "because he does not thing his family would be there. ")
    print(seaTurtle, "continues to search the", oceanName, "in hope that he will soon find his family that he has lost. ")

print("\nUntil one day while searching for his family", seaTurtle, " sees a family of", turtleType, "up ahead and is curious if they could be his family. ")
seaTurtlefamily =input("\nShould" + str(seaTurle)+ "check to see if the family of" +str(turtleType)+ "is his family or not? Type yes or no:")
if seaTurtlefamily.lower() == "yes" :
    print("\n",seaTurtle, "decides to check and see if they are his family.  ")
    print("\nAs",seaTurtle, "gets closer he soon realized that the family of", turtleType, "is his family he has been searching for.  ")
    print("\n",seaTurtle, "is happy he has finally found his family, and is not alone anymore.  ")
else:
    print("")

print("\nAfter traveling the", oceanName,"ocean", seaTurtle, "and his family decide to go to", islandName, "Island.  ")
print("\nTo make a home on", favoriteBeach, " beach, and live their remaining years happy together on", islandName, "Island.  ")




