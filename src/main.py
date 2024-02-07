"""! @file main.py
This program sets up the pins and timers required for a "MotorDriver" object and creates the object.
It then turns the motor to spin from 0% PWM to 100% PWM to -100% PWM to 0% and waits to repeat again.
"""
import motor_driver
import utime

if __name__ == "__main__":
    # Sets up pins and timers
    a_pin = pyb.Pin(pyb.Pin.board.PA10, pyb.Pin.OUT_PP)
    in1pin = pyb.Pin(pyb.Pin.board.PB4, pyb.Pin.OUT_PP)
    in2pin = pyb.Pin(pyb.Pin.board.PB5, pyb.Pin.OUT_PP)
    a_timer = pyb.Timer(3, freq=1000)

    moe = motor_driver.MotorDriver(a_pin, in1pin, in2pin, a_timer)
        
    # Cycles between -100% and 100% PWM and waiting
    PW = 0
    time_range = 5
    interval = 0.05
    try:
        while True:
            for value in range(5/interval):
                PW += 100/(5/interval)
                moe.set_duty_cycle(PW)
                utime.sleep(interval)
            for value in range(2*5/interval):
                PW -= 100/(5/interval)
                moe.set_duty_cycle(PW)
                utime.sleep(interval)
            for value in range(5/interval):
                PW += 100/(5/interval)
                moe.set_duty_cycle(PW)
                utime.sleep(interval)
            for value in range(5/interval):
                PW = 0
                moe.set_duty_cycle(PW)
                utime.sleep(interval)
    except KeyboardInterrupt:
        PW = 0
        moe.set_duty_cycle(PW)
        print("stopped")