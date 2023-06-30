import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist, Point
from nav_msgs.msg import Odometry
from std_msgs.msg import String  # Standard ROS 2 String message

from publisher_callback import publisher_callback
from listener_callback import listener_callback,  listener_callback2


from lidar import Lidar


class TurtleController(Node):
    def __init__(self):
        super().__init__('controller')
        self.x, self.y, self.theta = 0.0, 0.0, 0.0

        self.vel_msg = Twist()
        self.goal = Point()
        self.i = 0
        self.current_point = 0
        self.returning = False
        self.point_list = []
        self.return_list = [(0.0, 0.0)]
        
        self.running = False

        self.publisher = self.create_publisher(
            msg_type=Twist,
            topic='/cmd_vel',
            qos_profile=10)


        def listener_lambda(msg): return listener_callback(self, msg)
        self.subscription = self.create_subscription(
            msg_type=Odometry,
            topic='/odom',
            callback=listener_lambda,
            qos_profile=10)

        def listener_lambda2(msg): return listener_callback2(self, msg)
        self.subscription2 = self.create_subscription(
            msg_type=String,
            topic='/connection',
            callback=listener_lambda2,
            qos_profile=10)

        self.lidar_ = Lidar(self)

        def publisher_lambda(): return publisher_callback(self)
        self.timer = self.create_timer(
            timer_period_sec=0.02,
            callback=publisher_lambda)



    def logger(self, msg):
        self.get_logger().info(msg)


def main(args=None):
    rclpy.init(args=args)
    controller = TurtleController()
    rclpy.spin(controller)
    controller.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print("Erro: ", str(e))
