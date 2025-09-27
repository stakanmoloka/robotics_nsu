import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist

class TextToCmdVel(Node):

    def __init__(self):
        super().__init__('text_to_cmd_vel')
        self.subscription = self.create_subscription(
            String,
            'cmd_text',
            self.listener_callback,
            10)
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.subscription 

    def listener_callback(self, msg_text):
        twist_msg = Twist()
        command = msg_text.data.lower()
        if command == "move_forward":
            twist_msg.linear.x = 1.0
            twist_msg.angular.z = 0.0
            self.publisher_.publish(twist_msg)
            self.get_logger().info('Received text: "%s", moving turtle' % msg_text.data)
        elif command == "move_backward":
            twist_msg.linear.x = -1.0
            twist_msg.angular.z = 0.0
            self.publisher_.publish(twist_msg)
            self.get_logger().info('Received text: "%s", moving turtle' % msg_text.data)
        elif command == "turn_right":
            twist_msg.linear.x = 0.0
            twist_msg.angular.z = -1.0
            self.publisher_.publish(twist_msg)
            self.get_logger().info('Received text: "%s", turning turtle' % msg_text.data)
        elif command == "turn_left":
            twist_msg.linear.x = 0.0
            twist_msg.angular.z = 1.0
            self.publisher_.publish(twist_msg)
            self.get_logger().info('Received text: "%s", turning turtle' % msg_text.data)
        else:
            self.get_logger().info("Unknown command: '%s'" % command)

def main(args=None):
    rclpy.init(args=args)
    node = TextToCmdVel()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
