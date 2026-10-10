class Item:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

class Player:
    def __init__(self, name):
        self.name = name
        self.items = []
        self.current_room = None

    def move(self, room):
        self.current_room = room

    def collect_item(self):
        if self.current_room.item:
            self.items.append(self.current_room.item)
            self.current_room.item = None

    def save_game(self, clues):
        with open("savegame.txt", "w") as file:
            file.write(self.name + "\n")

            if self.current_room:
                file.write(self.current_room.name + "\n")
            else:
                file.write("None\n")

            for item in self.items:
                file.write(item.name + "\n")

            file.write("Clues:\n")

            for clue in clues:
                file.write(clue + "\n")

            
    def load_game(self, rooms, clues):
        with open("savegame.txt", "r") as file:
            name = file.readline().strip()
            room_name = file.readline().strip()

            self.name = name

            for room in rooms:
                if room.name == room_name:
                    self.current_room = room

            line = file.readline().strip()

            while line != "Clues:" and line != "":
                for room in rooms:
                    if room.item and room.item.name == line:
                        self.items.append(room.item)
                        room.item = None

                line = file.readline().strip()

            while line != "":
                line = file.readline().strip()
                if line != "":
                    clues.append(line)




class Room:

    def __init__(self, name,item):
        
        self.name = name
        self.item=item

