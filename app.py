from flask import Flask, render_template
app = Flask(__name__)

@app.route("/", methods=["POST"])
def home():
    return render_template("<h1>Welcome to the USER contact Form</h1>")

if __name__ == "__main__":
    app.run(debug == True)
