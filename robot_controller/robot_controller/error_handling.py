from geometry_msgs.msg import Twist

def handle_index_error(node, err):
    node.point_list = node.point_list[0:node.current_point-1]
    node.point_list.reverse()
   
    node.current_point =0

    speed = Twist()
    speed.linear.x = 0.0
    speed.angular.z = 0.3
    node.publisher.publish(speed)
    print(err)

def handle_exception(node, error):
    node.point_list = node.point_list[0:node.current_point]
    node.point_list.reverse()
   
    node.current_point =0

    speed = Twist()
    speed.linear.x = 0.0
    speed.angular.z = 0.3
    node.publisher.publish(speed)
    print(error)