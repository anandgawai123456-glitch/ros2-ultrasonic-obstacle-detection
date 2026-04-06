import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import serial

class UltrasonicPublisher(Node):
    def __init__(self):
        super().__init__('ultrasonic_node')

        print("✅ Node started")

        # Publisher
        self.publisher_ = self.create_publisher(Float32, 'distance', 10)

        # Serial connection
        try:
            self.ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
            print("✅ Serial connected")
        except Exception as e:
            print("❌ Serial error:", e)

        # Timer (runs every 0.5 sec)
        self.timer = self.create_timer(0.5, self.read_sensor)

    def read_sensor(self):
        print("⏱ Timer running")

        try:
            if self.ser.in_waiting > 0:
                data = self.ser.readline().decode().strip()
                print("RAW:", data)

                if data:
                    distance = float(data)

                    print("Distance value:", distance)

                    # Publish to ROS2 topic
                    msg = Float32()
                    msg.data = distance
                    self.publisher_.publish(msg)

                    # 🧠 Decision Logic
                    if distance < 20:
                        print("⚠️ VERY CLOSE OBJECT, khup javal ahe")
                    elif distance < 50:
                        print("Object nearby", "jawal pas ahe")
                    else:
                        print("Clear path", "pudhe kahich nai ahe")

        except Exception as e:
            print("Error:", e)


def main(args=None):
    rclpy.init(args=args)
    node = UltrasonicPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

