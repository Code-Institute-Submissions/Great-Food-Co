from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('sample.html')
   return render_template('signup_success.html')
if (__name__=='__main__'):
    app.secret_key='serecitivekey'
    app.run(debug=True)

