from mqtt_func import get_client,send_mqtt
from metrics import get_metrics
import time,socket
import configparser

hostname = socket.gethostname()
deviceId = hostname + str(int(time.time()))
client = get_client()


config = configparser.ConfigParser()
config.read_file(open(r'config.txt'))

interval = int(config.get('mqtt','interval'))
host_device = config.get('mqtt','deviceID')


mem_usage,cpu_temp,cpu_freq,cpu_usage,mem_total,mem_pct,disk_usage,gpu_util,gpu_temp,gpu_power = get_metrics()
payload = host_device + "/" + str(mem_usage) + ";" + str(cpu_temp) + ";" + str(cpu_freq) + ";" + str(cpu_usage) + ";"
payload+= str(mem_total) + ";" + str(mem_pct) + ";" + str(disk_usage) + ";" + str(gpu_util) + ";" + str(gpu_temp)
payload+= ";" + str(gpu_power) + "/" + str(time.time())
send_mqtt(client,"iot",payload)
time.sleep(1)
client.disconnect()

    

