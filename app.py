from flask import Flask, render_template
from readData import readData

app = Flask(__name__)

@app.route('/')
def hello():
    items = readData()
    return render_template('index.html', your_list=items)

if __name__ == '__main__':
    app.run()
