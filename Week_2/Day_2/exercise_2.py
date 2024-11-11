class Door():
    def __init__(self, is_opened = True):
        self.is_opened = True

    def open_door(self):
        if self.is_opened:
            print("The door was already open.")
        else:
            print("The door is now open.")
            self.is_opened = True

    def close_door(self):
        if self.is_opened:
            print("The door is now closed.")
            self.is_opened = False
        else:
            print("The door is already closed.")

class BlockedDoor(Door):
    def open_door(self):
        raise Exception('Blocked door cannot be open')

    def close_door(self):
        raise Exception('Blocked door can  not be closed')

door1 = Door()
door2 = BlockedDoor

door2.close_door()