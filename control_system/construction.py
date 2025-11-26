from control_system.queries import get_db_for_order,get_db_connection
# from object.house import House
# from object.room import Room
from object.room import Room

def add_soldier_to_room():
    received, on_hold= get_db_for_order()
    room1 = [received[0:8], received[8:16], received[16:24],received[24:32], received[32:40], received[40:48], received[48:56], received[56:64], received[64:72], received[72:80]]
    room2 = [received[80:88], received[88:96], received[96:104],received[104:112], received[112:120], received[120:128], received[128:136], received[136:144], received[144:152], received[152:160]]
    return room1, room2