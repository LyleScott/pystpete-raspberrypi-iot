import json
import paho.mqtt.client as paho
import random
import ssl
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

# MQTT Client setup
mqttc = paho.Client()
mqttc.on_connect = on_connect
mqttc.tls_set(
    caPath, certfile=certPath, keyfile=keyPath,
    cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2,
    ciphers=None)
mqttc.connect(awshost, awsport, keepalive=60)
mqttc.loop_start()

while True:
    sleep(0.5)
    if is_connected == True:
        temperature = round(random.uniform(10.0, 100.0), 3)

        print('Setting "desired" state to temperature={}'.format(temperature))
        data = json.dumps({
            'state': {
                'desired': {
                    'temperature': temperature,
                },
            }
        })
        mqttc.publish('$aws/things/AThing/shadow/update', data, qos=1)
        print('msg sent: temperature %s' % data)

        print('Device should now have a "desired" state out of sync with the '
              '"reported" state.')

        sleep(10)

        data = json.dumps({
            'state': {
                'reported': {
                    'temperature': temperature,
                }
            }
        })
        mqttc.publish('$aws/things/AThing/shadow/update', data, qos=1)

        print('Device should be "in sync" state now that reported == desired.')

        sleep(10)
        break
    else:
        print('waiting for connection...')
