from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p> <a href='https://fb-bike.it'>Clicca qui</a>"

if __name__ == "__main__":
    app.run()
