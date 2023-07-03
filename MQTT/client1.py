import paho.mqtt.client as mqtt
# mosquitto broker

# setting
# broker="broker.hivemq.com"
broker='127.0.0.1'
pub_topic='test/light'

#app
client =mqtt.Client()
client.connect(broker,1883,60)

def publish(msg):
    client.publish(pub_topic,msg)


print('ready to pub(light): ')

while True:
    msg=input()
    if msg=='~':
        break
    publish(msg)

print('--- publishing Ended')
client.disconnect()