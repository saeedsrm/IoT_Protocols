import paho.mqtt.client as mqtt
# mosquitto broker

# setting
# broker="broker.hivemq.com"
broker='127.0.0.1'
sub_topic='test/light'




def disconnect():
    client.disconnect()
    print("--- I hope you alwase laugh! :)")
    exit()

def on_message(client, userdata , msg):
    msg=msg.payload.decode()
    if msg=="!":
        disconnect()
        return
    print(msg) 



#app
client =mqtt.Client()
client.connect(broker,1883,60)
client.on_message=on_message

client.subscribe(sub_topic)


print("ready to receive from light: ")

client.loop_forever() # or: loop_start() , loop_stop()