#!/usr/bin/python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

# Topic name = /turtle1/cmd_vel
# Topic's msg type = geometry_msgs/msg/Twist

class DriveCirclesNode(Node):
    def __init__(self):
        super().__init__('drive_circles_node')
        self.get_logger().info("Node has started successfully")
        self.pt_cmd_vel_pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.time_to_publish = self.create_timer(1.0, self.cmd_vel_publish)
    def cmd_vel_publish(self):
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 2.0

        self.pt_cmd_vel_pub.publish(msg)


def main(args=None):
    rclpy.init()
    node  = DriveCirclesNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=='__main__':
    main()