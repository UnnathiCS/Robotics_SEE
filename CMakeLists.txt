cmake_minimum_required(VERSION 3.5)
project(my_robot_description)  # Ensure this matches your package name

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(xacro REQUIRED)  # Needed for Xacro processing

# Install launch files
install(DIRECTORY launch
  DESTINATION share/my_robot_description
)

# Install URDF/Xacro files
install(DIRECTORY urdf
  DESTINATION share/my_robot_description
)

# Enable testing
if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  set(ament_cmake_copyright_FOUND TRUE)
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()  # This ensures proper nesting

ament_package()
