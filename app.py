from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def student():
   return render_template('contact_form.html')

@app.route('/confirmation',methods = ['POST', 'GET'])
def confirmation():
   if request.method == 'POST':
      confirmation = request.form
      return render_template("confirmation.html",confirmation = confirmation)

if __name__ == '__main__':
   app.run(debug = True)
