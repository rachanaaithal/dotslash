from flask import Flask, jsonify, request, render_template
from firebase_db import db, get_request_data
from firebase_storage import storage
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
	
	return render_template("base_generic.html")


@app.route("/requests",methods = ['GET'])
def get_requests():

	if request.method == 'GET':
		data = get_request_data("queries").val()
		response = {}

		for k,v in data.items():
			key = k
			val = v
			response[key] = val
		print(response)
		response=[{'id':key, 'url':response[key]['url'], 'question': response[key]['question']} for key in response]
		print(response)
		return jsonify(response), 201

	else:
		return jsonify({}), 405



if __name__ == "__main__":
	app.run(debug=True) 