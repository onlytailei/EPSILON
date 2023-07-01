docker: melodic 18.04
host: 22.04

# start docker container
docker run -v /home/tai/Projects/EPSILON:/root/catkin_ws/src/EPSILON -i -d epsilon:latest bash


# in docker container
source /opt/ros/melodic/setup.bash
source ~/catkin_ws/devel/setup.bash

export ROS_MASTER_URI=http://172.17.0.2:11311
export ROS_IP=172.17.0.2

roslaunch ~/catkin_ws/src/EPSILON/launch/eudm_ros.launch

# host
export ROS_MASTER_URI=http://172.17.0.1:11311
export ROS_IP=172.17.0.1

rviz -d phy_simulator_planning.rviz

cd Projects/EPSILOM/aux_tools/src
python terminal_server.py