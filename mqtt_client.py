# mqtt_client.py
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("localhost", 1883, 60)

def send_data(topic, message):
    client.publish(topic, message)
