<!-- SPDX-FileCopyrightText: 2025 FANUC America Corp.
     SPDX-FileCopyrightText: 2025 FANUC CORPORATION

     SPDX-License-Identifier: Apache-2.0
-->
<!-- markdownlint-disable MD013 -->
# fanuc_description

This repository contains description files and meshes for FANUC robot arms.

## Installation

See the [fanuc_driver README](https://github.com/FANUC-CORPORATION/fanuc_driver) for instructions.

## Repository structure

```text
├── fanuc_crx_description
│   ├── launch
│   │   └── view_crx.launch.py
│   ├── meshes
│   │   ├── crx10ia
│   │   │   ├── collision
│   │   │   │   └── ...
│   │   │   └── visual
│   │   │       └── ...
│   │   └── ... other models
│   ├── robot
│   │   ├── crx10ia.urdf.xacro
│   │   └── ... other example top-level xacro files
│   ├── rviz
│   │   └── view_crx.rviz
│   ├── urdf
│   │   ├── crx10ia_urdf_macro.xacro
│   │   └── ... other models
│   ├── CMakeLists.txt
│   └── package.xml
├── ... other model families
└── README.md
```

Description files are organized by FANUC robot arm model family.

### Package Structure

Packages have the following subdirectories:

- `meshes/`: Visual and collision meshes for each robot.
- `urdf/`: Base xacro macro files for generating a robot description (as a URDF)
for a specific robot model.
- `robot/`: Example top-level xacro files that generate a complete URDF
containing a robot model.
- `launch/` and `rviz/`: Launch files and configuration for visualizing robots
in `robot/`.

## Licensing

The original FANUC ROS 2 Driver source code and associated documentation
including these web pages are Copyright (C) 2025 FANUC America Corporation
and FANUC CORPORATION.

Any modifications or additions to source code or documentation
contributed to this project are Copyright (C) the contributor,
and should be noted as such in the comments section of the modified file(s).

FANUC ROS 2 Driver is licensed under
     [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0)

Please see the LICENSE folder in the root directory for the full texts of these licenses.
