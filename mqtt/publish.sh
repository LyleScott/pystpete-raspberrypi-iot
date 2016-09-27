import paho.mqtt.client as mqtt

# https://pypi.python.org/pypi/paho-mqtt/1.1#callbacks

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))


# The callback that happens after a PUBLISH.
def on_publish(client, userdata, mid):
    print('published: ' + str(mid))


def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_publish = on_publish
    client.connect('broker.hivemq.com', 1883, 60)
    client.publish('PyStPete', 'Woohoo!')
    client.disconnect()


if __name__ == '__main__':
    main()
