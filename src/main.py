from time import sleep
from djitellopy import Tello

t = Tello(retry_count=1)
t.LOGGER.setLevel("DEBUG")
t.connect()                 # puts drone in SDK 'command' mode
sleep(1.0)                  # give sensors a beat
print("Battery:", t.get_battery())
print("Temp:", t.get_temperature())
print("Height:", t.get_height())
t.takeoff()
t.send_rc_control(0,0,0,0)
t.land()
t.end()