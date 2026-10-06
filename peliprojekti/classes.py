class Item:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

class Player:

    def __init__(self, name):
        self.name = name
        self.items = []
        self.current_room = None

    def move(self,room):
        self.current_room=room

    def collect_item(self,):
        if self.current_room.item:
            self.items.append(self.current_room.item)
            self.current_room.item = None


class Room:

    def __init__(self, name,item):
        
        self.name = name
        self.item=item

