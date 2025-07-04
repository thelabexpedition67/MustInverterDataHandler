import time  # Import the time module for sleep
import serial
from routines import *
from mapper import *

# Define the serial port (change the port name as needed)
serial_port = "/dev/ttyUSB0"

# Define the configuration for command strings # Set to True or False as needed
# This configuration can slow down the execution
command_config = {
    "command_1_enabled": False,  # not really needed/implemented
    "command_2_enabled": False, 
    "command_3_enabled": True,   # good data
    "command_4_enabled": False, 
    "command_5_enabled": False, 
    "command_6_enabled": True    # good data
}

# Construct the command strings based on the configuration
charger_id = '04'
inverter_id = '04'

command_string_1 = f"{charger_id} 03 27 11 00 0A"
command_string_2 = f"{charger_id} 03 27 75 00 18"
command_string_3 = f"{charger_id} 03 3B 61 00 15"
command_string_4 = f"{inverter_id} 03 4E 21 00 10"
command_string_5 = f"{inverter_id} 03 4E 85 00 2C"
command_string_6 = f"{inverter_id} 03 62 71 00 4F"

try:

    # Calculate the CRC value for the command
    command_bytes_1 = generate_crc(command_string_1)
    command_bytes_2 = generate_crc(command_string_2)
    command_bytes_3 = generate_crc(command_string_3)
    command_bytes_4 = generate_crc(command_string_4)
    command_bytes_5 = generate_crc(command_string_5)
    command_bytes_6 = generate_crc(command_string_6)

    # Perform other operations with the serial connection
    ser = serial.Serial(serial_port, baudrate=19200, timeout=1)
    ser.setRTS(True)
    responses = []

    if command_config["command_1_enabled"]:
        response_1 = get_part_arr(ser, command_bytes_1, 10, 20)
        time.sleep(0.03)
        responses.append(convert_partArr1_to_json(response_1))

    if command_config["command_2_enabled"]:
        response_2 = get_part_arr(ser, command_bytes_2, 24, 20)
        time.sleep(0.03)
        responses.append(convert_partArr2_to_json(response_2))

    if command_config["command_3_enabled"]:
        response_3 = get_part_arr(ser, command_bytes_3, 21, 20)
        time.sleep(0.03)
        responses.append(convert_partArr3_to_json(response_3))

    if command_config["command_4_enabled"]:
        response_4 = get_part_arr(ser, command_bytes_4, 16, 20)
        time.sleep(0.03)
        responses.append(convert_partArr4_to_json(response_4))

    if command_config["command_5_enabled"]:
        response_5 = get_part_arr(ser, command_bytes_5, 44, 20)
        time.sleep(0.03)
        responses.append(convert_partArr5_to_json(response_5))

    if command_config["command_6_enabled"]:
        response_6 = get_part_arr(ser, command_bytes_6, 79, 40)
        responses.append(convert_partArr6_to_json(response_6))

    # Close the serial connection when done
    ser.close()

    # Example usage:
    merged_result = merge_json(responses)
    print(merged_result)

except Exception as e:
    print("Error:", str(e))
