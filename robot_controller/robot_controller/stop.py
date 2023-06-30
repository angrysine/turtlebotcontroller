from geometry_msgs.msg import Twist
import rclpy
from rclpy.node import Node

def publisher_callback(node):
    speed = Twist()

                
    speed.linear.x = 0.0
    speed.angular.z = 0.0
    node.publisher.publish(speed)

class TurtleController(Node):
    def __init__(self):
        super().__init__('controller')
        
        
        self.vel_msg = Twist()



        self.publisher = self.create_publisher(
            msg_type=Twist,
            topic='/cmd_vel',
            qos_profile=10)
    

        publisher_lambda =  lambda : publisher_callback(self)
        self.timer = self.create_timer(
            timer_period_sec=0.02,
            callback=publisher_lambda)
    



def main(args=None):
    rclpy.init(args=args)
    controller = TurtleController()
    # print(controller.current_point)
    # changeCurrentPoint(controller)
    # print(controller.current_point)

    rclpy.spin(controller)
    controller.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()