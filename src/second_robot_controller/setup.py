from setuptools import find_packages, setup

package_name = 'second_robot_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sefahb13',
    maintainer_email='sefahb13@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "first_node = second_robot_controller.first_node:main",
            "first_pub_node = second_robot_controller.drive_circles:main",
            "first_sub_node = second_robot_controller.pose_sub:main",
            "first_pub_sub_node = second_robot_controller.pub_sub:main"
        ],
    },
)
