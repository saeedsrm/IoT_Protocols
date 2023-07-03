import paho.mqtt.client as mqtt

# from multiprocessing import Process
import threading


#Setting
broker='127.0.0.1'
sub_topic='test/light'
pub_topic='test/door'


#app
def disconnect():
    client.disconnect()
    p.terminate()
    print('--- I hope you always laugh! :)')
    exit()

def on_message(client,userdata,msg):
    msg=msg.payload.decode()
    print('received: ',msg)

def publish(msg):
    client.publish(pub_topic,msg)

def listen():
    client.loop_forever()


def run_listen():
    client.on_message=on_message
    client.subscribe(sub_topic)
    p.start()


client=mqtt.Client()
client.connect(broker,1883,60)


p = threading.Thread(target=listen)
# p=Process(target=listen)
run_listen()

print('ready to sub(light) and pub(door): ')

while True:
    msg=input()
    if msg=='~':
        break
    publish(msg)


disconnect()