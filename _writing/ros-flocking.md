---
layout: article
title: 'Drone Swarm Simulation'
description: 'Simulation of collaborative drone flights with ROS and Gazebo.'
github_repo: 'matejkajinic/ros-flocking'
github_url: 'https://github.com/matejkajinic/ros-flocking'
source_path: 'README.md'
last_commit_sha: 'bccf5dd01a4a5ba8df60f843128a6e92a3e75357'
last_commit_date: '2020-02-16T17:22:58Z'
---

<!-- Generated at 2026-03-20T21:59:12Z by scripts/sync_writing.py -->

# Birds (boid) simulation

Boid flocking simulation using Gazebo simulator and ROS.

![image1](images/flocking.jpg)

Installation Instructions
-------------------------
1. Install Ubuntu 16.04, [ROS Kinetic](https://wiki.ros.org/kinetic/Installation/Ubuntu) and Gazebo
2. Setup ROS workspace
```
$ mkdir -p ~/catkin_ws/src
$ cd ~/catkin_ws/src
$ catkin_init_workspace                     # initialize your catkin workspace
```
3. Compile the workspace of boid package
```
$ cd ~/catkin_ws/src

*Extract the file here*

$ cd ~/catkin_ws/
$ catkin_make
```

4. Source `setup.bash` file

```
$ source devel/setup.bash
```

To run the simulation
-----------

Launch the gazebo simulator with boid models

```
$ roslaunch boid_gazebo swarm_in_gazebo.launch
```

Launch boid controller node (open new terminal)

```
$ roslaunch boid_gazebo flocking.launch
```

To set another goal
-----------

Goal 1
(open new terminal)

```
rostopic pub /boid/set_goal geometry_msgs/Point "x: 12.0
y: 8.0
z: 9.0" 
```

Goal 2
(open new terminal)

```
rostopic pub /boid/set_goal geometry_msgs/Point "x: 5.0
y: -5.0
z: 10.0" 
```

## References
[1] http://www.cs.toronto.edu/~dt/siggraph97-course/cwr87/

