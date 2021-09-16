from mqtt_func import get_client,send_mqtt
import time

deviceId = "elijah" + str(int(time.time()))
#client = get_client(deviceId)
client = get_client()
node = "EXT"

client.loop_forever()
