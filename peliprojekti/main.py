from functions import *
from classes   import Player, Item, Room
from pathlib import Path

def read_text_file(filename):
    file_path = Path(__file__).parent / filename

    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
        print(text)



name= input("what is ur name") 
age= int(input("what is ur age"))
print()
player = Player(name)

print()
print("hello your name is",name,"and your age is",age)
print()
if age < 12:
     print("you are a minor")
     exit()

# objects
player = Player(name)

item1 = Item("working gloves", 0.2)
item2 = Item("access card", 2)
item3 = Item("security log", 5)

entrance = Room("Entrance", None)
main_hall = Room("Main Hall", None)
security_desk = Room("Security Desk", item3)
security_room = Room("Security Room", item2)
diamond_display = Room("Diamond Display", item1)

rooms = [entrance, main_hall, security_desk, security_room, diamond_display]

game_started = False

while True:
    print("Welcome to the main menu")
    print()

    if game_started == False:
        print("1. Start")
        print("2. Quit")

    else:
        print("1. Talk")
        print("2. Search")
        print("3. move")
        print("4. collect item")
        print("5.clues")
        print("6.accuse")
        print("7. Save game and Quit")
        print("8. load game")
        print("9. Quit")

    print()
    command = input("Enter a command: ")

    if game_started == False:

        if command == "1":
            read_text_file("intro.txt")
            print()
            read_text_file("ohjeet.txt")
            print()
            start_game()
            print()
            game_started = True

        elif command == "2":
            break

    else:

        if command == "1":
            talk_to_people(player,rooms)

        elif command == "2":
            search_museum(player, rooms,clues)

        elif command == "3":
             move_player(player,rooms)

        elif command == "4":
            collect_item(player)

        elif command == "5":
           show_clues()

        elif command=="6":
           accuse_someone()

        elif command=="7":
            player.save_game(clues)
            print("Game saved. Goodbye!")
            break

        elif command=="8":
            player.load_game(rooms, clues)
            print("Game loaded!")
            print("Welcome back,", player.name)

        elif command=="9":
            print("Goodbye!")
            break
 

