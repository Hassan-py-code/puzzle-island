

# puzzle island

print("""

░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗  ████████╗░█████╗░  ███╗░░░███╗██╗░░░██╗
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝  ╚══██╔══╝██╔══██╗  ████╗░████║╚██╗░██╔╝
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░  ░░░██║░░░██║░░██║  ██╔████╔██║░╚████╔╝░
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░  ░░░██║░░░██║░░██║  ██║╚██╔╝██║░░╚██╔╝░░
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗  ░░░██║░░░╚█████╔╝  ██║░╚═╝░██║░░░██║░░░
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝  ░░░╚═╝░░░░╚════╝░  ╚═╝░░░░░╚═╝░░░╚═╝░░░

██╗░██████╗██╗░░░░░░█████╗░███╗░░██╗██████╗░██╗
██║██╔════╝██║░░░░░██╔══██╗████╗░██║██╔══██╗██║
██║╚█████╗░██║░░░░░███████║██╔██╗██║██║░░██║██║
██║░╚═══██╗██║░░░░░██╔══██║██║╚████║██║░░██║╚═╝
██║██████╔╝███████╗██║░░██║██║░╚███║██████╔╝██╗
╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░╚═╝
""")

door_color = input("""There are tow doors in front of you. 🚪 red door and a 🚪 blue door
which door do you want to open?\n""").lower()


if door_color == "red":
    print('Great!now you entered a room.')
    box = input("""You found three boxes:🎁 white,🎁 yellow,🎁 green
which box do you open:\n""").lower()

    if box == "yellow":
        print("opps! you opened a box filled with  Crocodile 🐊🐊🐊🐊🐊")
    elif box == "green":
        print('Opps! you opened a box filled with lion 🦁🦁🦁🦁🦁')
    elif box == "white":
        print("Gongratulations!you found the treasure!💰💰💰💰💰💰")
    
    else:
        print('Invalid choice!🤷‍♂️🤷‍♂️🤷‍♂️🤷‍♂️')

elif door_color=="blue":
       print("""Oops!you chose the snak door
Game over! 🐍🐍🐍🐍🐍🐍🐍🐍🐍""")



else:
     print('Invalid choice!🤷‍♂️🤷‍♂️🤷‍♂️🤷‍♂️')

