from flask import Flask, render_template, jsonify
import bluetooth

app = Flask(__name__)

@app.route('/')
def index():
    return "<p>Hello, World!</p>"

@app.route('/scan')
def scan():
    devices = bluetooth.discover_devices(lookup_names=True, duration=5)
    return jsonify(devices)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
