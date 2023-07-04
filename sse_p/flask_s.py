
from flask import Flask
from requests import Response
app = Flask(__name__)

@app.route("/stream")
def stream():
    def event_stream():
        message_to_send='test'
        while True:
            if message_to_send:
                yield "data: {}\n\n".format(message_to_send)
    
    return Response(event_stream(), mimetype="text/event-stream")