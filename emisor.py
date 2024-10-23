import network
from machine import Pin
import espnow
import utime

# Initialize WiFi in station mode
sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.disconnect()

# Initialize ESP-NOW
esp = espnow.ESPNow()
esp.active(True)

# Set peer address (replace with actual MAC address of the peer)
peer = b'\xFF\xFF\xFF\xFF\xFF\xFF'  # Replace this with the actual peer MAC address
esp.add_peer(peer)

# Initialize button on pin 23
button_pin = Pin(23, Pin.IN, Pin.PULL_UP)

last_button_state = 1  # Assuming button is not pressed (active-low)
debounce_delay = 50  # 50 milliseconds debounce delay

while True:
    current_button_state = button_pin.value()

    if current_button_state != last_button_state:
        utime.sleep_ms(debounce_delay)  # Debounce delay
        current_button_state = button_pin.value()  # Check button state again after debounce

        if current_button_state == 0:
            message = b'ledOn'  # Send as bytes
            print(f"Sending command: {message}")
            esp.send(peer, message)

        else:
            message = b'ledOff'  # Send as bytes
            print(f"Sending command: {message}")
            esp.send(peer, message)

        last_button_state = current_button_state  # Update the last button state