#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include "DHT.h"

// DHT11 Configuration
#define DHTPIN 4         // GPIO pin where DHT11 data pin is connected
#define DHTTYPE DHT11    // Sensor type DHT11
DHT dht(DHTPIN, DHTTYPE);

// OLED Configuration
#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1);

// LED Configuration
// #define LED_PIN 2       // Built-in LED on ESP32 usually GPIO2

void setup() {
  // Start Serial
  Serial.begin(115200);

  // Initialize DHT11
  dht.begin();

  // Initialize OLED
  if(!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    Serial.println(F("SSD1306 allocation failed"));
    for(;;); // Stop here if OLED not found
  }
  
  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(SSD1306_WHITE);

  // Initialize LED
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  // LED Blink
  digitalWrite(LED_BUILTIN, HIGH); // LED ON
  delay(500);

  // Read DHT11 Sensor
  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature(); // Default in Celsius

  // Check if any reads failed
  if (isnan(humidity) || isnan(temperature)) {
    Serial.println(F("Failed to read from DHT sensor!"));
    display.clearDisplay();
    display.setCursor(0,10);
    display.println("Sensor Error");
    display.display();
  } else {
    // Print to Serial
    Serial.print(F("Humidity: "));
    Serial.print(humidity);
    Serial.print(F("%  Temperature: "));
    Serial.print(temperature);
    Serial.println(F("°C"));

    // Print to OLED
    display.clearDisplay();
    display.setCursor(0,0);
    display.println("Temp: " + String(temperature) + " C");
    display.println("Humidity: " + String(humidity) + " %");
    display.display();
  }

  digitalWrite(LED_BUILTIN, LOW); // LED OFF
  delay(500); // Wait before next reading
}
