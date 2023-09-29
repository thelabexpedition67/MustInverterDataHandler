import time  # Import the time module for sleep
import serial

def bytes_to_data_array(byte_array, arr_length):
    if len(byte_array) != arr_length * 2 + 5:
        raise Exception(f"Error by byte array length, require: {arr_length * 2 + 5}, actually: {len(byte_array)}")

    str_array = [""] * arr_length
    num1 = 0
    index = 0
    empty = ""

    for num2 in byte_array:
        if num1 <= 2 or num1 >= len(byte_array) - 2:
            num1 += 1
        else:
            if num1 % 2 == 1:
                empty = format(num2, '02X')
            if num1 % 2 == 0:
                str_value = empty + format(num2, '02X')
                str_array[index] = str_value
                empty = ""
                index += 1
            num1 += 1

    return str_array

def generate_crc(hex_string):
    hex_string = hex_string.replace(" ", "")
    if len(hex_string) % 2 != 0:
        hex_string += " "
    num_array1 = bytearray.fromhex(hex_string)
    max_value1 = 0xFF
    max_value2 = 0xFF

    for num1 in num_array1:
        max_value1 ^= num1
        for _ in range(8):
            num2 = max_value2
            num3 = max_value1
            max_value2 >>= 1
            max_value1 >>= 1
            if (num2 & 1) == 1:
                max_value1 |= 0x80
            if (num3 & 1) == 1:
                max_value2 ^= 0xA0
                max_value1 ^= 0x01

    length = len(num_array1) + 2
    num_array2 = bytearray(length)
    num_array2[:-2] = num_array1
    num_array2[-1] = max_value2
    num_array2[-2] = max_value1
    return num_array2

def get_part_arr(ser, command_bytes, data_length, max_loop_count=20):
    try:
        ser.write(command_bytes)
        num = 0
        while ser.in_waiting != (data_length * 2 + 5):
            if num >= max_loop_count:
                return None
            time.sleep(0.1)  # Adjust sleep duration as needed
            num += 1
        num_array = ser.read(ser.in_waiting)
        return bytes_to_data_array(num_array, data_length)
    except Exception as e:
        print("Error:", str(e))
        return None
        
def get_part_arr_serialin(serial_port, command_bytes, data_length, max_loop_count=20):
    try:
        with serial.Serial(serial_port, baudrate=19200, timeout=1) as ser:
            ser.setRTS(True)
            ser.write(command_bytes)
            num = 0
            while ser.in_waiting != (data_length * 2 + 5):
                if num >= max_loop_count:
                    return None
                time.sleep(0.1)  # Adjust sleep duration as needed
                num += 1
            num_array = ser.read(ser.in_waiting)
            return bytes_to_data_array(num_array,data_length)
    except Exception as e:
        print("Error:", str(e))
        return None
