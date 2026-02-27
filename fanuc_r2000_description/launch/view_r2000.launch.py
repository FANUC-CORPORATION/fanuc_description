# SPDX-FileCopyrightText: 2025-2026, FANUC America Corporation
# SPDX-FileCopyrightText: 2025-2026, FANUC CORPORATION
#
# SPDX-License-Identifier: Apache-2.0

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import (
    Command,
    FindExecutable,
    LaunchConfiguration,
    PathJoinSubstitution,
    PythonExpression,
)
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    declared_arguments = [
        DeclareLaunchArgument(
            "robot_model",
            description="The robot model to visualize (required)",
            choices=["r2000ic_100p", "r2000ic_100ph", "r2000ic_125l", "r2000ic_165f", "r2000ic_165r", "r2000ic_190s", "r2000ic_190u", "r2000ic_210f", "r2000ic_210l", "r2000ic_210r", "r2000ic_210we", "r2000ic_220u", "r2000ic_240f", "r2000ic_270f", "r2000ic_270r", "r2000id_100fh", "r2000id_165fh", "r2000id_210fh"],
        )
    ]
    robot_model = LaunchConfiguration("robot_model")

    description_file = PathJoinSubstitution(
        [
            FindPackageShare("fanuc_r2000_description"),
            "robot",
            PythonExpression(["'", robot_model, ".urdf.xacro'"]),
        ]
    )

    robot_description_content = Command(
        [
            PathJoinSubstitution([FindExecutable(name="xacro")]),
            " ",
            description_file,
        ]
    )

    rviz_file = os.path.join(
        get_package_share_directory("fanuc_r2000_description"),
        "rviz",
        "view_r2000.rviz",
    )

    joint_state_publisher_node = Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui",
    )
    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="both",
        parameters=[{"robot_description": robot_description_content}],
    )
    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        output="both",
        arguments=["--display-config", rviz_file],
    )

    nodes_to_start = [
        joint_state_publisher_node,
        robot_state_publisher_node,
        rviz_node,
    ]

    return LaunchDescription(declared_arguments + nodes_to_start)
