mydictionary = {"Kojo": "0540912245",
                "Kwame": "0244020103",
                "Ama": "0247678787"}
newcontact = input("Enter your name ")
newdigits = input("Enter your digits ")
mydictionary[newcontact] = newdigits
print(mydictionary)


colour = ["red", "blue", "green"]
counter = 0
while counter < 3:
    print(colour[counter])
    counter += 1

while True:
    print("this script will not stop")


rgb = ["red", "blue", "green"]
for color in rgb:
    print("current color is " + color)

# Display contents of dictionary
contacts = {"Kojo": "0540912245",
            "Kwame": "0244020103",
            "Ama": "0247678787"}
for contact, phnum in contacts.items():
    print(contact + " has " + phnum + " as his/her phone number")
