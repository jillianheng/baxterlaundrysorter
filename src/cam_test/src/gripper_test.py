#!/usr/bin/env python
import rospy
from baxter_interface import gripper as baxter_gripper

rospy.init_node('gripper_test')

#Set up the right gripper
right_gripper = baxter_gripper.Gripper('right')

# #Calibrate the gripper (other commands won't work unless you do this first)
# print('Calibrating...')
# right_gripper.calibrate()
# rospy.sleep(2.0)

#Close the right gripper
print('Closing...')

while True:
	right_gripper.close(block=False)
# rospy.sleep(1.0)

# #Open the right gripper
# print('Opening...')
# right_gripper.open(block=True)
# rospy.sleep(1.0)
# print('Done!')

