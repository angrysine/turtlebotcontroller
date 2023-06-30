from .auxiliar import calculate_angle_to_goal, calculate_goal, check_lidar_margin, check_reached_point, adjust_speed
import rclpy
from geometry_msgs.msg import Twist
from std_msgs.msg import String  # Standard ROS 2 String message


MAX_DIFF = 0.1


def publisher_callback(node):
    
    if node.running:

      
        try:
            goal = calculate_goal(node)
            angle_to_goal = calculate_angle_to_goal(node, goal)

            #if not check_lidar_margin(node) and not node.returning:
                #node.logger(f"lidar{node.i}")
                #node.i += 1

               # node.returning = True
               # node.point_list = [
                 #   (0.0, 0.0), *node.point_list[0:node.current_point]]
                #node.point_list.reverse()

               # node.current_point = 0

            if check_reached_point(goal.x - node.x, goal.y - node.y, MAX_DIFF):
                node.logger(str(node.point_list))
                node.logger(str(node.current_point))
                if len(node.point_list)-1 > node.current_point:
                    node.current_point += 1

                else:

                    speed = Twist()

                    speed.linear.x = 0.0
                    speed.angular.z = 0.0
                    node.publisher.publish(speed)
                    node.stop = True
                    
            speed = adjust_speed(node, angle_to_goal, MAX_DIFF)
            node.publisher.publish(speed)

        except Exception as error:

            node.logger(str(error))


