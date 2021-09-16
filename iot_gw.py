from mqtt_func import get_client,send_mqtt
import time

client = get_client()
client.loop_forever()
