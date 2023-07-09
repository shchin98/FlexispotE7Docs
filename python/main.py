import machine
from machine import UART, Pin

UART_ID = 2
READ_PIN_ID =16
system_led = Pin(2, Pin.OUT)
system_led.value(1)
serial = UART(UART_ID, baudrate=9600, timeout=500)
read_pin = Pin (READ_PIN_ID, Pin.OUT)
read_pin.value(1)

cmd=bytearray(b'\x9b\x06\x02\x01\x00\xfc\xa0\x9d') # standing
serial.write(cmd)