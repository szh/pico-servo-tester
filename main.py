import time

from machine import PWM, Pin

pi_led = Pin(25, Pin.OUT)
led = Pin(10, Pin.OUT)
btn_cycle = Pin(14, Pin.IN, Pin.PULL_DOWN)
btn_low = Pin(11, Pin.IN, Pin.PULL_DOWN)
btn_mid = Pin(12, Pin.IN, Pin.PULL_DOWN)
btn_max = Pin(13, Pin.IN, Pin.PULL_DOWN)
servo = PWM(Pin(16))
servo.freq(50)

MIN = 1000000
MAX = 2000000
MID = 1500000

WAIT_TIME = 0.5

pi_led.on()


def cycle_servo():
    servo.duty_ns(MIN)
    time.sleep(WAIT_TIME)
    servo.duty_ns(MID)
    time.sleep(WAIT_TIME)
    servo.duty_ns(MAX)
    time.sleep(WAIT_TIME)


def goto_min():
    servo.duty_ns(MIN)


def goto_max():
    servo.duty_ns(MAX)


def goto_mid():
    servo.duty_ns(MID)


while True:
    if btn_cycle.value():
        led.value(1)
        cycle_servo()
    elif btn_low.value():
        led.value(1)
        goto_min()
    elif btn_mid.value():
        led.value(1)
        goto_mid()
    elif btn_max.value():
        led.value(1)
        goto_max()
    else:
        led.value(0)
