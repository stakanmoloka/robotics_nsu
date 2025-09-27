from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='sim1',
            namespace='turtlesim1'
        ),
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='sim2',
            namespace='turtlesim2'
        ),
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='sim3',
            namespace='turtlesim3'
        ),
        Node(
            package='turtlesim',
            executable='mimic',
            name='mimic1',
            remappings=[
                ('/input/pose', '/turtlesim1/turtle1/pose'),
                ('/output/cmd_vel', '/turtlesim2/turtle1/cmd_vel')
            ]
        ),
        Node(
            package='turtlesim',
            executable='mimic',
            name='mimic2',
            remappings=[
                ('/input/pose', '/turtlesim2/turtle1/pose'),
                ('/output/cmd_vel', '/turtlesim3/turtle1/cmd_vel')
            ]
        ),
    ])
