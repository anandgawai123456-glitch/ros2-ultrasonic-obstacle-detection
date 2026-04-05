# ROS2 Ultrasonic Obstacle Detection 🚀

## 📌 Project Overview

This project demonstrates real-time obstacle detection using an ultrasonic sensor (HC-SR04) connected to an ESP32, integrated with ROS2.

The system reads distance data from the sensor and publishes it to a ROS2 topic, where logic is applied to detect nearby obstacles.

---

## ⚙️ Technologies Used

* ROS2 (rclpy)
* ESP32 (Arduino IDE)
* Ultrasonic Sensor (HC-SR04)
* Python (pyserial)

---

## 🔌 Hardware Setup

* ESP32
* HC-SR04 Ultrasonic Sensor
* Voltage Divider (1kΩ + 2kΩ)

### Connections:

* VCC → VIN (5V)
* GND → GND
* TRIG → GPIO 5
* ECHO → Voltage Divider → GPIO 18

---

## 📡 ROS2 Architecture

ESP32 → Serial → ROS2 Node → `/distance` Topic

---

## 🧠 Features

* Real-time distance measurement
* ROS2 publisher node
* Decision logic:

  * < 20 cm → Very Close
  * < 50 cm → Nearby
  * > 50 cm → Clear Path

---

## ▶️ How to Run

```bash
cd ros2_ws
colcon build
source install/setup.bash
ros2 run my_robot_pkg ultrasonic_pub
```

---

## 📊 Example Output

Distance: 15.2
⚠️ VERY CLOSE OBJECT

---

## 🚀 Future Improvements

* Add subscriber node
* Integrate with robot movement (/cmd_vel)
* Visualize in RViz
* Wireless communication (ESP32 WiFi)

---

## 👨‍💻 Author

Anand Pradeep Gawai
