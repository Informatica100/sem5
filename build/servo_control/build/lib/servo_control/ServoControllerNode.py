import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray
import serial

class ServoController(Node):
    def __init__(self):
        super().__init__('servo_controller')
        self.subscription = self.create_subscription(Float64MultiArray, 'servo_angles', self.listener_callback, 10)
        try:
            self.arduino = serial.Serial('/dev/ttyS3', 9600)
            # self.arduino = serial.Serial('/dev/ttyACM0', 9600)
            self.get_logger().info("Verbonden met Arduino")
        except serial.SerialException as e:
            self.get_logger().error(f"Kan Arduino niet vinden: {e}")

    def listener_callback(self, msg):
        try:
            angle1, angle2 = msg.data
            command = f"{int(angle1)},{int(angle2)}\n"
            self.arduino.write(command.encode())
            self.get_logger().info(f"Verstuurd naar Arduino: {command.strip()}")
        except Exception as e:
            self.get_logger().error(f"Fout bij het sturen: {e}")

def main(args=None):
    rclpy.init(args=args)
    node = ServoController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
