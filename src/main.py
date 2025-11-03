## Imports.
from djitellopy import Tello




def move_the_drone(tello):
    tello.move_forward(20)    


def first_fight(self,tello):
    tello.connect()
    tello.takeoff()
    battery = tello.get_battery()
    print(battery)
    tello.land()



if __name__ == '__main__':
    tello = Tello()
    tello.connect()
    tello.takeoff()
    first_fight(tello)
