import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class DistanceSubscriber(Node):
    def __init__(self):
        super().__init__('distance_subscriber')

        self.subscription = self.create_subscription(
            Float32,
            'distance',
            self.callback,
            10
        )

    def callback(self, msg):
        distance = msg.data
        print("Received Distance:", distance)

        if distance < 20:
            print("🛑 STOP - Object very close")
        elif distance < 50:
            print("⚠️ object detected")
        else:
            print("✅ chala pudhe")

def main(args=None):
    rclpy.init(args=args)
    node = DistanceSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
