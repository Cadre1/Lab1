"""! @file motor_driver.py (Copy of step_response.py)
Creates and records the response of the given circuit for a step response input 
"""
import pyb
import utime

class MotorDriver:
    """! 
    This class implements a motor driver for an ME405 kit. 
    """
    def __init__(self, en_pin, in1pin, in2pin, timer):
        """! 
        Creates a motor driver by initializing GPIO
        pins and turning off the motor for safety. 
        @param en_pin (There will be several parameters)
        """"""!
        Led Setup function setting up interrupts, pins, queues, and prints output voltages
        """
        # Initializing Pins
        # Enable Pin
        en_pin = pyb.Pin(en_pin, pyb.Pin.OUT_PP)
        en_pin.high()
        # IN Pin 1
        in1pin = pyb.Pin(in1pin, pyb.Pin.OUT_PP)
        in1pin.low()
        # IN Pin 2
        in2pin = pyb.Pin(in2pin, pyb.Pin.OUT_PP)
        in2pin.low()
        
        # Initializing the PWM Timers
        self.PWM_tim1 = timer.channel(1,
                                      pyb.Timer.PWM,
                                      pin=in1pin,
                                      pulse_width=8000)
        self.PWM_tim2 = timer.channel(2,
                                      pyb.Timer.PWM,
                                      pin=in2pin,
                                      pulse_width=8000)
        print ("Creating a motor driver")


    def set_duty_cycle(self, level):
        """!
        This method sets the duty cycle to be sent
        to the motor to the given level. Positive values
        cause torque in one direction, negative values
        in the opposite direction.
        @param level A signed integer holding the duty
               cycle of the voltage sent to the motor 
        """
        
        if level <= 0:
            self.PWM_tim1.pulse_width_percent(0)
            self.PWM_tim2.pulse_width_percent(-1*level)
        elif level > 0:
            self.PWM_tim1.pulse_width_percent(level)
            self.PWM_tim2.pulse_width_percent(0)
        print (f"Setting duty cycle to {level}")
          
    
if __name__ == "__main__":
    a_pin = pyb.Pin(pyb.Pin.board.PA10, pyb.Pin.OUT_PP)
    in1pin = pyb.Pin(pyb.Pin.board.PB4, pyb.Pin.OUT_PP)
    in2pin = pyb.Pin(pyb.Pin.board.PB5, pyb.Pin.OUT_PP)
    a_timer = pyb.Timer(3, freq=1000)

    moe = MotorDriver(a_pin, in1pin, in2pin, a_timer)
    moe.set_duty_cycle(-42)


#     [PWM_tim1, PWM_tim2] = motor_setup()
#     time_range = 5
#     interval = 0.05
#     PW1 = 0
#     PW2 = 0
#     
#     try:
#         while True:
#             for value in range(5/interval):
#                 PW1 += 100/(5/interval)
#                 PW2 += 0/(5/interval)
#                 set_motor(PWM_tim1, PWM_tim2, PW1, PW2)
#                 utime.sleep(interval)
#                 print(PW1, ', ', PW2)
#             PW1 = 0
#             PW2 = 0
#             set_motor(PWM_tim1, PWM_tim2, PW1, PW2)
#             
#             for value in range(5/interval):
#                 PW1 += 0/(5/interval)
#                 PW2 += 100/(5/interval)
#                 set_motor(PWM_tim1, PWM_tim2, PW1, PW2)
#                 utime.sleep(interval)
#                 print(PW1, ', ', PW2)
#             PW1 = 0
#             PW2 = 0
#             set_motor(PWM_tim1, PWM_tim2, PW1, PW2)
#     except Exception as e:
#         print(e)
#         print("stopped")
#     