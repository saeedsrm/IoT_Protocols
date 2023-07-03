
from time import sleep
import requests
import random
import json
# dashoboard link
# http://iot.sensifai.com:9090/dashboard/a68e93e0-8c44-11ed-ab34-194fa8ffdeff?publicId=e125ce10-927a-11ed-9ada-194fa8ffdeff




def send_request_to_iot_panel():
    url = "http://iot.sensifai.com:9090/api/v1/TAO37FyHZEIagFeh1Hb5/telemetry"
    data = {
        "pressure": random.randrange(800, 1200, 1),
        "acceleration_angular":random.randrange(0, 10, 1),
        "acceleration_linear":random.randrange(0, 10, 1),
        "speed": random.randrange(0, 10, 1),
        "outside_temp": random.randrange(0, 50, 1),
        "inside_temp": random.randrange(0, 80, 1),
        "sunlight_infrared": random.randrange(20, 50, 1),
        "sunlight_spectrum": random.randrange(20, 50, 1),
        "sunlight_visible": random.randrange(20, 50, 1),
        "humidity": random.randrange(0, 100, 1),
        "height": random.randrange(0, 300, 1),
        # "img_path": "http://secure-iot.ir/cansat/1.jpg",
        "image_text": random.randrange(20, 50, 1)
    }
    payload = json.dumps(data)
    headers = {
        'Content-Type': 'application/json'
    }
    requests.request("POST", url, headers=headers, data=payload)
    print('data sent to server')
        # try:
        #     requests.request("POST", url, headers=headers, data=payload)
        #     print('data sent to server')
        # except:
        #     print('some error in sending data to server')


while True:
    send_request_to_iot_panel()
    sleep(1)