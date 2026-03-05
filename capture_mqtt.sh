#!/bin/bash

echo "Introduce el tiempo de captura en segundos:"
read CAPTURE_TIME

if [ -z "$CAPTURE_TIME" ]; then 
	CAPTURE_TIME=10
fi

LOG_FILE="mqtt_capture.log"

echo "[1/4] Ejecutando MQTT.."

./Ejecutables/mqtt_subscribe_emqx_linux > "$LOG_FILE" 2>&1 & 
PID=$!

echo " Proceso iniciado correctamnte con PID: $PID"

SECONDS_PASSED=0


while kill -0 $PID 2>/dev/null && [ $SECONDS_PASSED -lt $CAPTURE_TIME ]; do
	sleep 1
	SECONDS_PASSED=$((SECONDS_PASSED +1))
done
if kill -0 $PID 2>/dev/null; then
	echo "[2/4] Tiempo maximo alcanzado. finalizando proceso.."

	kill -SIGINT $PID
	sleep 2

	if kill -0 $PID 2>/dev/null; then
		echo "Enviando SIGTERM.."	
		kill -SIGTERM $PID
		sleep 2
	fi

	if kill -0 $PID 2>/dev/null; then
		echo "forzando cierre con SIGKILL"
		kill -SIGKILL $PID
	fi
fi

wait $PID 2>/dev/null
echo "[3/4] Ejecutando ejemplo python dentro de bash"  

python3 - <<'PY'
print("Hola mundo desde python ejecutado dentro de bash")
PY

echo "[4/4] Ejecutando analisis en Python.."
python3 plots_mqtt.py "$LOG_FILE"

echo "Proceso finalizado correctamente"
