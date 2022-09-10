from crypt import methods
from flask import request, jsonify
from app import app, mongo, auth, tokens

@auth.verify_token
def verify_token(token):
    if token in tokens:
        return tokens[token]

@app.route("/createUser", methods=["POST"])
@auth.login_required
def create_user():
    userData = request.json
    result = mongo.flask.Users.insert_one(userData)
    return jsonify({"status":"success", "message": "user data saved successfully"}), 200
