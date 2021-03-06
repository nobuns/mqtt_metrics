import paho.mqtt.client as mqtt
import time,ssl
import configparser

config = configparser.ConfigParser()
config.read_file(open(r'config.txt'))

url = config.get('mqtt','url')
username = str(config.get('mqtt','username'))
passwd = config.get('mqtt','passwd')
port = int(config.get('mqtt','port'))
deviceId = config.get('mqtt','deviceID') + str(int(time.time()))
topic = config.get('mqtt','topic')

def on_connect(client, userdata, flags, rc):
    print("Connected with result code: %s" % rc)
    client.subscribe(topic)


def on_publish(client, userdata, mid):
    print("Message {0} sent from {1}".format(str(mid), deviceId))

def on_log(client, userdata, level, buf):
    print("log: ",buf)
    pass

def on_disconnect(client, userdata,rc=0):
    print ("disconnected: " + str(rc))

def on_message(client, userdata, message):
    data = dict(
        topic=message.topic,
        payload=message.payload.decode(),
        timestamp = 0
    )
    print (data)
    return 1
    
def get_client():
    client = mqtt.Client(deviceId, mqtt.MQTTv311)
    if str(port)!="1883":
        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        client.tls_set_context(context)
    client.username_pw_set(username,passwd)
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_disconnect = on_disconnect
    client.on_log=on_log
    client.connect(url,port,30)
    client.loop_start()
    return client

def send_mqtt(client,topic,payload):
    client.publish(topic,payload)
