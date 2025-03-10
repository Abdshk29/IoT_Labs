print("Hello, Muhammad Abdullah")

import network
import time
import socket
import dht
import machine
from machine import Pin
from neopixel import NeoPixel

# Initialize DHT11 Sensor
DHT_PIN = 4
dht_sensor = dht.DHT11(machine.Pin(DHT_PIN))

def dht_measure():
    dht_sensor.measure()
    time.sleep(0.2)
    temp = dht_sensor.temperature()
    humidity = dht_sensor.humidity()
    return temp, humidity

# Initialize NeoPixel LED
pin = Pin(48, Pin.OUT)   # Set GPIO48 as output
neo = NeoPixel(pin, 1)   # Create NeoPixel driver on GPIO48 for 1 pixel

# WiFi Station Credentials
ssid_st = "Shahmir 2.4G"
password_st = "shahzad1"

print("Connecting to WiFi", end="")
sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect(ssid_st, password_st)

# Wait for connection
for _ in range(10):
    if sta.isconnected():
        break
    time.sleep(1)

if sta.isconnected():
    print("Connected to WiFi!")
    print("IP Address as station:", sta.ifconfig()[0])
else:
    print("Failed to connect")

# Create Access Point
ssid_ap = "ESP32_AP"
password_ap = "12345678"  # Minimum 8 characters
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=ssid_ap, password=password_ap, authmode=network.AUTH_WPA2_PSK)

print("Access Point Active")
print("AP IP Address:", ap.ifconfig()[0])

# Web Server Function
def web_page():
    temp, humidity = dht_measure()
    html = f"""<!DOCTYPE html>
    <html>
    <head><title>ESP32 RGB LED Control</title></head>
    <body>
    <h1>ESP32 RGB LED Control</h1>
    <p><a href="/?RGB=red"><button>Turn RGB RED</button></a></p>
    <p><a href="/?RGB=green"><button>Turn RGB GREEN</button></a></p>
    <p><a href="/?RGB=blue"><button>Turn RGB BLUE</button></a></p>
    <br>
    <h1>Temperature and Humidity</h1>
    <h2>Temp: {temp} &#8451;</h2>
    <h2>Humidity: {humidity}%</h2>
    </body>
    </html>"""
    return html

# Start Web Server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 80))
s.listen(5)

while True:
    conn, addr = s.accept()
    print("Connection from:", addr)
    request = conn.recv(1024).decode()
    print("Request:", request)
    
    if "/?RGB=red" in request:
        neo[0] = (255, 0, 0)  # Set NeoPixel to red
        neo.write()
    elif "/?RGB=green" in request:
        neo[0] = (0, 255, 0)  # Set NeoPixel to green
        neo.write()
    elif "/?RGB=blue" in request:
        neo[0] = (0, 0, 255)  # Set NeoPixel to blue
        neo.write()
        
    response = web_page()
    conn.send("HTTP/1.1 200 OK\nContent-Type: text/html\n\n".encode())
    conn.send(response.encode())
    conn.close()