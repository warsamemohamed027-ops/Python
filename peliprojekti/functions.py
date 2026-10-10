clues = []


def start_game():
    print("You are now ready to investigate the museum and find out who stole the diamond.")
    print("What do you want to do first?")

def search_museum(player, rooms, clues):

    if player.current_room == rooms[0]:  # Room 1 - Entrance
        print("You search the entrance.")
        print()
        print("You don't find anything useful.")

    elif player.current_room == rooms[1]:  # Room 2 - Main Hall
        print("You search the main hall.")
        print()
        print("You don't find anything useful.")

    elif player.current_room == rooms[2]:  # Room 3 - Security Desk
        print("You search the security desk.")
        print()
        print("You find a security log!")
        print("The log shows the scheduled locations of the staff.")
        print()
        print("Technician - Security Room, 7:00-7:20")
        print()
        print("security guard - Security Desk, 7:00-7:30")
        print()
        print("museum employee - Main Hall, 7:00-7:30")
        print()
        print("You remember the technician said he was working around the diamond display.")
        print("Something doesn't add up.")
        print()

        clues.append("The technician's story does not match the security log")

    elif player.current_room == rooms[3]:  # Room 4 - Security Room
        print("You search the security room.")
        print()
        print("You don't find anything useful.")

    elif player.current_room == rooms[4]:  # Room 5 - Diamond Display
        print("You search around the diamond display.")
        print()
        print("You find a working glove!")
        print("It appears to belong to the technician.")
        print()

        clues.append("A working glove was found near the diamond display")

def talk_to_people(player,rooms):

    # if player.current_room == rooms[1]:
    #  print("The museum employee is here.")

    # print("1. security guard")
    # print("2. museum employee")
    # print("3. wealthy visitor")
    # print("4. technician")
    # print()

    if player.current_room == rooms[1]:
        print("Who do you want to talk to?")
        print("1. Museum employee")
        print("2. Wealthy visitor")
        choice = input("Choose a person: ")

        if choice == "1":
            person = "2"
        elif choice == "2":
            person = "3"
        else:
            print("Invalid choice.")
            return

    elif player.current_room == rooms[2]:
        person = "1"

    elif player.current_room == rooms[4]:
        person = "4"

    else:
        print("There is nobody here to talk to.")
        return

    if person == "1":
        print("You approach the security guard.")
        print()
        print("I saw someone near the diamond display", "He says.")
        print("They used an access card to enter the restricted area.")
        print()
        if "access card clue" not in clues:
            clues.append("access card clue")
        print("Clue collected: someone used an access card to get close to the diamond.")

    elif person == "2":
        print("You approach the museum employee.")
        print()
        print('"I noticed the wealthy visitor asking questions about the diamond," He says.')
        print('"He seemed very interested in it."')
        print()
        print('"The security system was also put into maintenance mode."')
        print("You wonder who would do that.")
        print()
        if "maintenance mode clue" not in clues:
         clues.append("maintenance mode clue")
        print("Clue collected: the security was in maintenance mode")

    elif person == "3":
        print("You approach the wealthy visitor.")
        print()
        print("You heard from the museum employee that he has been asking questions about the diamond.")
        print("You ask him about it.")
        print("I was only interested in the diamond", "He says.")
        print()
        print("I was here yesterday at 7.30pm; it was still there when I left.")
        if "timing clue" not in clues:
         clues.append("timing clue")
        print()
        print("Clue collected: The diamond was still there at 7.30pm,30 minutes before the museum closes.")

    elif person == "4":
        print("You approach the technician.")
        print()
        print("I was working around the diamond display yesterday", "He says.")
        print("I noticed one of my working gloves was missing.")
        print()
        print("You wonder if the thief used the gloves to steal the diamond.")
        if "working gloves" not in clues:
            clues.append("working gloves")
        print()
        print("Clue collected: Working gloves.")

    else:
        print("Invalid choice.")


def accuse_someone():
    print("1. security guard")
    print("2. museum employee")
    print("3. wealthy visitor")
    print("4. technician")

    person = input("Who do you want to accuse? ")

    if person == "1":
        print("You accuse the security guard.")
        print()
        print("His access card showed he was at his post so he was accounted for.")
        print()
        print("your accusation was wrong")
        print()
        print("Game over")
        exit()

        
    elif person == "2":
        print("You accuse the museum employee.")
        print()
        print("The cameras show he was helping customers at the time of the theft")
        print()
        print("your accusation was wrong")
        print()
        print("Game over")
        exit()

    elif person == "3":
        print("You accuse the wealthy visitor.")
        print()
        print("He says he was only interested in the diamond and was still there at 7.30pm.")
        print("the cameras show him leaving at 7.40pm. 20 minutes before the museum closed and the diamond was still there.")
        print()
        print("your accusation was wrong")
        print()
        print("Game Over")
        exit()

    elif person == "4":
        print("The technician was the Thief.")
        print()
        print("The security log showed that his story did not match his location.")
        print("The security system had been placed into maintenance mode.")
        print("His gloves were connected to the diamond display.")
        print("And he had access to both the security system and the restricted area.")
        print()
        print("congratulations! you have solved the case.")
        exit()

    else:
        print("Invalid choice.")


def show_clues():
    if clues:
        print("Clues collected:")
        for clue in clues:
            print("-", clue)
    else:
        print("no clues collected yet")


def move_player(player,rooms):
    print("Where do you want to go?")
    print("1. Entrance")
    print("2. Main Hall")
    print("3. Security Desk")
    print("4. Security Room")
    print("5. Diamond Display")

    choice=input("Choose a Room")

    if choice == "1":
        player.move(rooms[0])
        print("You enter the museum entrance.")
       

    elif choice == "2":
        player.move(rooms[1])
        print("You enter the Main hall.")
        print()
        print("The museum employee is here.")
    elif choice == "3":
        player.move(rooms[2])
        print("you arrive at the Security Desk.")
        print()
        print("The security guard is here.")

    elif choice == "4":
        player.move(rooms[3])
        print()
        print("you enter the Security Room.")
        print("The technican is working nearby.")

    elif choice == "5":
        player.move(rooms[4])
        print("You arrive at the Diamond display.")
        print()
    



    
def collect_item(player):
    if player.current_room is None:
        print("You need to move to a room first.")
        return

    if player.current_room.item is not None:
        item = player.current_room.item
        player.collect_item()
        print("You collected:", item.name)
    else:
        print("There is no item to collect here.")

    
          