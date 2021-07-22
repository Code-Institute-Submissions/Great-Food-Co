from flask import Flask, render_template

app = flask(__name__)


@app.route("/")
def index():
    return render_template('sample.html')

if (__name__=='__main__'):
    app.secret_key='serecitivekey'
    app.run(debug=True)

