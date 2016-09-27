import json
import paho.mqtt.client as paho
import random
import ssl
import sys
from time import sleep

# IMPORTANT: change these.
awshost = 'a338uorq6ck4b5.iot.us-east-1.amazonaws.com'
caPath = 'certs/ca.pem'
certPath = 'certs/6bd88989df-certificate.pem.crt'
keyPath = 'certs/6bd88989df-private.pem.key'
awsport = 8883


is_connected = False

def on_connect(client, userdata, flags, rc):
    """Fires when the connection is successfully made to the MQTT broker."""
    global is_connected
    is_connected = True
    print('Connection returned result: ' + str(rc) )

    try:
        arg = sys.argv[1]
    except IndexError:
        print('USAGE: {} text'.format(sys.argv[0]))
        sys.exit(1)

    print('Setting uscroll to {}'.format(arg))

    data = json.dumps({
        'state': {
            'desired': {
                'uscroll': arg,
            },
        }
    })
    client.publish('$aws/things/AThing/shadow/update', data, qos=1)
    print('message sent.')


def on_publish(*args, **kwargs):
    sys.exit()


# MQTT Client setup
mqttc = paho.Client()
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.tls_set(
    caPath, certfile=certPath, keyfile=keyPath,
    cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2,
    ciphers=None)
mqttc.connect(awshost, awsport, keepalive=60)
mqttc.loop_forever()
