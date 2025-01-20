from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<p>Per eseguire il gioco migliore che c\'è <a href="https://fb-bike.it/game">clicca qua</a></p>'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
