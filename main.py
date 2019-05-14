# Lenguaje - Python 3
# Librerias - Flask - flask_cors
# Para ejecutar la app se usa el comando FLASK_APP=main.py flask run

from flask import Flask
from flask import json
from flask_cors import CORS
import random
import datetime

app = Flask(__name__)
CORS(app)

randomNumber = random.randrange(1, 9999)

data = {
    "processId": randomNumber,
    "dateTime": datetime.datetime.now(),
    "responseType": "JSON"
}


@app.route('/pid')
def pid():
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')