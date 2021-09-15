from mqtt_func import get_client,send_mqtt
import time

deviceId = "elijah" + str(int(time.time()))
client = get_client()
node = "EXT"

send_mqtt(client,"iot","payload")
time.sleep(3)
client.disconnect()
