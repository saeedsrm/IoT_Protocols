import paho.mqtt.client as mqtt

#Setting
broker='127.0.0.1'
sub_topics=[('test/light',0),('test/door',1)]


#app
def disconnect():
    client.disconnect()
    p.terminate()
    print('--- I hope you always laugh! :)')
    exit()

def on_message(client,userdata,msg):
    msg=msg.payload.decode()
    if msg=='!':
        disconnect()
        return
    print(msg)


client=mqtt.Client()
client.connect(broker,1883,60)
client.on_message=on_message
client.subscribe(sub_topics)


print('ready to recevie from both topics: ')
client.loop_forever()
