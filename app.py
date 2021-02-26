# Author: Phaticusthiccy
# Telegram: t.me/phaticusthiccy

from flask import Flask, send_file, jsonify, request
import utility, carbon
from flask_cors import CORS
import asyncio
import os
import json

app = Flask(__name__)
app.secret_key = 'i_iz_noob'
loop = asyncio.get_event_loop()
CORS(app)


@app.route('/', methods=['GET', 'POST'])
def home():
    from flask import jsonify
    data = None
    if request.method == "POST":
        data = jsonify(**request.json)
        try:
            code = data['code']
        except KeyError:
            return jsonify({"error": "You need to write any code to generate carbon!"})
    else:
        code = request.args.get('code')
        if code is None:
            return jsonify({"error": "You need to write any code to generate carbon!"})
        data = request.args
    try:
        validatedBody = utility.validateBody(data)
        carbonURL = utility.createURLString(validatedBody)
        path = os.getcwd() + '/carbon_screenshot.png'
        loop.run_until_complete(carbon.get_response(carbonURL, path))
        return send_file(path, mimetype='image/png')
    except Exception as e:
        return jsonify({"error": e})


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000, use_reloader=True, threaded=True)
