#!/bin/bash
if ! screen -list | grep -q "mqtt_device"; then
    screen -dmS mqtt_device python telemetry_mqtt.py
fi


