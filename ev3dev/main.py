#!/usr/bin/env python3
from ev3dev2.motor import Motor, OUTPUT_A, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor, InfraredSensor # UltrasonicSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound

class DriveBase:
    def __init__(self, left_motor, right_motor, wheel_diameter, axle_track):
        self.left_motor = left_motor
        self.right_motor = right_motor
        self.wheel_diameter = wheel_diameter
        self.axle_track = axle_track

    def drive(self, millimeters, rotations):
        self.left_motor.on_for_rotations(millimeters, rotations)
        self.right_motor.on_for_rotations(millimeters, rotations)

    def drive_time(self, distance, x, milliseconds):
        self.left_motor.on_for_seconds(milliseconds / 1000)
        self.right_motor.on_for_seconds(milliseconds / 1000)

sound = Sound()
#ultrasonicSensor = UltrasonicSensor()
infraredSensor = InfraredSensor(INPUT_1)
infraredSensor.mode = infraredSensor.MODE_IR_REMOTE
# Play a sound.
sound.beep()
# Initialize the Ultrasonic Sensor. It is used to detect
# obstacles as the robot drives around.
#obstacle_sensor = infraredSensor(INPUT_1)
# Initialize two motors with default settings on Port B and Port C.
# These will be the left and right motors of the drive base.
left_motor = Motor(OUTPUT_B)
right_motor = Motor(OUTPUT_C)
# The wheel diameter of the Robot Educator is 56 millimeters.
wheel_diameter = 56
# The axle track is the distance between the centers of each of the wheels.
# For the Robot Educator this is 114 millimeters.
axle_track = 114
# The DriveBase is composed of two motors, with a wheel on each motor.
# The wheel_diameter and axle_track values are used to make the motors
# move at the correct speed when you give a motor command.

robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)
# The following loop makes the robot drive forward until it detects an
# obstacle. Then it backs up and turns around. It keeps on doing this
# until you stop the program.
while True:
    # Begin driving forward at 200 millimeters per second.
    robot.drive(50, 5)
    # Wait until an obstacle is detected. This is done by repeatedly
    # doing nothing (waiting for 10 milliseconds) while the measured
    # distance is still greater than 300 mm.
    while infraredSensor.proximity > 50:
#    while obstacle_sensor.distance_centimeters() > 300:
        wait(10)
        # Drive backward at 100 millimeters per second. Keep going for 2 seconds.
        robot.drive_time(-100, 0, 2000)
        # Turn around at 60 degrees per second, around the midpoint between
        # the wheels. Keep going for 2 seconds.

    robot.drive_time(0, 60, 2000)
