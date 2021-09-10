from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')
@app.route("/aflah")
def aflah():
    name2 = 'foobar'
    return render_template('about.html', name=name2)
app.run(debug=True)