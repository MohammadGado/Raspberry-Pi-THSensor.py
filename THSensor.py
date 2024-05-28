from sense_hat import SenseHat
import json
from time import sleep
import time
from socket import *

# Initialize Sense HAT
s = SenseHat()
s.low_light = True
sense = SenseHat()
sense.low_light = True
sense.clear()

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105,180)
lightblue = (0,175,255)


LB = lightblue
O = nothing
B = blue
snowflake = [
LB, O, O, LB, LB, O, O, LB,
O, LB, O, LB, LB, O, LB, O,
O, O, LB, LB, LB, LB, O, O,
LB, LB, LB, LB,LB, LB, LB, LB,
LB, LB, LB, LB, LB, LB, LB, LB,
O, O, LB, LB, LB, LB, O, O,
O, LB, O, LB, LB, O, LB, O,
LB, O, O, LB, LB, O, O, LB,
]
waterdrop = [
O, O, O, B, O, O, O, O,
O, O, O, B, O, O, O, O,
O, O, B, B, B, O, O, O,
O, B, B, B, B, B, O, O,
O, B, B, B, B, B, O, O,
O, B, B, B, B, B, O, O,
O, O, B, B, B, O, O, O,
O, O, O, O, O, O, O, O,
]

HumidAndFrozen = [
LB, O, O, LB, B, O, O, O,
O, LB, O, LB, B, O, O, O,
O, O, LB, LB, B, B, O, O,
LB, LB, LB, LB, B, B, O, O,
LB, LB, LB, LB, B, B, B, O,
O, O, LB, LB, B, B, B, O,
O, LB, O, LB, B, B, B, O,
LB, O, O, LB, B, B, O, O,
]
# Server details (IP address of your PC)
serverName = '255.255.255.255'  
serverPort = 5005

# Configure UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

# Sensor name
sensor_name = "Sense HAT"

# Data collection and transmission loop
while True:
    temperature = sense.get_temperature()  # Get temperature
    humidity = sense.get_humidity()  # Get humidity

 if temperature <= 5 and humidity >= 65:
       s.set_pixels(HumidAndFrozen)

    elif temperature <= 5:
       s.set_pixels(snowflake)

    elif humidity >= 65:
       s.set_pixels(waterdrop)


    else:
        s.clear(O)


    # Create data dictionary
    data = {"SensorName": sensor_name, "Temperature": temperature, "Humidity": humidity}
    # Convert dictionary to JSON string
    message = json.dumps(data)
    # Print data for debugging
    print(data)

    # Send data via UDP
    clientSocket.sendto(message.encode(), (serverName, serverPort))

    # Wait for 5 seconds before next reading
    sleep(5)
