# Lab1
 Group 18's Lab 1

This project contains a main.py file and a motor_driver.py file. The program, motor_driver.py, contains a class, MotorDriver, that initializes the GPIO pins as PWM outputs and the timer required for the L6206 motor driver shield. This program also allows for the motor's PWM duty cycle to be set to run the motor forwards and backwards corresponding to a positive or negative value, respectively. The program, main.py, runs a test for this class that loops the motor's PWM duty cycle between -100% to 100% with a pause after each loop.
