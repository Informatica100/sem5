import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/burak/arduinobot_ws2/install/arduino_py_examples'
