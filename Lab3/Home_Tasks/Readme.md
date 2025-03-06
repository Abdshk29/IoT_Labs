# Task-1:- Blow on the sensor and observe whether it detects minor changes in temperature and humidity.
After blowing on the sensor 4-5 times, the humidity rose from 43% to 82% and Temparature rose from 23C to 25C.

# Task-2:- Running the Code With Interrupt
When the code is run with interrupts, the temperature and humidity values are displayed on the serial monitor. On pressing the boot button, display is turned off. After pressing the boot button again, display is turned on.
When the code is run without interrupts, the temperature and humidity values are displayed on the serial monitor but pressing the boot button is having no effect on it since it doesnt recognize the button which was causing the interrupt.

# Task-3:- Understanding debouncing issue

# Debounce Issue:
A debounce issue occurs when a button press or other input generates multiple rapid signals instead of a single clean one. This happens due to mechanical vibrations in switches, causing false triggers in ESP32-S3 when using Thonny.

# Debounce Solution:
1-Prevents multiple unintended triggers
2-Ensures accurate input detection
3-Improves reliability in IoT applications

# Applications of Debounce:
1-IoT Devices & Home Automation – Prevents false triggering of relays, lights, or appliances.
2-Embedded Systems & Microcontrollers – Ensures accurate sensor and button inputs in ESP32, Arduino, etc.
3-Industrial Automation – Avoids multiple activations of machinery and safety systems.
4-Medical Devices – Ensures correct operation of critical equipment like heart monitors and ventilators.
5-Gaming Controllers & Keyboards – Prevents multiple key presses from a single tap.

# Why Debounce?
Debounce occurs due to mechanical vibrations in switches, electrical noise, or high-speed processing detecting multiple false signals. Microcontrollers like ESP32-S3 register these rapid fluctuations as multiple presses. It can be fixed using software delays, state tracking, or hardware filters like capacitors.

# Is debounce a compiler error?
No, debounce is not a compiler error. It is a hardware-related issue caused by mechanical vibrations or electrical noise in input signals (e.g., buttons, switches).

# Is debounce a logical error?
Yes, debounce can be considered a logical error in certain cases because it leads to unintended multiple triggers in input handling.

# How to fix debounce?
Debounce can be fixed using software delays, state tracking, or hardware filters like capacitors. It can be implemented in different ways based on the specific application and requirements.

# Task-4:- Why Do We Use Interrupts
Interrupts allow a microcontroller (e.g., ESP32-S3) to respond immediately to external events without continuously checking for changes (polling). This results in faster and more responsive responses to user interactions, such as button presses or sensor data changes.

1-Efficient CPU Usage – The processor can perform other tasks instead of waiting for an event.
2-Faster Response Time – Ensures immediate action when an event occurs (e.g., button press, sensor input).
3-Power Saving – Helps in low-power applications by waking the device only when needed.
4-Better Real-Time Performance – Essential for time-sensitive tasks like motor control, signal processing, and IoT applications.

# How does interrupt lower the processing cost of the micro-controller?
Interrupts reduce the processing cost by allowing the microcontroller to execute tasks only when necessary, rather than continuously checking for events (polling).



