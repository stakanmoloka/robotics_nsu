from service_full_name_interfaces.srv import FullNameSumService

import rclpy
from rclpy.node import Node


class service_name(Node):

    def __init__(self):
        super().__init__('minimal_service')
        self.srv = self.create_service(FullNameSumService, 'SummFullName', self.callback)

    def callback(self, request, response):
        response.full_name = request.last_name + ' ' + request.name + ' ' + request.first_name
        self.get_logger().info(f'Incoming request\nlast_name: {request.last_name} name: {request.name} first name: {request.first_name}')

        return response


def main():
    rclpy.init()

    minimal_service = service_name()

    rclpy.spin(minimal_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()