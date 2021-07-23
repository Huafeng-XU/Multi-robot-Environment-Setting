# start extrinsinc camera
export AUTO_EX_CALIB=calibration
roslaunch turtlebot3_autorace_camera turtlebot3_autorace_extrinsic_camera_calibration.launch
# start detect lane
export AUTO_DT_CALIB=calibration
roslaunch turtlebot3_autorace_detect turtlebot3_autorace_detect_lane.launch
# start rqt
rqt
# start configuration
rosrun rqt_reconfigure rqt_reconfigure
