import json
import requests
from os import environ
from query_api import query_api_func
from flask import Flask, make_response, jsonify, escape, request, json

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/<path:subpath>', methods=['GET'])
def searchpanel(subpath):
    request_args = request.args.to_dict()
    if not request_args:
        json_response = escape(subpath)
    else:
        print("Quering the API.....")
        request_query_response = query_api_func(environ['API_DOMAIN'], request_args)
        json_response = app.response_class(response=json.dumps(request_query_response),mimetype='application/json')
        
    return json_response

if __name__ == '__main__':
    app.run(debug=environ['FLASK_DEBUG'], port=environ['FLASK_RUN_PORT'])