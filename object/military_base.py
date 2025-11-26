from house import House

class Military_base:

    def __init__(self):
        self.houses = []

    def add_house(self, house:House):
        self.houses.append(house)
        return self.houses