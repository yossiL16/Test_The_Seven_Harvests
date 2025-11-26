from room import Room

class House:

    def __init__(self):
        self.rooms = []
        self.num_rooms = 10

    def add_rooms_to_hous(self, room:Room):

        if len(self.rooms) < self.num_rooms:
            self.rooms.append(room)
            return True
        else:
            return False

