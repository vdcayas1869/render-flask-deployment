from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route("/home", methods=['POST', 'GET'])
def home():
    return render_template("<h1>Welcome to the USER contact Form</h1>")

if __name__ == "__main__":
    app.run(debug == True)
