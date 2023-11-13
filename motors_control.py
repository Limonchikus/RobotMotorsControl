class RobotMotorsControl:
    def __init__(self):
        # Initialize motor speeds to zero
        self.left_motor_speed = 0
        self.right_motor_speed = 0

    def set_motor_speed(self, left_speed, right_speed):
        # Set the speed of left and right motors.
        self.left_motor_speed = left_speed
        self.right_motor_speed = right_speed
        print(f"Left motor speed set to {left_speed}, Right motor speed set to {right_speed}")

    def stop_motors(self):
        # Stop both motors.
        self.set_motor_speed(0, 0)
        print("Motors stopped.")

    def forward(self, speed):
        #Move the robot forward at the given speed.
        self.set_motor_speed(speed, speed)

    def backward(self, speed):
        #Move the robot backward at the given speed.
        self.set_motor_speed(-speed, -speed)

    def turn_left(self, speed):
        #Turn the robot left.
        self.set_motor_speed(0, speed)

    def turn_right(self, speed):
        #Turn the robot right.
        self.set_motor_speed(speed, 0)

# Example usage
robot = RobotMotorsControl()
robot.forward(10)
robot.turn_left(5)
robot.stop_motors()

