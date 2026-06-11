import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/t_b/ros2_ws/src/UR-MiR-mobile-manipulator/install/point_cloud_functions'
