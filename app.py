from flask import Flask, jsonify, request, render_template
from firebase_db import db, get_request_data, update_data
from firebase_storage import storage
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
	
	return render_template("base_generic.html")


@app.route("/requests",methods = ['GET'])
def get_requests():
	'''
	This function gets all the queries and returns them as a json object.
	'''
	if request.method == 'GET':
		data = get_request_data("queries").val()
		response = {}

		for k,v in data.items():
			key = k
			val = v
			response[key] = val

		if response:
			return jsonify(response), 201
		else:
			return jsonify({}), 401

	else:
		return jsonify({}), 405

@app.route("/send_string", methods = ['POST'])
def update_response():
	'''	
	This route updates the response string typed by the volunteer. 
	A json request with following structure:
	{
		"Id" : Key of the json object
		"Response string": Response string
	}
	'''
	if request.method == 'POST':
		try:
			id_tag = request.json['id']
			response_string = request.json['response']
		except KeyError:
			return jsonify({}),401

		tag = "queries"
		retval = update_data(id_tag, tag, response_string)

		return jsonify({}),201
	else:	
		return jsonify({}),405



if __name__ == "__main__":

	app.run(debug=True) 