#!flask/bin/python
from flask import Flask, jsonify, abort, make_response

app = Flask(__name__)

suits = [
	{
		'id': 1,
		'name': 'Mark I',
		'description': 'This is a description of the Mark I suit'
	},
	{
		'id': 2,
		'name': 'Mark II',
		'description': 'This is a description of the Mark II suit'

	}
]



@app.route('/')
def index():
	return "Iron Man Armor Database"

#@app.route('/armor/api/v1.0/suits', methods = ['GET'])
#def get_suits():
#	return jsonify( {'suits': suits})

@app.route('/armor/api/v1.0/suits/<int:suit_id>', methods = ['GET'])
def get_suits(suit_id):
	suit = filter(lambda t: t['id'] == suit_id, suits)
	if len(suit) == 0:
		abort(404)
	return jsonify( { 'suit': suit[0] } )

@app.errorhandler(404)
def not_found(error):
	return make_response('This is not the page you are looking for', 404)

if __name__ == '__main__':
	app.run(debug = True)
