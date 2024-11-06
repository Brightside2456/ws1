#!/usr/bin/python3

import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose

# Topic name = /turtle1/pose
# Message type = turtlesim/msg/Pose
# Pose.x
#Pose.y
#Pose.theta
#Pose.linear_velocity
#Pose.angular_velocity

class PoseSubscriberNode(Node):
    def __init__(self):
        super().__init__('pose_subscriber')
        self.st_pose_sub = self.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10)

    def pose_callback(self, mssg: Pose):
        self.get_logger().info(f"X-Coordinates = {mssg.x}\nY-Coordinates = {mssg.x}\nLinear_Velocity = {mssg.linear_velocity} \n Angular_Velocity: {mssg.angular_velocity}")
    



def main(args=None):
    rclpy.init()
    node = PoseSubscriberNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__=='__main__':
    main()
