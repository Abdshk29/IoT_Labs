print("Hello, ESP32-S3!")

from machine import Pin, I2C
import machine
import ssd1306
import dht
import time

DHT_PIN = 4  # DHT11 data pin
button = Pin(0, Pin.IN, Pin.PULL_UP)

# Initialize DHT11 sensor
sensor = dht.DHT11(machine.Pin(DHT_PIN))  

# Initialize OLED display
i2c = machine.I2C(scl=machine.Pin(9), sda=machine.Pin(8))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

pressed = False  # Track button state
debounce_time = 0  # Track debounce timing

TEMP_ICON = [
    0b00011000,  #    ██    
    0b00011000,  #    ██    
    0b00011000,  #    ██    
    0b00011000,  #    ██    
    0b00011000,  #    ██    
    0b00111100,  #   ████   
    0b00111100,  #   ████   
    0b00011000   #    ██    
]

HUMIDITY_ICON = [
    0b00001000,  #     █    
    0b00011000,  #    ██    
    0b00111000,  #   ███    
    0b01111000,  #  ████    
    0b01111000,  #  ████    
    0b00111000,  #   ███    
    0b00011000,  #    ██    
    0b00000000   #          
]

def draw_icon(oled, x, y, icon):
    """Draws an 8x8 icon on the OLED at (x, y)."""
    for row in range(8):
        for col in range(8):
            pixel_on = (icon[row] >> (7 - col)) & 1
            oled.pixel(x + col, y + row, pixel_on)


def read_button():
    global pressed, debounce_time
    
    if button.value() == 0:  # Button pressed
        if time.ticks_ms() - debounce_time > 200:  # Simple debounce check
            pressed = not pressed
            debounce_time = time.ticks_ms()
            
            if pressed:
                oled.poweroff()
            else:
                oled.poweron()

# Main loop
while True:
    try:
        read_button()  # Check button state manually
        
        sensor.measure()
        time.sleep(0.2)
        temp = sensor.temperature()
        humidity = sensor.humidity()
        print(temp, humidity)
        
        oled.fill(0)
        draw_icon(oled, 0, 0, TEMP_ICON)
        oled.text("{} C".format(temp), 10, 0)
            
        # Draw humidity icon and text
        draw_icon(oled, 0, 16, HUMIDITY_ICON)
        oled.text("{}%".format(humidity), 10, 16)
        
        oled.show()
    
    except Exception as e:
        print("Error reading DHT11 sensor:", e)

    time.sleep(1)  # Update every second