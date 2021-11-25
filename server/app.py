from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/hello')
@cross_origin()
def hello_world():  # put application's code here
    return "Hello World!"


if __name__ == '__main__':
    app.run(debug=True)
