# Must Inverter Data Handler

MustInverterDataHandler is Python application designed for interacting with Must Inverter PH1800 devices, enabling the retrieval of solar inverter data in JSON format. This script could work also on other similar inverter, I own just the PH1800 so feel free to try, nothing is going to explode, maybe...

## Features

- **Data Retrieval**: Must Inverter Data Handler allows you to effortlessly retrieve real-time data from your Must Inverter PH1800, including information on power generation, battery status, grid connectivity, and more. It provides this data in a structured JSON format for easy integration into other systems.

- **Command Configuration**: Must Inverter Data Handler offers flexibility through command configuration. You can enable or disable specific data retrieval commands, optimizing performance and focusing on the data you need most.

- **Data Writing (Future Expansion)**: While Must Inverter Data Handler excels at data retrieval, it's designed with future expansion in mind. It offers the flexibility to write data back to the inverter or other connected devices, enabling you to control and manage your solar power system remotely.

- **Open Source**: Must Inverter Data Handler is open source and hosted on GitHub, allowing the community to contribute, customize, and extend its functionality. Feel free to adapt it to your specific needs.

## Getting Started

### Prerequisites

- Python 3.x
- pip (Python package manager)
- Serial library

### Installation

1. Clone the repository:

- `git clone https://github.com/thelabexpedition67/MustInverterDataHandler.git`
- `cd MustInverterDataHandler`

2. Install the required Python packages:

- `pip install -r requirements.txt`

### Configuration

1. Configure the serial port and command strings in the `main.py` script.

- `serial_port`: Specify the path to the serial port where your Must Inverter PH1800 is connected.
- `command_config`: Enable or disable specific data retrieval commands based on your requirements.

### Usage

Run the application:

- `python main.py`

### Output Example

```
{
    "ChargerWorkstate": 2,
    "MpptState": 2,
    "ChargingState": 1,
    "PvVoltage": "78.00",
    "BatteryVoltage": "26.90",
    "ChargerCurrent": "20.20",
    "ChargerPower": 539,
    "RadiatorTemperature": 35,
    "ExternalTemperature": 0,
    "BatteryRelay": 1,
    "PvRelay": 1,
    "ErrorMessage": 0,
    "WarningMessage": 0,
    "BattVolGrade": 24,
    "RatedCurrent": "60.00",
    "AccumulatedPower": "100.70",
    "AccumulatedTime": "00:00:00",
    "WorkState": 2,
    "AcVoltageGrade": 230,
    "RatedPower": 3000,
    "InverterBatteryVoltage": "27.30",
    "InverterVoltage": 229.9,
    "GridVoltage": "234.70",
    "BusVoltage": "423.20",
    "ControlCurrent": "1.70",
    "InverterCurrent": "1.50",
    "GridCurrent": "0.00",
    "LoadCurrent": "1.50",
    "PInverter": 37,
    "PGrid": 0,
    "PLoad": 37,
    "LoadPercent": 1,
    "SInverter": 396,
    "SGrid": 0,
    "Sload": 352,
    "Qinverter": 394,
    "Qgrid": 0,
    "Qload": 394,
    "InverterFrequency": 50.0,
    "GridFrequency": "49.97",
    "InverterMaxNumber": "0000",
    "CombineType": "0000",
    "InverterNumber": "0000",
    "AcRadiatorTemperature": 31,
    "TransformerTemperature": 0,
    "DcRadiatorTemperature": 0,
    "InverterRelayState": 1,
    "GridRelayState": 0,
    "LoadRelayState": 1,
    "N_LineRelayState": 0,
    "DCRelayState": 1,
    "EarthRelayState": 0,
    "AccumulatedChargerPower": "0.20",
    "AccumulatedDischargerPower": "51.40",
    "AccumulatedBuyPower": "0.00",
    "AccumulatedSellPower": "0.00",
    "AccumulatedLoadPower": "53.00",
    "AccumulatedSelf_usePower": "51.20",
    "AccumulatedPV_sellPower": "0.00",
    "AccumulatedGrid_chargerPower": "0.00",
    "BattPower": -449,
    "BattCurrent": -16
}
```

## License

This project is licensed under the MIT License

## Acknowledgments

- pySerial - Python serial library for serial communication.

- I would like to extend my gratitude to the creators of the [Console Dumper for Must Power PH1800 Inverters](https://github.com/aquarat/must_inverter). Their project was needed on the development of this Python version. Below the reasons why I wanted to create this python version.

### Why this Python Version?

- **Faster Retrieval:** The Python version of the Must Inverter Data Handler offers significantly faster data retrieval, making it a great choice for applications where speed matters.

- **Easier Implementation:** Unlike the original C# project, which requires Mono on Linux, this Python version can be used without any additional dependencies, making it easier to set up and run on Linux systems.

I hope this Python implementation proves to be a valuable addition to the Must Inverter community.

## Contributing

Contributions are welcome! Feel free to open issues or pull requests to improve this project.
