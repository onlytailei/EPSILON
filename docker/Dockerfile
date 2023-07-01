FROM osrf/ros:melodic-desktop-full

ADD sources.list /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y\
    libgoogle-glog-dev libdw-dev libopenblas-dev gfortran \
    python-pip

ADD pip.conf /root/.pip/
ENV PIP_CONFIG_FILE=/root/.pip/pip.conf
RUN pip install empy pygame

RUN mkdir -p /root/catkin_ws/src