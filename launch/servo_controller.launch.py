from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='servo_control',
            executable='servo_controller',
            name='servo_controller',
            output='screen',
        ),
    ])
