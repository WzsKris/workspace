#include "ros/ros.h"
#include "fullurdf2/SetDamping.h"
#include <iostream>

int main(int argc, char **argv)
{
  ros::init(argc, argv, "damping_client");

  if (argc != 3)
  {
    ROS_INFO("Usage: damping_client <joint_name> <damping>");
    return 1;
  }

  ros::NodeHandle nh;
  ros::ServiceClient client = nh.serviceClient<fullurdf2::SetDamping>("/gazebo/set_joint_damping_fullurdf2");

  fullurdf2::SetDamping srv;
  srv.request.joint_name = argv[1];
  srv.request.damping = std::stod(argv[2]);

  if (client.call(srv))
  {
    if (srv.response.success)
    {
      ROS_INFO("Successfully set damping: %s", srv.response.message.c_str());
    }
    else
    {
      ROS_ERROR("Failed to set damping: %s", srv.response.message.c_str());
    }
  }
  else
  {
    ROS_ERROR("Failed to call service set_joint_damping_fullurdf2");
  }

  return 0;
}
