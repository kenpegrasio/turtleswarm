# This python code is intended to be run on the RPi
import rclpy
import sys
from rclpy.node import Node
from rclpy.time import Time
from geometry_msgs.msg import TwistStamped

class TwistListener(Node):
    def __init__(self, namespace):
        super().__init__('twist_listener')
        self.namespace = namespace

        # Create the Twist listener to listen for the published update
        self.twist_listener = self.create_subscription(
            TwistStamped, 
            f'{namespace}/cmd_vel',
            self.twist_callback,
            10
        )
    
    def twist_callback(self, msg: TwistStamped):
        receive_time = self.get_clock().now()
        sent_time = Time.from_msg(msg.header.stamp)
        latency_ms = (receive_time - sent_time).nanoseconds / 1e6
        
        with open("output.txt", "a") as f:
            f.write(f"{latency_ms}\n")
        
        self.get_logger().info(f'Receive time: {receive_time}, sent time: {sent_time}, latency: {latency_ms}')


def main(args=None):
    rclpy.init(args=None)
    if args is None:
        args = sys.argv[1:]
    node = TwistListener('' if len(args) == 0 else args[0])
    with open("output.txt", "a") as f:
        f.write(f"\n")
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()