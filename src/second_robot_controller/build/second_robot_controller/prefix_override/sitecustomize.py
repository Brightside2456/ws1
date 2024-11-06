import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/sefahb13/ws1/src/second_robot_controller/install/second_robot_controller'
