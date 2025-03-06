print("Hello, ESP32-S3!")

from machine import Pin, I2C, Timer
import machine
import ssd1306 
import dht
import time

DHT_PIN = 4  # DHT22 data pin
button = Pin(0, Pin.IN, Pin.PULL_UP)
# Initialize DHT22 sensor
dht_sensor = dht.DHT11(machine.Pin(DHT_PIN)) # change DHT11 fr physical device

# Initialize OLED display
i2c = machine.I2C(scl=machine.Pin(9), sda=machine.Pin(8))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

pressed= False
debounce_timer = None

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

def button_pressed(pin):
    global  debounce_timer, pressed  # Declare variables as global

    if debounce_timer is None:
        pressed= not pressed
        if pressed:
            oled.poweroff()
           
        else:
            oled.poweron()

        # Start a timer for debounce period (e.g., 200 milliseconds)
        debounce_timer = Timer(0)
        debounce_timer.init(mode=Timer.ONE_SHOT, period=200, callback=debounce_callback)

def debounce_callback(timer):
    global debounce_timer
    debounce_timer = None

# Attach the interrupt to the button's rising edge
button.irq(trigger=Pin.IRQ_FALLING, handler=button_pressed)


# Main loop
while True:
    try:
        dht_sensor.measure()
        time.sleep(.2)
        temp = dht_sensor.temperature()
        humidity = dht_sensor.humidity()
        print(temp, humidity)
        oled.fill(0)
        draw_icon(oled, 0, 0, TEMP_ICON)
        oled.text("{} C".format(temp), 10, 0)
            
        # Draw humidity icon and text
        draw_icon(oled, 0, 16, HUMIDITY_ICON)
        oled.text("{}%".format(humidity), 10, 16)
        oled.show()


    except Exception as e:
        print("Error reading DHT22 sensor:", e)
    
        
    time.sleep(1)  # Update every 2 seconds