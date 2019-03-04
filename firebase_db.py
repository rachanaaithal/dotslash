from init_firebase import firebase

db = firebase.database()

def put_request_data(tag,data):

	db.child(tag).push(data)

def get_request_data(data):

	queries = db.child(data).get()

	return queries

'''
queries = get_request_data("queries")

data = queries.val()

for v in data.items():
	#print("Key is {}".format(k))
	print("Value is {}".format(v))
'''