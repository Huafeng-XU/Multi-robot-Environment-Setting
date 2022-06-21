## in pi
# start the bringup.sh 
./bringup.sh

# start the low-level control
srobot...

### in remote pc
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



# for pipe robot
## check the linux environment for runing
conda env list
## activate the pipe-ins
conda activate pipe-ins
## start recieved
python3 app2.py

## in pi
python3 push
