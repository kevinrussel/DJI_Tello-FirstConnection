## Imports.
from djitellopy import Tello




def first_fight():
    tello = Tello()
    tello.connect()
    tello.takeoff()
    battery = tello.get_battery()
    print(battery)
    tello.land()



if __name__ == '__main__':
    first_fight()
    