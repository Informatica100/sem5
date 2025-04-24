from setuptools import setup, find_packages

package_name = 'servo_control'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/servo_controller.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Burak',
    maintainer_email='burak@outlook.com',
    description='A simple ROS 2 node to control servos via Arduino',
    license='MIT',
    entry_points={
        'console_scripts': [
            'servo_controller = servo_control.ServoControllerNode:main',
        ],
    },
)
