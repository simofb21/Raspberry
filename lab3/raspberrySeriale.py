import serial

# Configura la porta seriale
ser = serial.Serial(
    port='/dev/serial0', 
    baudrate=9600,        
    timeout=1            
)

print("Listening for messages from ESP32...")

try:
    while True:
        if ser.in_waiting > 0: 
            data = ser.readline().decode('utf-8').strip()
            print(f"Received: {data}")
except KeyboardInterrupt:
    print("\nExiting...")
finally:
    ser.close()
