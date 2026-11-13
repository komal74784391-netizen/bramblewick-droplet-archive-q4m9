"""Archived Droplet revision A firmware."""

import time

from machine import Pin

PUL = Pin(2, Pin.OUT)
DIR = Pin(3, Pin.OUT)


def jog(steps, delay_us=1200):
    for _ in range(steps):
        PUL.high()
        time.sleep_us(2)
        PUL.low()
        time.sleep_us(delay_us)


if __name__ == "__main__":
    DIR.high()
    jog(400)
