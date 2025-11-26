


class Soldier:

    def __init__(self,personal_number:int, f_name:str, l_name:str, gender:str,city:str, distance:int):
        self.personal_number = personal_number
        self.f_name = f_name
        self.l_name = l_name
        self.gender = gender
        self.city = city
        self.distance = distance
        self.status = None

    def to_dict(self):
        return {
            "personal_number": self.personal_number,
            "f_name": self.f_name,
            "l_name": self.l_name,
            "gender": self.gender,
            "city":self.city,
            "distance":self.distance,
            "status":self.status
        }

