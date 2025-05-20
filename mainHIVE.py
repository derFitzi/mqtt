import paho.mqtt.client as mqtt
import time

BROKER = "03027efd654c4d958f11112b6f287ce1.s1.eu.hivemq.cloud"
PORT = 8883
SUBSCRIBE_TOPIC = "sensor/movement"
PUBLISH_TOPIC = "sensor/movement/processed"
USERNAME = "lfitz"
PASSWORD = "LukPw1LukPw"  # Passwort für Hive anderes nur LukPw

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Verbindung hergestellt")
        client.subscribe(SUBSCRIBE_TOPIC)
    else:
        print(f"Verbindung fehlgeschlagen, Fehlercode: {rc}")

def on_message(client, userdata, msg):
    print({msg.payload.decode()})
    client.publish(PUBLISH_TOPIC, msg.payload.decode())

def on_log(client, userdata, level, buf):
    print(f"Log: {buf}")

client = mqtt.Client(client_id="unique_client_id_123")
client.username_pw_set(USERNAME, PASSWORD)
client.tls_set()  # TLS aktivieren
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
