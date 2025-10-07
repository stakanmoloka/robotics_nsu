import sys
import rclpy
import math 
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

def normalize_angle(angle):
    while angle > math.pi:
        angle -= 2 * math.pi
    while angle < -math.pi:
        angle += 2 * math.pi
    return angle


class MoveToGoal(Node):
    def __init__(self):
        super().__init__('move_to_goal')
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)


    def move(self, x, y, theta):
        pose = self.get_current_pose()
        print(f"Turtle position: x={pose.x}, y={pose.y}, theta={pose.theta}")
        x_cur = pose.x
        y_cur = pose.y
        angle_to_goal = math.atan2(y - y_cur, x - x_cur)
        distance = math.sqrt((x - x_cur)**2 + (y - y_cur)**2)

        while True:
            pose = self.get_current_pose()
            angle_to_goal = math.atan2(y - pose.y, x - pose.x)
            angle_diff = normalize_angle(angle_to_goal - pose.theta)
            distance = math.sqrt((x - pose.x)**2 + (y - pose.y)**2)

            print(f"angle_to_goal={angle_to_goal:.2f}, theta={pose.theta:.2f}, distance={distance:.2f}")

            twist_msg = Twist()

            if abs(angle_diff) > 0.1:
                twist_msg.angular.z = 0.5 if angle_diff > 0 else -0.5
                twist_msg.linear.x = 0.0
            elif distance > 0.1:
                twist_msg.angular.z = 0.0
                twist_msg.linear.x = 0.5
            else:
                twist_msg.angular.z = theta
                twist_msg.linear.x = 0.0
                self.publisher.publish(twist_msg)
                break

            self.publisher.publish(twist_msg)

    def get_current_pose(self):
        self.future = rclpy.task.Future()
        sub = self.create_subscription(Pose, 'turtle1/pose',
                                       lambda msg: self.future.set_result(msg), 1)
        rclpy.spin_until_future_complete(self, self.future)
        self.destroy_subscription(sub)

        return self.future.result()
        

def main():
    rclpy.init()

    moving_node = MoveToGoal()
    moving_node.move(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]))
    moving_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()