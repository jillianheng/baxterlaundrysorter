#!/usr/bin/env python

import roslib
import rospy
import baxter_interface
from sensor_msgs.msg import Image
from cam_test.srv import ImageSrv, ImageSrvResponse

from baxter_interface.camera import CameraController

class ImgService:
  #Callback for when an image is received
  def imgReceived(self, message):
    #Save the image in the instance variable
    self.lastImage = message
    
    #Print an alert to the console
    #print(rospy.get_name() + ":Image received!")

  #When another node calls the service, return the last image
  def getLastImage(self, request):
    #Print an alert to the console
    #print("Image requested!")

    #Return the last image
    return ImageSrvResponse(self.lastImage)

  def __init__(self):
    #Create an instance variable to store the last image received
    self.lastImage = None;

    #Initialize the node
    rospy.init_node('left_hand_camera_srv')
    # rospy.init_node('right_hand_camera_srv')

    # right_cam = CameraController("right_hand_camera")
    # right_cam.close()

    left_cam = CameraController("left_hand_camera")
    left_cam.resolution = (1280,800)
    left_cam.open()

    # cameraController = baxter_interface.CameraController("left_hand_camera")
    # # cameraController.close()
    # cameraController.resolution= (1280,800)
    # cameraController.open()

    #Subscribe to the image topic
    rospy.Subscriber("/cameras/left_hand_camera/image", Image, self.imgReceived)

    #Create the service
    rospy.Service('last_image', ImageSrv, self.getLastImage)
    print "Service last_image created"

  def run(self):
    rospy.spin()


#Python's syntax for a main() method
if __name__ == '__main__':
  node = ImgService()
  node.run()