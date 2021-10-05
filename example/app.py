from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/loopindex')
def loopindex():
    items = ['a', 'b', 'c', 'd']
    return render_template('loopindex.html', items = items)

@app.route('/node')
def node():
    return render_template('node.html')

@app.route('/nodeimg')
def nodeimg():
    return render_template('nodeimg.html')


app.run()