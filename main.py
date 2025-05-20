import paho.mqtt.client as mqtt
import time

BROKER = "localhost"
PORT = 1883
SUBSCRIBE_TOPIC = "sensor/movement"
PUBLISH_TOPIC = "sensor/movement/processed"
USERNAME = "lfitz"
PASSWORD = "LukPw"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Verbindung hergestellt")
        client.subscribe(SUBSCRIBE_TOPIC)
    else:
        print("Verbindung fehlgeschlagen")

def on_connect2(client, userdata, flags, rc):
            if rc == 0:
                print("Verbindung hergestellt")
                client.subscribe(SUBSCRIBE_TOPIC)
            else:
                print("Verbindung fehlgeschlagen")




def on_message(client, userdata, msg):
    print({msg.payload.decode()})
    client.publish(PUBLISH_TOPIC, msg.payload.decode())

def on_log(client, userdata, level, buf):
    print(f"Log: {buf}")

client = mqtt.Client()
client.username_pw_set(USERNAME, PASSWORD)
client.on_connect = on_connect
client.on_message = on_message
client.on_log = on_log

connected = False
while not connected:
    try:
        client.connect(BROKER, PORT, 60)
        connected = True
    except Exception as e:
        print(f"Fehler beim Verbinden: {e}")
        time.sleep(5)

client.loop_forever()