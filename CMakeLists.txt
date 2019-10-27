cmake_minimum_required(VERSION 2.8.3)
project(performance_test)

## Compile as C++11, supported in ROS Kinetic and newer
add_compile_options(-std=c++11)

# Catkin dependencies
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation
)

## Generate messages in the 'msg' folder
add_message_files(
  FILES
  SuperAwesome.msg
)

## Generate added messages and services with any dependencies listed here
generate_messages(
  DEPENDENCIES
  std_msgs
)

## The catkin_package macro generates cmake config files for your package
catkin_package(
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

add_executable(
  cpp_publisher
  src/publisher.cpp
)

add_executable(
  cpp_subscriber
  src/subscriber.cpp
)

## Specify libraries to link a library or executable target against
target_link_libraries(cpp_publisher
  ${catkin_LIBRARIES}
)

target_link_libraries(cpp_subscriber
  ${catkin_LIBRARIES}
)
