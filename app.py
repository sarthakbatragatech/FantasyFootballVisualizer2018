from flask import Flask, render_template
from readData import readData
from flask import jsonify


app = Flask(__name__)

@app.route('/')
def QB():
    items = readData()
    message = {
        'status': 200,
        'message': 'OK',
        'data': items
    }
    resp = jsonify(message)
    resp.status_code = 200
    print(resp)
    return(resp)
    return render_template('index.html', your_list=items)

if __name__ == '__main__':
    app.run()
