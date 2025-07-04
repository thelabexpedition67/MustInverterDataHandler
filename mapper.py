import json

# Function to convert a hex string representing a two's complement signed integer to an integer value.
# It correctly handles negative values by interpreting the two's complement representation.
# Input: Hex string, e.g., "FF70"
# Output: Integer value, e.g., -142
def twos_complement(hex_str, num_bits=16):
    value = int (hex_str, 16 )
    if (value & (1 << (num_bits - 1))) != 0:
        # It's a negative value, perform two's complement
        value -= 1 << num_bits
    return value

# Map a hex string to a version, e.g. 1.00.00
def to_version(hex_str):
    value = twos_complement(hex_str)
    if hex_str != "0" and value != 0:
        major = value // 10000
        minor = (value // 100) % 100
        patch = value % 100
        return f"{major}.{minor:02}.{patch:02}"
    else:
        return "1.00.00"

def merge_json(json_list):
    merged_json = {}
    
    for json_str in json_list:
        try:
            data = json.loads(json_str)
            if isinstance(data, dict):
                merged_json.update(data)
        except json.JSONDecodeError:
            print(f"Skipping invalid JSON: {json_str}")
    
    return json.dumps(merged_json, indent=4)

#not implemented/needed
def convert_partArr1_to_json(partArr1):
    if partArr1 is not None and len(partArr1) == 10:
        return json.dumps(partArr1, indent=4)
    else:
        return None

def convert_partArr2_to_json(partArr2):
    if partArr2 is not None and len(partArr2) == 24:
        result = {
            "ChargerWorkEnable": twos_complement(partArr2[0]),
            "AbsorbVoltage": "{:.2f}".format(float (twos_complement(partArr2[1]) * 0.1)),
            "FloatVoltage": "{:.2f}".format(float (twos_complement(partArr2[2]) * 0.1)),
            "AbsorptionVoltage": "{:.2f}".format(float (twos_complement(partArr2[3]) * 0.1)),
            "BatteryLowVoltage": "{:.2f}".format(float (twos_complement(partArr2[4]) * 0.1)),
            "BatteryHighVoltage": "{:.2f}".format(float (twos_complement(partArr2[6]) * 0.1)),
            "MaxChargerCurrent": "{:.2f}".format(float (twos_complement(partArr2[7]) * 0.1)),
            "AbsorbChargerCurrent": "{:.2f}".format(float (twos_complement(partArr2[8]) * 0.1)),
            "BatteryType": twos_complement(partArr2[9]),
            "BatteryAh": twos_complement(partArr2[10]),
            "RemoveTheAccumulatedData": twos_complement(partArr2[11]),
            "BatteryEqualizationEnable": twos_complement(partArr2[17]),
            "BatteryEqualizationVoltage": "{:.2f}".format(float (twos_complement(partArr2[18]) * 0.1)),
            "BatteryEqualizedTime": twos_complement(partArr2[20]),
            "BatteryEqualizedTimeout": twos_complement(partArr2[21]),
            "EqualizationInterval": twos_complement(partArr2[22]),
            "EqualizationActivedImmediately": twos_complement(partArr2[23])
        }

        return json.dumps(result, indent=4)
    else:
        return None

def convert_partArr3_to_json(partArr3):
    if partArr3 is not None and len(partArr3) == 21:
        result = {
            "ChargerWorkstate": twos_complement(partArr3[0]),
            "MpptState": twos_complement(partArr3[1]),
            "ChargingState": twos_complement(partArr3[2]),
            "PvVoltage": "{:.2f}".format(float (twos_complement(partArr3[4]) * 0.1)),
            "BatteryVoltage": "{:.2f}".format(float (twos_complement(partArr3[5]) * 0.1)),
            "ChargerCurrent": "{:.2f}".format(float (twos_complement(partArr3[6]) * 0.1)),
            "ChargerPower": twos_complement(partArr3[7]),
            "RadiatorTemperature": twos_complement(partArr3[8]),
            "ExternalTemperature": twos_complement(partArr3[9]),
            "BatteryRelay": twos_complement(partArr3[10]),
            "PvRelay": twos_complement(partArr3[11]),
            "ErrorMessage": twos_complement(partArr3[12]),
            "WarningMessage": twos_complement(partArr3[13]),
            "BattVolGrade": twos_complement(partArr3[14]),
            "RatedCurrent": "{:.2f}".format(float(twos_complement(partArr3[15]) * 0.1)),
            "AccumulatedPower": "{:.2f}".format(float((twos_complement(partArr3[16]) * 1000) +  (twos_complement(partArr3[17]) * 0.1))),
            "AccumulatedTime": f"{int(partArr3[18]):02}:{int(partArr3[19]):02}:{int(partArr3[20]):02}"
        }
        return json.dumps(result, indent=4)
    else:
        return None

def convert_partArr4_to_json(partArr4):
    if partArr4 is not None and len(partArr4) == 16:
        int16_4 = twos_complement(partArr4[4])
        int16_5 = twos_complement(partArr4[0])
        str1 = ""

        # Map int16_5 to InverterMachineType
        if int16_5 == 1600:
            str1 = "PC1600"
        elif int16_5 == 1800:
            str1 = "PV1800" if int16_4 > 20000 else "PH1800"
        elif int16_5 == 3000:
            str1 = "PH3000"
        elif int16_5 == 3500:
            str1 = "PV3500"

        result = {
            "InverterMachineType": str1,
            "InverterSerialNumber": partArr4[1] + partArr4[2]
        }

        result["InverterHardwareVersion"] = to_version(partArr4[3])
        result["InverterSoftwareVersion"] = to_version(partArr4[4])

        # Add the remaining fields
        result["InverterBatteryVoltageC"] = partArr4[8]
        result["InverterVoltageC"] = partArr4[9]
        result["GridVoltageC"] = partArr4[10]
        result["BusVoltageC"] = partArr4[11]
        result["ControlCurrentC"] = partArr4[12]
        result["InverterCurrentC"] = partArr4[13]
        result["GridCurrentC"] = partArr4[14]
        result["LoadCurrentC"] = partArr4[15]

        return json.dumps(result, indent=4)
    else:
        return None

def convert_partArr6_to_json(partArr6):
    if partArr6 is not None and len(partArr6) == 79:
        result = {
            "WorkState":  (twos_complement(partArr6[0])),
            "AcVoltageGrade": twos_complement(partArr6[1]),
            "RatedPower": twos_complement(partArr6[2]),
            "InverterBatteryVoltage": "{:.2f}".format(float (twos_complement(partArr6[4]) * 0.1)),
            "InverterVoltage": "{:.2f}".format(float (twos_complement(partArr6[5]) * 0.1)),
            "GridVoltage": "{:.2f}".format(float (twos_complement(partArr6[6]) * 0.1)),
            "BusVoltage": "{:.2f}".format(float (twos_complement(partArr6[7]) * 0.1)),
            "ControlCurrent": "{:.2f}".format(float (twos_complement(partArr6[8]) * 0.1)),
            "InverterCurrent": "{:.2f}".format(float (twos_complement(partArr6[9]) * 0.1)),
            "GridCurrent": "{:.2f}".format(float (twos_complement(partArr6[10]) * 0.1)),
            "LoadCurrent": "{:.2f}".format(float (twos_complement(partArr6[11]) * 0.1)),
            "PInverter": twos_complement(partArr6[12]),
            "PGrid": twos_complement(partArr6[13]),
            "PLoad": twos_complement(partArr6[14]),
            "LoadPercent": twos_complement(partArr6[15]),
            "SInverter": twos_complement(partArr6[16]),
            "SGrid": twos_complement(partArr6[17]),
            "Sload": twos_complement(partArr6[18]),
            "Qinverter": twos_complement(partArr6[20]),
            "Qgrid": twos_complement(partArr6[21]),
            "Qload": twos_complement(partArr6[22]),
            "InverterFrequency": "{:.2f}".format(float (twos_complement(partArr6[24]) * 0.01)),
            "GridFrequency": "{:.2f}".format(float (twos_complement(partArr6[25]) * 0.01)),
            "InverterMaxNumber": partArr6[28],
            "CombineType": partArr6[29],
            "InverterNumber": partArr6[30],
            "AcRadiatorTemperature": twos_complement(partArr6[32]),
            "TransformerTemperature": twos_complement(partArr6[33]),
            "DcRadiatorTemperature": twos_complement(partArr6[34]),
            "InverterRelayState":  (twos_complement(partArr6[36])),
            "GridRelayState":  (twos_complement(partArr6[37])),
            "LoadRelayState":  (twos_complement(partArr6[38])),
            "N_LineRelayState":  (twos_complement(partArr6[39])),
            "DCRelayState":  (twos_complement(partArr6[40])),
            "EarthRelayState":  (twos_complement(partArr6[41])),
            "AccumulatedChargerPower": "{:.2f}".format(float (twos_complement(partArr6[44]) * 1000 + twos_complement(partArr6[45]) * 0.1)),
            "AccumulatedDischargerPower": "{:.2f}".format(float (twos_complement(partArr6[46]) * 1000 + twos_complement(partArr6[47]) * 0.1)),
            "AccumulatedBuyPower": "{:.2f}".format(float (twos_complement(partArr6[48]) * 1000 + twos_complement(partArr6[49]) * 0.1)),
            "AccumulatedSellPower": "{:.2f}".format(float (twos_complement(partArr6[50]) * 1000 + twos_complement(partArr6[51]) * 0.1)),
            "AccumulatedLoadPower": "{:.2f}".format(float (twos_complement(partArr6[52]) * 1000 + twos_complement(partArr6[53]) * 0.1)),
            "AccumulatedSelf_usePower": "{:.2f}".format(float (twos_complement(partArr6[54]) * 1000 + twos_complement(partArr6[55]) * 0.1)),
            "AccumulatedPV_sellPower": "{:.2f}".format(float (twos_complement(partArr6[56]) * 1000 + twos_complement(partArr6[57]) * 0.1)),
            "AccumulatedGrid_chargerPower": "{:.2f}".format(float (twos_complement(partArr6[58]) * 1000 + twos_complement(partArr6[59]) * 0.1)),
            #"InverterErrorMessage": Rs485ComServer.Operator.AnalyBitMessage(partArr6[60], Rs485Parse.InverterError1) + Rs485ComServer.Operator.AnalyBitMessage(partArr6[61], Rs485Parse.InverterError2),
            #"InverterWarningMessage": Rs485ComServer.Operator.AnalyBitMessage(partArr6[64], Rs485Parse.InverterWarning),
            "SerialNumber": (partArr6[68] + partArr6[69]),
            #"SerialNumber": (twos_complement(partArr6[68]) * 65536 + twos_complement(partArr6[69])),
            "HardwareVersion": to_version(partArr6[70]),
            "SoftwareVersion": to_version(partArr6[71]),
            "BattPower": twos_complement(partArr6[72]),
            "BattCurrent": twos_complement(partArr6[73]),
            "BattVoltageGrade": twos_complement(partArr6[74]),
            "RatedPowerW": twos_complement(partArr6[76]),
            "CommunicationProtocolEdition": to_version(partArr6[77]),
            "ArrowFlag": twos_complement(partArr6[78])
        }

        return json.dumps(result, indent=4)
    else:
        return None

def convert_partArr5_to_json(partArr5):
    if partArr5 is not None and len(partArr5) == 44:
        result = {
            "InverterOffgridWorkEnable": twos_complement(partArr5[0]),
            "InverterOutputVoltageSet": float (twos_complement(partArr5[1]) * 0.1),
            "InverterOutputFrequencySet": float (twos_complement(partArr5[2])),
            "InverterSearchModeEnable": twos_complement(partArr5[3]),
            "InverterDischargerToGridEnable": twos_complement(partArr5[7]),
            "EnergyUseMode": twos_complement(partArr5[8]),
            "GridProtectStandard": twos_complement(partArr5[10]),
            "SolarUseAim": twos_complement(partArr5[11]),
            "InverterMaxDischargerCurrent": "{:.2f}".format(float (twos_complement(partArr5[12]) * 0.1)),
            "NormalVoltagePoint": "{:.2f}".format(float (twos_complement(partArr5[17]) * 0.1)),
            "StartSellVoltagePoint": "{:.2f}".format(float (twos_complement(partArr5[18]) * 0.1)),
            "GridMaxChargerCurrentSet": "{:.2f}".format(float (twos_complement(partArr5[24]) * 0.1)),
            "InverterBatteryLowVoltage": "{:.2f}".format(float (twos_complement(partArr5[26]) * 0.1)),
            "InverterBatteryHighVoltage": "{:.2f}".format(float (twos_complement(partArr5[27]) * 0.1)),
            "MaxCombineChargerCurrent": "{:.2f}".format(float (twos_complement(partArr5[31]) * 0.1)),
            "SystemSetting": partArr5[41],
            "ChargerSourcePriority": twos_complement(partArr5[42]),
            "SolarPowerBalance": twos_complement(partArr5[43])
        }
        return json.dumps(result, indent=4)
    else:
        return None
