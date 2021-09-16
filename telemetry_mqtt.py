from mqtt_func import get_client,send_mqtt
from metrics import get_metrics
import time,socket

hostname = socket.gethostname()
deviceId = hostname + str(int(time.time()))
client = get_client()
node = "EXT"
interval = 60
host_device = "mailbuns"

try:
    while True:
        mem_usage,cpu_temp,cpu_freq,cpu_usage,mem_total,mem_pct,disk_usage = get_metrics()
        payload = host_device + "/" + str(mem_usage) + ";" + str(cpu_temp) + ";" + str(cpu_freq) + ";" + str(cpu_usage) + ";"
        payload+= str(mem_total) + ";" + str(mem_pct) + ";" + str(disk_usage) + "/" + str(time.time())
        send_mqtt(client,"iot",payload)
        time.sleep(60)
except KeyboardInterrupt:
    client.disconnect()

    

