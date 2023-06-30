from geometry_msgs.msg import Twist, Point
from math import atan2
def calculate_goal(node):
    goal = Point()
    goal.x = node.point_list[node.current_point][0]
    goal.y = node.point_list[node.current_point][1]
    return goal

def calculate_angle_to_goal(node, goal):
    inc_x = goal.x - node.x
    inc_y = goal.y - node.y
    angle_to_goal = atan2(inc_y, inc_x)
    return angle_to_goal

def check_lidar_margin(node):
    return node.lidar_.check_safety_margin()

def check_reached_point( inc_x, inc_y,MAX_DIFF):
    return abs(inc_x) < MAX_DIFF and abs(inc_y) < MAX_DIFF

def adjust_speed(node, angle_to_goal,MAX_DIFF):
    speed = Twist()
    if not node.stop:
        if abs(angle_to_goal - node.theta) > MAX_DIFF:
            speed.linear.x = 0.0
            speed.angular.z = 0.3 if (angle_to_goal - node.theta) > 0.0 else -0.3
        else:
            speed.linear.x = 0.1
            speed.angular.z  =0.0
    else:
        speed.linear.x = 0.0
        speed.angular.z = 0.0
        node.current_point = 0
        node.running = False
        node.stop = False
    return speed
