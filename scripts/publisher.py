# This python code is intended to be run on your LAPTOP
import rclpy
import sys
from rclpy.node import Node
from geometry_msgs.msg import TwistStamped
import time

class TwistPublisher(Node):
    def __init__(self, namespace):
        super().__init__('twist_publisher')
        self.namespace = namespace

        # Create the Twist publisher to move the robot
        self.get_logger().info("Create publisher to " + f'{namespace}/cmd_vel')
        self.twist_publisher = self.create_publisher(TwistStamped, f'{namespace}/cmd_vel', 10)
    
    def move_forward(self, idx):
        msg = TwistStamped()

        # Include time stamp in the message
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = "twist_stamped"

        # Twist data
        msg.twist.linear.x = 0.01
        msg.twist.angular.z = 0.0
        self.twist_publisher.publish(msg)
        self.get_logger().info(f"{idx}: Publish twist to move forward")
    
    def stop(self):
        msg = TwistStamped()

        # Include time stamp in the message
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = "twist_stamped"

        # Twist data
        msg.twist.linear.x = 0.0
        msg.twist.angular.z = 0.0
        self.twist_publisher.publish(msg)
        self.get_logger().info("Publishing twist to stop")

    def run(self):
        self.get_logger().info("Waiting for subscriber to connect")
        while self.twist_publisher.get_subscription_count() == 0:
            rclpy.spin_once(self, timeout_sec=0.1)
        self.get_logger().info("Subscriber connected, start sending message")
        for idx in range(1, 10):
            self.move_forward(idx)
            rclpy.spin_once(self, timeout_sec=0.01)
            time.sleep(1)
        self.stop()


def main(args=None):
    rclpy.init(args=None)
    if args is None:
        args = sys.argv[1:]
    twist_publisher = TwistPublisher('' if len(args) == 0 else args[0])
    twist_publisher.run()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
