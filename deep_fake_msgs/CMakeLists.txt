cmake_minimum_required(VERSION 3.8)
project(deep_fake_msgs)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(action_msgs REQUIRED)
find_package(std_msgs REQUIRED)
find_package(rosidl_default_generators REQUIRED)

set(action_files action/DeepFakeRequest.action)

rosidl_generate_interfaces(deep_fake_msgs
        ${action_files}
        DEPENDENCIES
        action_msgs
        std_msgs
        builtin_interfaces
  )

ament_export_dependencies(rosidl_default_runtime)

ament_package()
