# Practica 1 – MQTT Data Capture and Visualization
##Operating Systems – Bash and Python Project

---

## Discription:
this repository contain a operating systems practice developped using **Bash y Python**
the objective of this project is to autaumate the capturing, storing and visualizing of enviromental sensor data recieved from an MQTT broker
the QMTT subscriber prints the data directly into the terminal without storing it

the project solves the problem by:

- Capturing the program output autumatically
- Storing the output in a log file
- Processing the data from the log file
- Extracts the **JSON** payload 
- Visualises the data as:
  - PNG graph
  - ACSII graph in the terminal

the program uses multiple Operating Systems concepts such as:
- Process manigment 
- Monitoring processes
- Process termination
- Log processing
- Data visualization with **Python**
- output redirection in **bash**

---

## 2. Repository structure

```
Practica_1_SO
│
├── Ejecutables/
├── plots/
├── scripts/
├── src/
├── capture_mqtt.sh
├── plots_mqtt.py
├── mqtt_capture.log
└── README.md
```

---

## 3. System Requirements
- Operating system: 
Linux (tested on Ubuntu 22.04)
- Shell :
Bash
- Python : 
Python 3

### Required Python libraries
-`matplotlib`
- json (standard Python library)

### Install required library:
```in bash
pip install matplotlib
```

---

## 4. MQTT Data Topics:
The system captures data from the following MQTT topics:
`sensor/data/gas_sensor` and `sensor/data/sen55`

Example MQTT output received from the subscriber program:
```
[MSG] Topic: sensor/data/sen55
Payload: {"MassConcentrationPm1p0":0.70,"AmbientTemperature":21.17,...}
```
The Bash script captures this output and stores it in a log file for later processing

---

## 5. Running the Project
### 1. Give execution permission to the Bash script
```bash
chmod +x capture_mqtt.sh
```
### 2. Run the capture script
```bash
./capture_mqtt.sh
```
### 3. Enter capture time (in seconds)
Example:
```
Enter capture time (seconds): 30
```

---

## 6. Program Execution Flow
- The bash script executes the MQTT subscriber program
- The programs output is directed to `capture_mqtt.log`
- The script get the programs PID using `$!`
- The script keeps checking if the program is still active using `kill-0`
- After the chosen time the script stopes the program using :
  - `SIGINT`
  - `SIGTERM`
  - `SIGKILL` (if necessary)
- the python code is executed automatically 

---

## 7.Python Data Processing
the Python script:

- Reads the `mqtt_capture.log` file
- Extracts the JSON payload data
- Parses sensor values
- Generates graphs of the stored data:
  - A PNG graph saved on `/plots` directory
  - An ASCII graph displayed directly in the terminal 

---

## 8. Example Output:
After running the program successfully, the following outputs are produced:

- A log file containing captured MQTT messages
```
mqtt_capture.log
```

- Generated graphs in:
```
plots/
```

- An ASCII graph displayed in the terminal

---

## 9. commen problems 
   
### Python library not found
Install required library:
```bash
pip install matplotlib
```

### Permission denied when running the script

Give execution permission:
```bash
chmod +x capture_mqtt.sh
```

### MQTT executable not running
Ensure the MQTT subscriber executable is located in the project directory and has execution permission

---

## 10. Authors
- **Naela Khaldi** y **Zineb Hamman**
- Operating Systems
- Academic Year 2025/2026

---

## 11. Notes

The project was developed as part of an Operating Systems practice assignment focusing on automation, process control, and data visualization.




