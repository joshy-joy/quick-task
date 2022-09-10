from crypt import methods
from flask import request, jsonify
from app import app, mongo

@app.route("/createUser", methods=["POST"])
def create_user():
    userData = request.json
    result = mongo.flask.Users.insert_one(userData)
    return jsonify({"status":"success", "message": "user data saved successfully"}), 200
