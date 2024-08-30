#include "ros/ros.h"
#include "softactuator/SetFriction.h"
#include <iostream>

int main(int argc, char **argv)
{
  ros::init(argc, argv, "friction_client");

  if (argc != 3)
  {
    ROS_INFO("Usage: friction_client <joint_name> <friction>");
    return 1;
  }

  ros::NodeHandle nh;
  ros::ServiceClient client = nh.serviceClient<softactuator::SetFriction>("/gazebo/set_joint_friction_softactuator");

  softactuator::SetFriction srv;
  srv.request.joint_name = argv[1];
  srv.request.friction = std::stod(argv[2]);

  if (client.call(srv))
  {
    if (srv.response.success)
    {
      ROS_INFO("Successfully set friction: %s", srv.response.message.c_str());
    }
    else
    {
      ROS_ERROR("Failed to set friction: %s", srv.response.message.c_str());
    }
  }
  else
  {
    ROS_ERROR("Failed to call service set_joint_friction_softactuator");
  }

  return 0;
}
