from flask import Flask, jsonify
import bluetooth
import json  # Importa il modulo json

app = Flask(__name__)

@app.route('/')
def index():
    return "<p>API per la scansione Bluetooth</p>"

@app.route('/scan')
def scan():
    try:
        nearby_devices = bluetooth.discover_devices(lookup_names=True, duration=5)
        devices = []
        for addr, name in nearby_devices:
            devices.append({"address": addr, "name": name})

        return jsonify({"status": "success", "devices": devices})
    
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
