#include "ros/ros.h"
#include "fullurdf2/SetStiffness.h"
#include <iostream>

int main(int argc, char **argv)
{
  ros::init(argc, argv, "stiffness_client");

  if (argc != 3)
  {
    ROS_INFO("Usage: stiffness_client <joint_name> <stiffness>");
    return 1;
  }

  ros::NodeHandle nh;
  ros::ServiceClient client = nh.serviceClient<fullurdf2::SetStiffness>("/gazebo/set_joint_stiffness_fullurdf2");

  fullurdf2::SetStiffness srv;
  srv.request.joint_name = argv[1];
  srv.request.stiffness = std::stod(argv[2]);

  if (client.call(srv))
  {
    if (srv.response.success)
    {
      ROS_INFO("Successfully set stiffness: %s", srv.response.message.c_str());
    }
    else
    {
      ROS_ERROR("Failed to set stiffness: %s", srv.response.message.c_str());
    }
  }
  else
  {
    ROS_ERROR("Failed to call service set_joint_stiffness_fullurdf2");
  }

  return 0;
}
