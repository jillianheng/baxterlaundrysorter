# baxterlaundrysorter

Main code can be found in >src>cam_test>image_process.py
Launch file in >launch>run_cam.launch

Packages used: ar_track_alvar, moveIt, OpenCV

How to run our code on Baxter:
> source devel/setup.bash
> ./baxter.sh
> rosrun baxter_tools enable_robot.py -e
> rosrun baxter_interface joint_trajectory_action_server.py

New Terminal
> source devel/setup.bash
> ./baxter.sh
> roslaunch baxter_moveit_config move_group.launch

New Terminal
> source devel/setup.bash
> ./baxter.sh
> roslaunch cam_test run_cam.launch
