import paho.mqtt.client as mqtt

def publish_to_mqtt(topic, message):
    client = mqtt.Client()
    client.connect("localhost", 1883)  # Connect to the broker
    client.publish(topic, message)
    client.disconnect()
