from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://mydb.db"
db = SQLAlchemy(app)

from app.database import User


@app.route("/users")
def get_all_users():
    out = {
        "ok": True,
        "message": "Success"
    }
    out["users"] = User.query.all()
    return out


@app.route("/users", methods=["POST"])
def create_user():
    out = {
        "ok": True,
        "message": "Success"
    }
    user_data = request.json
    
    return out, 201


@app.route("/users/<int:uid>", methods=["DELETE"])
def delete_user(uid):
    out = {
        "ok": True,
        "message": "Success"
    }
    deactivate_user(uid)
    return out, 200
    

@app.route("/users/<int:uid>", methods=["GET"])
def get_single_user(uid):
    out = {
        "ok": True,
        "message": "Success"
    }
    out["body"] = select(uid)
    return out


@app.route('/agent')
def agent():
    user_agent = request.headers.get("User-Agent")
    return"<P>Your user agent is: %</p>" % user_agent
