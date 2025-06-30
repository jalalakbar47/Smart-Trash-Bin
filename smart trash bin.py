import RPi.GPIO as GPIO
import time

# === GPIO Pin Setup ===
TRIG = 23         # Ultrasonic sensor trigger pin
ECHO = 24         # Ultrasonic sensor echo pin
SERVO_PIN = 18    # Servo motor control pin

# === Initialize GPIO ===
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(SERVO_PIN, GPIO.OUT)

# === Servo Setup ===
servo = GPIO.PWM(SERVO_PIN, 50)  # 50Hz frequency
servo.start(0)                   # Initial position

def open_lid():
    """Rotate servo to open position"""
    servo.ChangeDutyCycle(7)     # Adjust angle as needed
    time.sleep(0.5)

def close_lid():
    """Rotate servo to closed position"""
    servo.ChangeDutyCycle(2)     # Adjust angle as needed
    time.sleep(0.5)

def measure_distance():
    """Measure distance using ultrasonic sensor"""
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    pulse_start = time.time()
    pulse_end = time.time()

    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = round(pulse_duration * 17150, 2)  # cm
    return distance

# === Main Program Loop ===
try:
    print("🔄 Smart Trash Bin Running... Press Ctrl+C to stop.")
    while True:
        distance = measure_distance()
        print(f"👀 Detected Distance: {distance} cm")

        if distance < 20:  # Threshold for bin to open
            print("🙋 Object detected! Opening lid...")
            open_lid()
            time.sleep(2)  # Wait time before closing
            print("🛑 Closing lid...")
            close_lid()
        else:
            servo.ChangeDutyCycle(0)  # Prevent jitter

        time.sleep(0.5)

except KeyboardInterrupt:
    print("\n🧹 Cleaning up GPIO...")
    servo.stop()
    GPIO.cleanup()
    print("✅ Program terminated safely.")