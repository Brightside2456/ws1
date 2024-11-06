#!/usr/bin/python3
import rclpy
from rclpy.node import Node


class LoggerNode(Node):
    def __init__(self):
        super().__init__('logger_node')
        self.counter = 0
        self.timer_cb = self.create_timer(1.0, self.logg)

    def logg(self):
        self.get_logger().info(f"Count is : {self.counter}")
        self.counter += 1




def main(args=None):
    rclpy.init(args=args)
    node = LoggerNode()
    rclpy.spin(node=node)
    rclpy.shutdown()
    pass



if __name__=='__main__':
    main()