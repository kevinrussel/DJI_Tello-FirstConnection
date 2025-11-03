## Imports.
from djitellopy import Tello




def square(tello):
    tello.move_forward(100)
    tello.move_left(100)
    tello.move_back(100)
    tello.move_right(100)
    tello.land()
    

def first_fight(tello):
    print(tello.get_battery())
    tello.land()


0
if __name__ == '__main__':
    tello = Tello()
    tello.connect()
    tello.takeoff()
    # first_fight(tello)
    square(tello)
