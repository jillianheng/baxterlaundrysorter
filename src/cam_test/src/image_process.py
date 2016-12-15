#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
from cam_test.srv import ImageSrv, ImageSrvResponse
import cv2, time, sys
from cv_bridge import CvBridge, CvBridgeError
import numpy as np
from numpy.linalg import *
import math
import tf
import time

#for path planning/movement
import moveit_commander
from moveit_msgs.msg import OrientationConstraint, Constraints
from geometry_msgs.msg import PoseStamped, Pose, Vector3, Quaternion
from baxter_interface import gripper as baxter_gripper
from std_msgs.msg import String, Int16MultiArray
from sensor_msgs.msg import Image


#refPt=[(469, 273), (789, 514)]
val=50

#Hardcode positions of clothes
clothes1top = [0.783, 0.538, 0.223,0.999,-0.028, 0.015, -0.009]
clothes2top = [0.764, 0.357, 0.233, 1.000, -0.003, -0.024, 0.018]
clothes3top = [0.796, 0.107, 0.295, -0.000, 1.000, 0.004, -0.007]

clothes1bot = [0.782, 0.581, -0.026, 0.999, 0.014, -0.031, 0.018]
clothes2bot = [0.762, 0.359, -0.043, 0.999, -0.028, 0.016, 0.006]
clothes3bot = [0.790, 0.127, -0.069, -0.037, 0.995, 0.023, -0.088]

#Hardcode positions of baskets
basket1 = [0.006, 0.771, 0.263, -0.487, 0.873, -0.001, -0.035]
basket2 = [0.396, 0.781, 0.238, 0.755, -0.656, 0.011, 0.020]


# Create a CvBridge to convert ROS messages to OpenCV images
bridge = CvBridge()

# Converts a ROS Image message to a NumPy array to be displayed by OpenCV
def ros_to_np_img(ros_img_msg):
  return np.array(bridge.imgmsg_to_cv2(ros_img_msg,'bgr8'))

def capture_image():
  try:
    # Request the last image from the image service
    # And extract the ROS Image from the ImageSrv service
    # Remember that ImageSrv.image_data was
    # defined to be of type sensor_msgs.msg.Image

    ros_img_msg = last_image_service().image_data

    # Convert the ROS message to a NumPy image
    np_image = ros_to_np_img(ros_img_msg)

    # Display the processed CV Image
    #cv2.imshow("CV Image", np_image)
    #np_image=np_image[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
    dark = check_image(cropimage(np_image))

    return dark 

    while True:
      if rospy.is_shutdown():
        raise KeyboardInterrupt
      cv2.waitKey(10)

  except KeyboardInterrupt:
    print 'Keyboard Interrupt, exiting'
    return

    # Catch if anything went wrong with the Image Service
  except rospy.ServiceException, e:
    print "image_process: Service call failed: %s"%e
    
  cv2.destroyAllWindows()

def cropimage(image):
  #because image.shape[0] gives the number of rows
  centerheight = 0.5*image.shape[0]
  #because image.shape[1] gives the number of columns
  centerwidth = 0.5*image.shape[1]
  #because cropping an image needs to be done in a y,x format
  newimage = image[centerheight-val:centerheight+val, centerwidth-val:centerwidth+val]
  #cv2.imshow("Cropped",newimage)
  return newimage

def check_image(image):
  
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  blurred = cv2.medianBlur(gray, 5)
  ret, thresh = cv2.threshold(blurred, 90, 255, cv2.THRESH_BINARY_INV)
  #cv2.imshow('Blurred image', gray)
  contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

  average_color_row =  np.average(gray, axis=0)
  average_color = np.average(average_color_row, axis = 0)
  average_color=np.uint8(average_color)
  average_color_img = np.array([[average_color]*100]*100, np.uint8)
  cv2.imwrite("average_color.png", average_color_img)
  #cv2.imshow("Final image", average_color_img)

  #print(average_color)
  if average_color < 90:
      print('picture is dark')
      return True
  else:
      print('picture is light')
      return False

