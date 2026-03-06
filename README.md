# Práctica 1: Captura y visualización de datos MQTT
##Sistemas operativos: **Proyecto Bash y Python**

---

## Descripción:
Este repositorio contiene una práctica de sistemas operativos desarrollada con **Bash y Python**.  
El objetivo de este proyecto es automatizar la captura, el almacenamiento y la visualización de datos de sensores ambientales recibidos de un broker **MQTT**.  
El suscriptor **QMTT** imprime los datos directamente en la terminal sin almacenarlos.

El proyecto resuelve el problema mediante:

- Captura automática de la salida del programa
- Almacenamiento de la salida en un archivo de registro
- Procesamiento de los datos del archivo de registro
- Extracción de la carga útil **JSON**
- Visualización de los datos como:
  - Gráfico PNG
  - Gráfico ACSII en la terminal

El programa utiliza conceptos de múltiples sistemas operativos, como:
- Gestión de procesos
- Monitoreo de procesos
- Terminación de procesos
- Procesamiento de registros
- Visualización de datos con **Python**
- Redirección de salida en **bash**

---

## 2. Estructura del repositorio

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

## 3. Requisitos del sistema
- Sistema operativo:  
Linux (probado en Ubuntu 22.04)
- Shell:  
Bash
- Python:  
Python 3

### Bibliotecas de Python necesarias  
- `matplotlib`  
- json (biblioteca estándar de Python)   

### Instalar la biblioteca necesaria:  
```in bash  
pip install matplotlib  
```

---

## 4. Temas de datos MQTT:
El sistema captura datos de los siguientes temas MQTT:  
`sensor/data/gas_sensor` y `sensor/data/sen55`  

Ejemplo de salida MQTT recibida del programa suscriptor:  
```
[MSG] Tema: sensor/data/sen55  
Carga útil: {"MassConcentrationPm1p0":0.70,"AmbientTemperature":21.17,...}  
```
El script de Bash captura esta salida y la almacena en un archivo de registro para su posterior procesamiento.  

---

## 5. Ejecución del proyecto
### 1. Otorgue permisos de ejecución al script de Bash  
```bash  
chmod +x capture_mqtt.sh  
```
### 2. Ejecute el script de captura  
```bash
./capture_mqtt.sh  
```
### 3. Ingrese el tiempo de captura (en segundos)  
Ejemplo:  
```
Ingrese el tiempo de captura (en segundos): 30  
```

---

## 6. Flujo de ejecución del programa
- El script bash ejecuta el programa suscriptor MQTT
- La salida del programa se dirige a `capture_mqtt.log`
- El script obtiene el PID del programa mediante `$!`
- El script comprueba continuamente si el programa sigue activo mediante `kill-0`
- Transcurrido el tiempo seleccionado, el script detiene el programa mediante:
   - `SIGINT`
   - `SIGTERM`
   - `SIGKILL` (si es necesario)
- El código Python se ejecuta automáticamente

---

## 7. Procesamiento de datos en Python
El script de Python:

- Lee el archivo `mqtt_capture.log`
- Extrae los datos de la carga útil JSON
- Analiza los valores del sensor
- Genera gráficos de los datos almacenados:
- Un gráfico PNG guardado en el directorio `/plots`
- Un gráfico ASCII mostrado directamente en la terminal

---

## 8. Ejemplo de salida:
Tras ejecutar el programa correctamente, se generan las siguientes salidas:  

- Un archivo de registro con los mensajes MQTT capturados  
```
mqtt_capture.log
```

- Gráficos generados en:  
```
plots/
```

- Un gráfico ASCII mostrado en la terminal  

---

## 9. Problemas comunes  

### No se encontró la biblioteca de Python  
Instalar la biblioteca requerida:  
```bash
pip install matplotlib
```

### Permiso denegado al ejecutar el script  

Otorgar permiso de ejecución:  
```bash
chmod +x capture_mqtt.sh
```

### El ejecutable MQTT no se está ejecutando  
Asegúrese de que el ejecutable del suscriptor MQTT se encuentre en el directorio del proyecto y tenga permiso de ejecución.  

---

## 10. Autores  
**Naela Khaldi** y **Zineb Hamman**   
Sistemas Operativos  
 Curso Académico 2025/2026  

---

## 11. Notas

El proyecto se desarrolló como parte de una práctica de Sistemas Operativos centrada en la automatización, el control de procesos y la visualización de datos.  




