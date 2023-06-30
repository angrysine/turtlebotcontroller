from tf_transformations import euler_from_quaternion
import json
from .build_goals import build_goals
from math import pi 


def listener_callback(node, msg):
 
    node.x = msg.pose.pose.position.x
    node.y = msg.pose.pose.position.y
    rot = msg.pose.pose.orientation
    _, _, temp = euler_from_quaternion([rot.x, rot.y, rot.z, rot.w])
    node.theta = temp 
    # node.get_logger().info(f"x={node.x:3f}, y={node.y:3f}")


def listener_callback2(node, data):
    # publish the message
    
    
    # node.logger(str(data.data))
    if not node.running:
        
        
        
        if not data.data == "[]".strip():
            
            
            
            node.point_list = build_goals(json.loads(data.data))
        
            node.running = True

    if node.running:
        
        if data.data.strip() == "parar inspeção".strip():
               node.stop = True

    
