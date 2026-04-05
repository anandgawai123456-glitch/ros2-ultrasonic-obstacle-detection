from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='my_robot_pkg',
            executable='ultrasonic_pub',
            name='ultrasonic_node',
            output='screen'
        ),
        Node(
            package='my_robot_pkg',
            executable='distance_sub',
            name='distance_subscriber',
            output='screen'
        ),
    ])

