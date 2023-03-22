from arm_6axis import Arm_6
import time
PIN_LIST = [16, 17, 18, 19, 20, 21]

DIR_LIST = [0, 0, 0, 0, 0, 0]
arm = Arm_6(PIN_LIST, DIR_LIST)

# move to origin
arm.set_single_angle (0,0)
arm.set_single_angle (1,0)
arm.set_single_angle (2,0)
arm.set_single_angle (3,0)
arm.set_single_angle (4,0)
arm.set_single_angle (5,0)
arm.flesh ()
print(arm.pos_report())

arm.set_single_angle (1,-20); arm.flesh()
arm.set_single_angle (2,30); arm.flesh()
arm.set_single_angle (3,-30); arm.flesh()
arm.set_single_angle (4,-90); arm.flesh()

time.sleep(10)

arm.set_single_angle (4,0); arm.flesh()
arm.set_single_angle (3,-50); arm.flesh()
arm.set_single_angle (2, 74); arm.flesh()
