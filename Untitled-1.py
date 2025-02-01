class Room:
    def __init__(self, name, description, items=None, connected_rooms=None):
        self.name = name
        self.description = description
        self.items = items if items is not None else []
        self.connected_rooms = connected_rooms if connected_rooms is not None else {}

    def describe(self):
        print(f"You are in the {self.name}.")
        print(self.description)
        if self.items:
            print("You see the following items: " + ", ".join(self.items))
        if self.connected_rooms:
            print("You can go to: " + ", ".join(self.connected_rooms.keys()))

    def get_item(self, item):
        if item in self.items:
            self.items.remove(item)
            return item
        else:
            return None

class Game:
    def __init__(self):
        self.inventory = []
        self.current_room = None
        self.rooms = self.create_rooms()

    def create_rooms(self):
        rooms = {
            "Entrance": Room("Entrance", "A dark and eerie entrance with a faint red glow.", items=["flashlight"], connected_rooms={"Hallway": "hallway"}),
            "Hallway": Room("Hallway", "A long, dimly lit hallway with shadows dancing on the walls.", connected_rooms={"Entrance": "entrance", "Library": "library"}),
            "Library": Room("Library", "A dusty old library with books scattered everywhere.", items=["old book"], connected_rooms={"Hallway": "hallway"})
        }
        rooms["Entrance"].connected_rooms["Hallway"] = rooms["Hallway"]
        rooms["Hallway"].connected_rooms["Entrance"] = rooms["Entrance"]
        rooms["Hallway"].connected_rooms["Library"] = rooms["Library"]
        rooms["Library"].connected_rooms["Hallway"] = rooms["Hallway"]
        return rooms

    def start(self):
        self.current_room = self.rooms["Entrance"]
        self.current_room.describe()
        while True:
            command = input("> ").strip().lower()
            if command in ["quit", "exit"]:
                print("You decide to leave the dark place. Goodbye!")
                break
            elif command.startswith("go to "):
                destination = command.split(" ", 2)[2]
                if destination in self.current_room.connected_rooms:
                    self.current_room = self.current_room.connected_rooms[destination]
                    self.current_room.describe()
                else:
                    print("You can't go that way.")
            elif command.startswith("take "):
                item = command.split(" ", 1)[1]
                taken_item = self.current_room.get_item(item)
                if taken_item:
                    self.inventory.append(taken_item)
                    print(f"You took the {taken_item}.")
                else:
                    print("You can't take that.")
            elif command == "inventory":
                print("You have: " + ", ".join(self.inventory))
            else:
                print("Unknown command.")

if __name__ == "__main__":
    game = Game()
    game.start()
    
def factorial(n):
    if n == 0:
            return 1
                else:
                        return n * factorial(n-1)

                        number = 5
                        print("The factorial of", number, "is", factorial(number))
            
