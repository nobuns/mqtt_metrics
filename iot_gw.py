import configparser
import paho.mqtt.client as mqtt
import time,ssl

config = configparser.ConfigParser()
config.read_file(open(r'config.txt'))

url = config.get('mqtt','url')
username = config.get('mqtt','username')
passwd = config.get('mqtt','passwd')
port = int(config.get('mqtt','port'))
device_client = config.get('mqtt','deviceID')
topic = config.get('mqtt','topic')

#cafile = config.get('mqtt','cafile')

def on_connect(client, userdata, flags, rc):
    print("Connected with result code: %s" % rc)
    client.subscribe(topic)


def on_publish(client, userdata, mid):
    print("Message {0} sent from {1}".format(str(mid), deviceId))

def on_message(client, userdata, message):
    data = dict(
        topic=message.topic,
        payload=message.payload.decode(),
        timestamp = 0
    )
    print (data)
    
def on_log(client, userdata, level, buf):
    print("log: ",buf)
    pass

def on_disconnect(client, userdata,rc=0):
    print ("disconnected: " + str(rc))

client = mqtt.Client(device_client + str(time.time())) #, clean_session=False)
client.username_pw_set(username,passwd)
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect
client.on_log=on_log
#client.tls_set("/scripts/mqttgw/ca.crt",tls_version=2)
#client.tls_set(tls_version=2)
if port!=1883:
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    client.tls_set_context(context)
client.connect(url,port)
client.loop_forever()

