from control_system.construction import add_soldier_to_room


class House:

    def __init__(self):
        self.rooms_houses = []


    def add_rooms_to_hous(self):
        room1, room2 = add_soldier_to_room()
        self.rooms_houses.append(room1)
        self.rooms_houses.append(room2)


    def get_rooms_houses(self):
        return self.rooms_houses

