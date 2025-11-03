## Imports.
from djitellopy import Tello




def move_the_drone(tello):
    tello.move_forward(20)
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
    move_the_drone(tello)
