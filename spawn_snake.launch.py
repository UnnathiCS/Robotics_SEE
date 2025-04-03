import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from launch.actions import ExecuteProcess

def generate_launch_description():
    urdf_file = os.path.join(get_package_share_directory('my_robot_description'), 'urdf', 'snake_bot.urdf')

    return LaunchDescription([
        ExecuteProcess(
            cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_factory.so'],
            output='screen'),

        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=['-entity', 'snake_bot', '-file', urdf_file, '-x', '0', '-y', '0', '-z', '1'],
            output='screen'),
    ])
