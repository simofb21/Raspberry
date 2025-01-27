from flask import Flask, render_template, jsonify
import bluetooth
import csv
import os
import json  # Importa il modulo json
app = Flask(name)
CSV_FILE = 'bluetooth_scan_data.csv'
@app.route('/')
def index():
return "API per la scansione Bluetooth" # semplice testo per dire che la home funziona
@app.route('/scritturafile')
def scrittura_file():
try:
nearby_devices = bluetooth.discover_devices(lookup_names=True, duration=5)

    devices = [{"address": addr, "name": name} for addr, name in nearby_devices]

    with open(CSV_FILE, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.DictWriter(csvfile, fieldnames=["address","name"])
        csv_writer.writeheader()  # Scrive l'intestazione del CSV
        csv_writer.writerows(devices)  # Scrive i dati

    return jsonify({"status": "success", "message": "Dati salvati con successo nel file CSV."})

except Exception as e:
      return jsonify({"status": "error", "message": f"Errore durante la scrittura del file CSV: {str(e)}"}), 500


@app.route('/letturafile')
def lettura_file():
if not os.path.exists(CSV_FILE) or os.stat(CSV_FILE).st_size == 0:
return jsonify({"status": "error", "message": "File CSV non trovato o vuoto."}), 404

try:
    data = []
    with open(CSV_FILE, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            data.append(row)
    return jsonify({"status": "success", "data": data})
except Exception as e:
     return jsonify({"status": "error", "message": f"Errore durante la lettura del file CSV: {str(e)}"}), 500


@app.route('/json')
def json_devices():
try:
nearby_devices = bluetooth.discover_devices(lookup_names=True, duration=5)

    devices = [{"address": addr, "name": name} for addr, name in nearby_devices]
   
    return jsonify({"status": "success", "devices": devices})
except Exception as e:
    return jsonify({"status": "error", "message": f"Errore durante la scansione Bluetooth: {str(e)}"}), 500


if name == 'main':
app.run(host='0.0.0.0', port=5000, debug=True)