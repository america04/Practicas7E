from machine import Pin
from time import sleep_ms
import _thread

# Pines del botón y LED azul
boton = Pin(20, Pin.IN, Pin.PULL_DOWN)
azul = Pin(19, Pin.OUT)

# Pines de los 3 semáforos
semaforo1 = {
    "rojo": Pin(14, Pin.OUT),
    "amarillo": Pin(15, Pin.OUT),
    "verde": Pin(16, Pin.OUT)
}

semaforo2 = {
    "rojo": Pin(13, Pin.OUT),
    "amarillo": Pin(12, Pin.OUT),
    "verde": Pin(11, Pin.OUT)
}

semaforo3 = {
    "rojo": Pin(10, Pin.OUT),
    "amarillo": Pin(9, Pin.OUT),
    "verde": Pin(8, Pin.OUT)
}

semaforos = [semaforo1, semaforo2, semaforo3]

# Variable compartida para modo nocturno
modo_nocturno = False

# Función para apagar todos los LEDs
def apagar_todos():
    for s in semaforos:
        for luz in s.values():
            luz.value(0)

# Hilo para manejar el botón
def estado_boton_thread():
    global modo_nocturno
    while True:
        if boton.value() == 1:
            modo_nocturno = not modo_nocturno  # Cambia de estado
            azul.toggle()  # Indicador visual
            sleep_ms(500)  # Evita rebote y repeticiones
        sleep_ms(10)

# Iniciar hilo del botón
_thread.start_new_thread(estado_boton_thread, ())

# Bucle principal
while True:
    if modo_nocturno:
        # Modo nocturno: todos parpadean en amarillo
        apagar_todos()
        for s in semaforos:
            s["amarillo"].value(1)
            s["rojo"].value(1)
        sleep_ms(500)
        for s in semaforos:
            s["amarillo"].value(0)
            s["rojo"].value(0)
        sleep_ms(500)
    else:
        # Modo normal: simulación de semáforos
        # Semáforo 1 en verde, 2 en rojo, 3 en rojo
        apagar_todos()
        semaforo1["verde"].value(1)
        semaforo2["rojo"].value(1)
        semaforo3["rojo"].value(1)
        sleep_ms(2000)

        # Semáforo 1 amarillo
        apagar_todos()
        semaforo1["amarillo"].value(1)
        semaforo2["rojo"].value(1)
        semaforo3["rojo"].value(1)
        sleep_ms(1000)

        # Semáforo 1 rojo, Semáforo 2 verde
        apagar_todos()
        semaforo1["rojo"].value(1)
        semaforo2["verde"].value(1)
        semaforo3["rojo"].value(1)
        sleep_ms(2000)

        # Semáforo 2 amarillo
        apagar_todos()
        semaforo1["rojo"].value(1)
        semaforo2["amarillo"].value(1)
        semaforo3["rojo"].value(1)
        sleep_ms(1000)

        # Semáforo 3 verde
        apagar_todos()
        semaforo1["rojo"].value(1)
        semaforo2["rojo"].value(1)
        semaforo3["verde"].value(1)
        sleep_ms(2000)

        # Semáforo 3 amarillo
        apagar_todos()
        semaforo1["rojo"].value(1)
        semaforo2["rojo"].value(1)
        semaforo3["amarillo"].value(1)
        sleep_ms(1000)
