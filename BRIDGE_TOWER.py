import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# BRIDGE_TOWER.py



from flask import Flask, request, jsonify

from datetime import datetime

import json

import os



app = Flask(__name__)



EVENTS_FILE = "tower_events.json"



if not os.path.exists(EVENTS_FILE):
    pass

    with open(EVENTS_FILE, "w", encoding="utf-8") as f:
        pass

        json.dump([], f)



def load_events():
    pass

    with open(EVENTS_FILE, "r", encoding="utf-8") as f:
        pass

        return json.load(f)



def save_events(events):
    pass

    with open(EVENTS_FILE, "w", encoding="utf-8") as f:
        pass

        json.dump(events, f, indent=4, ensure_ascii=False)



@app.route("/")



def home():
    pass

    return jsonify({

        "status": "ONLINE",

        "tower": "ACTIVE",

        "bridge": "CONNECTED"

    })



@app.route("/new-event", methods=["POST"])



def new_event():
    pass



    data = request.json



    events = load_events()



    protocol = f"EVT-{len(events)+1:05d}"



    event = {

        "protocol": protocol,

        "timestamp": str(datetime.now()),

        "name": data.get("name"),

        "email": data.get("email"),

        "service": data.get("service"),

        "message": data.get("message"),

        "status": "RECEIVED"

    }



    events.append(event)



    save_events(events)



    print("\n================================================")

    print(" NEW EVENT RECEIVED ")

    print("================================================")

    print(f"PROTOCOL : {protocol}")

    print(f"NAME     : {event['name']}")

    print(f"EMAIL    : {event['email']}")

    print(f"SERVICE  : {event['service']}")

    print("================================================\n")



    return jsonify({

        "success": True,

        "protocol": protocol,

        "status": "RECEIVED"

    })



@app.route("/tower")



def tower():
    pass



    events = load_events()



    return jsonify(events)



if __name__ == "__main__":
    pass



    app.run(

        host="0.0.0.0",

        port=3000,

        debug=True

    )




