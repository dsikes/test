from flask import Flask, request, jsonify
import json
import uuid

app = Flask(__name__)


@app.route('/event', methods=['POST'])
def services():
    """ write incoming post data to tmp file """
    
    with open('/events/event-%s.json' % (str(uuid.uuid4())), 'w+') as eventfile:
        json.dump(request.json, eventfile)
    
    return jsonify({"status": "ok"})


@app.route('/', methods=['GET'])
def status():
    """ status / healthcheck endpoint """
    return jsonify({"status": "available"})
