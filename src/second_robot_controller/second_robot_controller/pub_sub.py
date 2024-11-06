import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class PubSubNode(Node):
    def __init__(self):
        super().__init__('publisher_subscriber')
        self.st_pose_sub = self.create_subscription(Pose, '/turtle1/pose', self.get_vals, 10)
        self.pt_cmd_vel_pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

    # def send_vals(self):

    def get_vals(self, pos: Pose):
        commands = Twist()

        if pos.x > 9.0:
            commands.linear.x = 1.0
            commands.angular.z = 0.9
        elif pos.x < 2.0:
            commands.linear.x = 1.0
            commands.angular.z = 0.9
        elif pos.y > 9.0:
            commands.linear.x = 1.0
            commands.angular.z = 0.9
        elif pos.y < 2.0:
            commands.linear.x = 1.0
            commands.angular.z = 0.9
        else:
            commands.linear.x = 2.0
            commands.angular.z = 0.0

        self.pt_cmd_vel_pub.publish(commands)
        
        
        
        



def main(args=None):
    rclpy.init()
    node = PubSubNode()
    rclpy.spin(node=node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()