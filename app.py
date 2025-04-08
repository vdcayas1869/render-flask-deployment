from flask import Flask, render_template
app = Flask(__name__)

@app.route("/home", methods=["POST"])
def home():
    return render_template('contact_form.html')

if __name__ == "__main__":
    app.run(debug == True)
