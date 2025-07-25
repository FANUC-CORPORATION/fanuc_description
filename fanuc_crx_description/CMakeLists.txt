# SPDX-FileCopyrightText: 2025, FANUC America Corporation
# SPDX-FileCopyrightText: 2025, FANUC CORPORATION
#
# SPDX-License-Identifier: Apache-2.0

cmake_minimum_required(VERSION 3.8)
project(fanuc_crx_description)

find_package(ament_cmake REQUIRED)

install(
  DIRECTORY launch meshes urdf robot rviz
  DESTINATION share/${PROJECT_NAME}/
)

ament_package()
