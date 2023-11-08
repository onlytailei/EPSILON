docker: melodic 18.04
host: 22.04

# start docker container
docker run -v /home/tai/Projects/EPSILON:/root/catkin_ws/src/EPSILON  -v /home/tai/Projects/EPSILON/.vscode/.vscode-server:/root/.vscode-server -v /home/tai/Projects/EPSILON/.vscode:/root/catkin_ws/.vscode -i -d epsilon:latest bash

**notice the ros master uri must be ended with a '/'**

docker run -v /home/tai/Projects/EPSILON:/root/catkin_ws/src/EPSILON  -v /home/tai/Projects/EPSILON/.vscode/.vscode-server:/root/.vscode-server -v /home/tai/Projects/EPSILON/.vscode:/root/catkin_ws/.vscode -v /home/tai/Projects/EPSILON/.vscode/.bashrc:/root/.bashrc -e ROS_IP=172.17.0.2 -i -d epsilon:latest bash

# in docker container
cd ~/catkin_ws
catkin_make
catkin_make -DCMAKE_BUILD_TYPE=Debug
catkin_make -DCMAKE_EXPORT_COMPILE_COMMANDS=1

# start a terminal
roscore

# run debug through vscode container
ROS: Launch separate


# without vscdoe container
roslaunch ~/catkin_ws/src/EPSILON/launch/eudm_ros.launch

# host
export ROS_MASTER_URI=http://172.17.0.2:11311
export ROS_IP=172.17.0.1

rviz -d phy_simulator_planning.rviz

cd Projects/EPSILOM/aux_tools/src
python terminal_server.py
