from machine import Pin
import time

# LEDs
verde = Pin(4, Pin.OUT)
amarillo = Pin(3, Pin.OUT)
rojo = Pin(2, Pin.OUT)

# Entrada desde PIC
modo = Pin(16, Pin.IN)

while True:
    if modo.value() == 0:  # Modo normal
        verde.value(1)
        time.sleep(5)
        verde.value(0)

        amarillo.value(1)
        time.sleep(2)
        amarillo.value(0)

        rojo.value(1)
        time.sleep(8)
        rojo.value(0)
    else:  # Modo nocturno
        amarillo.value(1)
        time.sleep(0.5)
        amarillo.value(0)
        time.sleep(0.5)
        
        rojo.value(1)
        time.sleep(0.5)
        rojo.value(0)
        time.sleep(0.5)