def move_arm(end):
  goal = PoseStamped()
  goal.header.frame_id = "base"

  #x, y, and z position
  goal.pose.position.x = end[0]
  goal.pose.position.y = end[1]
  goal.pose.position.z = end[2]
    
  #Orientation as a quaternion
  goal.pose.orientation.x = end[3]
  goal.pose.orientation.y = end[4]
  goal.pose.orientation.z = end[5]
  goal.pose.orientation.w = end[6]



  #Set the goal state to the pose you just defined
  left_arm.set_pose_target(goal)

  #Set the start state for the left arm
  left_arm.set_start_state_to_current_state()


  #Plan a path
  left_plan = left_arm.plan()

  #Execute the plan
  left_arm.execute(left_plan)

  rospy.sleep(1.0)

if __name__ == '__main__':
    #Initialize moveit_commander
    moveit_commander.roscpp_initialize(sys.argv)

    #Start a node
    rospy.init_node('moveit_node')

    # Initialize both arms
    robot = moveit_commander.RobotCommander()
    scene = moveit_commander.PlanningSceneInterface()
    left_arm = moveit_commander.MoveGroupCommander('left_arm')
    right_arm = moveit_commander.MoveGroupCommander('right_arm')
    left_arm.set_planner_id('RRTConnectkConfigDefault')
    left_arm.set_planning_time(10)
    right_arm.set_planner_id('RRTConnectkConfigDefault')
    right_arm.set_planning_time(10)

    
    # rospy.init_node('gripper_test')

    #Set up the left gripper
    left_gripper = baxter_gripper.Gripper('left')

    #Calibrate the gripper (other commands won't work unless you do this first)
    left_gripper.calibrate()
    rospy.sleep(2.0)

    # Waits for the image service to become available
    rospy.wait_for_service("last_image")
    print "Service available"
    # Initializes the image processing node
    #rospy.init_node('image_processing_node')
  
    # Creates a function used to call the 
    # image capture service: ImageSrv is the service type
  
    last_image_service = rospy.ServiceProxy('last_image', ImageSrv)



while not rospy.is_shutdown():

  listener = tf.TransformListener()
  trans = rot = None

  move_arm(basket1[0:7])
  start_time = time.time()

  while (time.time() < start_time + 2):
  	#ar_marker_0 for light basket
    try:
  	  (trans,rot) = listener.lookupTransform('/base', 'ar_marker_0',rospy.Time(0))
    except:
      break
  
  #if ar_marker_0 is detected, set as light position
  if (trans!= None or rot!= None):
  	lightBasket = basket1
  	darkBasket = basket2
  else:
  	lightBasket = basket2
  	darkBasket = basket1

  for i in range(3):
    if i ==0:
      move_arm(clothes1top[0:7])
      move_arm(clothes1bot[0:7])
      dark = capture_image()
      left_gripper.close(block=True)
      rospy.sleep(0.5)
      move_arm(clothes1top[0:7])
    if i ==1:
      move_arm(clothes2top[0:7])
      move_arm(clothes2bot[0:7])
      dark = capture_image()
      left_gripper.close(block=True)
      rospy.sleep(0.5)
      move_arm(clothes2top[0:7])

    if i ==2:
      move_arm(clothes3top[0:7])
      move_arm(clothes3bot[0:7])
      dark = capture_image()
      left_gripper.close(block=True)
      rospy.sleep(0.5)
      move_arm(clothes3top[0:7])


    #dark = capture_image()
    #left_gripper.close(block=True)
    #rospy.sleep(1.0)

    if dark == True:
      move_arm(darkBasket[0:7])
    else:
      move_arm(lightBasket[0:7])

    left_gripper.open(block=True)
    rospy.sleep(1.0)

  
  while True:
    if rospy.is_shutdown():
      raise KeyboardInterrupt
    cv2.waitKey(10)

