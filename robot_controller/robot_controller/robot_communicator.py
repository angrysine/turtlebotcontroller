# Basic ROS 2 program to publish real-time streaming 
# video from your built-in webcam
# Author:
# - Addison Sears-Collins
# - https://automaticaddison.com
  
# Import the necessary libraries
import rclpy # Python Client Library for ROS 2
from rclpy.node import Node # Handles the creation of nodes
from std_msgs.msg import String  # Standard ROS 2 String message
import json


class RobotCommunicator(Node):
  """
  this class will conenct with robot and recieve data
  """
  def listener_callback(self, data):
    #publish the message
    if not self.connected:
        self.connected = True
        self.logger("connected")
            # Create the message

        
    if not self.running:
      data = json.loads(data)
      if ["graph","nodes","edges" ] in data.keys():
        self.running = True
        self.logger("running")
        return data
  def logger(self,msg):
    self.get_logger().info(str(msg))
    
 
      # Display the message on the console
      #self.get_logger().info('Publishing message: "%s"' % msg.data)

  
  def __init__(self):
    """
    Class constructor to set up the node
    """
    # Initiate the Node class's constructor and give it a name
    super().__init__('connection_starter')
    self.connected = False
    self.running = False
    
      
    # We will publish a message every 0.1 seconds
    timer_period = 0.1  # seconds
      
    # Create the timer
    self.timer = self.create_timer(timer_period, self.timer_callback)

    # Create the subscriber. This subscriber will receive an json string
    self.subscription = self.create_subscription(
        String,
        'connection',
        self.listener_callback,
        10)
    self.subscription  # prevent unused variable warning
         

   
        
        
        
        
  
def main(args=None):
  
  # Initialize the rclpy library
  rclpy.init(args=args)
  
  # Create the node
  robot_communicator = RobotCommunicator()
  
  # Spin the node so the callback function is called.
  rclpy.spin(robot_communicator)
  
  # Destroy the node explicitly
  # (optional - otherwise it will be done automatically
  # when the garbage collector destroys the node object)
  robot_communicator.destroy_node()
  
  # Shutdown the ROS client library for Python
  rclpy.shutdown()
  
if __name__ == '__main__':
  main()