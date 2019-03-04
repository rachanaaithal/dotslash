import pyrebase

config = {
        "apiKey": " AIzaSyAo1tFyg-y8BfMdpEca4YJ3n0U_s_2R4-I ",
        "authDomain": "dotslash-e3ae8.firebaseapp.com",
        "databaseURL": "https://dotslash-e3ae8.firebaseio.com/",
        "storageBucket": "dotslash-e3ae8.appspot.com",
        "serviceAccount": "./dotslash-e3ae8-firebase-adminsdk-j0mxa-36fc653cc0.json"
        }

firebase = pyrebase.initialize_app(config)
'''

db = firebase.database()

def put_request_data(tag,data):

	db.child(tag).push(data)


def get_request_data(data):

	queries = db.child(data).get()

	return queries

queries = get_request_data("queries")

print(queries.val())
'''