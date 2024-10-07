import time
from machine import Pin

# Define and initialize sw5
sw5 = Pin(22, Pin.IN)  
led1 = Pin(16, Pin.OUT)

led_state = False
last_button_state = sw5.value()

while True:
    current_button_state = sw5.value()
    
    if current_button_state != last_button_state:
        time.sleep(0.01)  # Debounce delay
    elif current_button_state == 1:
            led_state = not led_state
    elif led_state:
                led1.on()
    else:
                led1.off()
    
    last_button_state = current_button_state
