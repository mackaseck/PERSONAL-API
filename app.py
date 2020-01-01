from flask import Flask, jsonify, request, Response
from settings import *
import json
from data_model import *


@app.route('/users')
def get_users():
	return jsonify({'Users': User.get_all_users()})


@app.route('/users/<email>')
def get_user(email):
	return_value = User.get_user(email)
	return jsonify(return_value)

def isvalid(user_object):
	if "first_name" in user_object and "last_name" in user_object and "DOB" in user_object and "city" in user_object and "email" in user_object:
		return True
	else:
		return False

@app.route('/users', methods=['POST'])
def add_user():
	request_data = request.get_json()
	if isvalid(request_data):
		User.add_user(request_data["first_name"], request_data["last_name"], request_data["DOB"], request_data["city"], request_data["email"])
		response = Response("", status=201)
		return response
	else:
		return Response("this is an invalid user", status = 400)


@app.route('/users/<email>', methods=['DELETE'])
def delete_user(email):
	User.delete(email)
	response = Response("",status=201)
	return response

@app.route('/users/<email>', methods=['PATCH'])
def update_city(email):
	request_data = request.get_json()
	User.update_user(email, request_data['city'])
	response = Response("", status=200)
	return response

@app.route('/users/<email>', methods=['PUT'])
def replace_user(email):
	request_data = request.get_json()
	User.replace_user(request_data['first_name'], request_data['last_name'], request_data['DOB'], request_data['city'], request_data['email'])
	response = Response("", status=201)
	return response









app.run(port=5000)
