import paho.mqtt.client as paho
import ssl

awshost = 'a338uorq6ck4b5.iot.us-east-1.amazonaws.com'
awsport = 8883
caPath = 'certs/ca.pem'
certPath = 'certs/6bd88989df-certificate.pem.crt'
keyPath = 'certs/6bd88989df-private.pem.key'


def on_connect(client, userdata, flags, rc):
    print('Connection returned result: ' + str(rc) )
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe('#' , 1 )

def on_message(client, userdata, msg):
    print('topic: '+msg.topic)
    print('payload: '+str(msg.payload))

mqttc = paho.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message
mqttc.tls_set(
    caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED,
    tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)
mqttc.connect(awshost, awsport, keepalive=60)
mqttc.loop_forever()
