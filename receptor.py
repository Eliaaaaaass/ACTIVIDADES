import network
import espnow
import machine

# Set up WiFi in station mode
sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.disconnect()

# Initialize ESP-NOW
esp = espnow.ESPNow()
esp.active(True)

# Set up LED on pin 22
led_pin = machine.Pin(22, machine.Pin.OUT)

while True:
    _, msg = esp.recv()
    if msg:
        if msg == b'ledOn':
            print("Turning on LED")
            led_pin.on()
        elif msg == b'ledOff':
            print("Turning off LED")
            led_pin.off()
        else:
            print("Unknown message!")
            