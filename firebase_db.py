from init_firebase import firebase
import json

db = firebase.database()

def put_request_data(tag,data):

	if tag and data:
		db.child(tag).push(data)
	

def get_request_data(tag):

	if tag:
		queries = db.child(tag).get()
		return queries

def update_data(id_tag,tag,data):

	queries = get_request_data(tag).val()
	response = {}

	for k,v in queries.items():
		if k == id_tag:
			response[k] = v
			break

	if response:
		response[k]['response'] = data
		db.child(tag).update(response)
	else:
		return None


tag = "queries"

id_tag = "-L_6L3Op4SXqvdt2TCAl"

data = "This is nice"

#json_dict = json.dumps(data)

update_data(id_tag,tag,data)


'''
queries = get_request_data("queries")

data = queries.val()

for v in data.items():
	#print("Key is {}".format(k))
	print("Value is {}".format(v))
'''