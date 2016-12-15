# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "cam_test: 0 messages, 1 services")

set(MSG_I_FLAGS "-Isensor_msgs:/opt/ros/indigo/share/sensor_msgs/cmake/../msg;-Igeometry_msgs:/opt/ros/indigo/share/geometry_msgs/cmake/../msg;-Istd_msgs:/opt/ros/indigo/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(genlisp REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(cam_test_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/cc/ee106a/fa16/class/ee106a-ade/ros-workspaces/final_proj/src/cam_test/srv/ImageSrv.srv" NAME_WE)
add_custom_target(_cam_test_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "cam_test" "/home/cc/ee106a/fa16/class/ee106a-ade/ros-workspaces/final_proj/src/cam_test/srv/ImageSrv.srv" "std_msgs/Header:sensor_msgs/Image"
)

#
#  langs = gencpp;genlisp;genpy
#

### Section generating for lang: gencpp
### Generating Messages

### Generating Services
_generate_srv_cpp(cam_test
  "/home/cc/ee106a/fa16/class/ee106a-ade/ros-workspaces/final_proj/src/cam_test/srv/ImageSrv.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/indigo/share/sensor_msgs/cmake/../msg/Image.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/cam_test
)

### Generating Module File
_generate_module_cpp(cam_test
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/cam_test
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(cam_test_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(cam_test_generate_messages cam_test_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/cc/ee106a/fa16/class/ee106a-ade/ros-workspaces/final_proj/src/cam_test/srv/ImageSrv.srv" NAME_WE)
add_dependencies(cam_test_generate_messages_cpp _cam_test_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(cam_test_gencpp)
add_dependencies(cam_test_gencpp cam_test_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS cam_test_generate_messages_cpp)

### Section generating for lang: genlisp
### Generating Messages

### Generating Services
_generate_srv_lisp(cam_test
  "/home/cc/ee106a/fa16/class/ee106a-ade/ros-workspaces/final_proj/src/cam_test/srv/ImageSrv.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/indigo/share/sensor_msgs/cmake/../msg/Image.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/cam_test
)

### Generating Module File
_generate_module_lisp(cam_test
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/cam_test
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(cam_test_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(cam_test_generate_messages cam_test_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/cc/ee106a/fa16/class/ee106a-ade/ros-workspaces/final_proj/src/cam_test/srv/ImageSrv.srv" NAME_WE)
add_dependencies(cam_test_generate_messages_lisp _cam_test_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(cam_test_genlisp)
add_dependencies(cam_test_genlisp cam_test_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS cam_test_generate_messages_lisp)

### Section generating for lang: genpy
### Generating Messages

### Generating Services
_generate_srv_py(cam_test
  "/home/cc/ee106a/fa16/class/ee106a-ade/ros-workspaces/final_proj/src/cam_test/srv/ImageSrv.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/indigo/share/sensor_msgs/cmake/../msg/Image.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/cam_test
)

### Generating Module File
_generate_module_py(cam_test
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/cam_test
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(cam_test_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(cam_test_generate_messages cam_test_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/cc/ee106a/fa16/class/ee106a-ade/ros-workspaces/final_proj/src/cam_test/srv/ImageSrv.srv" NAME_WE)
add_dependencies(cam_test_generate_messages_py _cam_test_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(cam_test_genpy)
add_dependencies(cam_test_genpy cam_test_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS cam_test_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/cam_test)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/cam_test
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
add_dependencies(cam_test_generate_messages_cpp sensor_msgs_generate_messages_cpp)

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/cam_test)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/cam_test
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
add_dependencies(cam_test_generate_messages_lisp sensor_msgs_generate_messages_lisp)

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/cam_test)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/cam_test\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/cam_test
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
add_dependencies(cam_test_generate_messages_py sensor_msgs_generate_messages_py)
