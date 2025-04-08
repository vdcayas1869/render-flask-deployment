from flask import Flask
app = Flask(__name__)

@app.rout("/", methods=["GET"])
def home():
    return "<h1>Vhens Flask Website</h1>"

if __name__ == "__main__":
    app.run