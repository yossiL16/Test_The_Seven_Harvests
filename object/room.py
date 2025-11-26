from soldier import Soldier

class Room:

    def __init__(self):

        self.num_beds = 8
        self.beds = []

    def add_solider_to_room(self, solider:Soldier):

        if len(self.beds) < self.num_beds:
            self.beds.append(solider)
            return True
        else:
            return False

