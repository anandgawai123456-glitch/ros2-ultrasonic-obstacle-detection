
# **ROS2 Learning Journey - Anand Gawai**

This repository contains my **ROS2 Humble simulation and beginner robotics projects**, including publisher and subscriber nodes, and experiments with Python nodes.

---

## **📌 Project Overview**

* Built ROS2 **Publisher and Subscriber nodes** in Python
* Learned to debug **Python errors** inside ROS2 packages
* Explored ROS2 concepts:

  * Nodes
  * Topics
  * Parameters
  * Callbacks
* Set up GitHub version control to **track and share progress**

---

## **📂 Project Structure**

```text
ros2_ws/
├── src/
│   └── my_robot_pkg/
│       ├── my_robot_pkg/
│       │   ├── temprature_publisher.py
│       │   ├── temprature_subscriber.py
│       │   └── other sample nodes...
│       └── setup.py
├── install/
├── build/
└── log/
```

* `temprature_publisher.py` → Publishes simulated temperature values
* `temprature_subscriber.py` → Subscribes to the temperature topic and prints values
* Other files are experimental ROS2 nodes (turtle controller, subscriber/publisher templates)

---

## **🚀 How to Run**

1. Source your ROS2 workspace:

```bash
source ~/ros2_ws/install/setup.bash
```

2. Run the Publisher node:

```bash
ros2 run my_robot_pkg temprature_publisher
```

3. Run the Subscriber node (in a new terminal):

```bash
ros2 run my_robot_pkg temprature_subscriber
```

4. Check topics and nodes:

```bash
ros2 node list
ros2 topic list
ros2 topic echo /temperature
```

---

## **🛠 Skills Learned**

* ROS2 Humble environment setup
* Python scripting for ROS2 nodes
* Publisher-Subscriber communication
* Git & GitHub version control
* Debugging Python and ROS2 errors

---

## **💻 Author**

**Anand Gawai**

* Electrical Engineer | Robotics Enthusiast
* GitHub: [anandgawai123456-glitch](https://github.com/anandgawai123456-glitch)


