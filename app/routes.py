from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydb.db"
db = SQLAlchemy(app)

from app.database import User


@app.route("/")
def index():
    username = "Leo"
    return render_template("index.html", name=username)


@app.route("/greet/<username>")
def greeting(username):
    return render_template("index.html", name=username)


@app.route("/users/<int:uid>/profiles")
def get_profile(uid):
    user = User.query.filter_by(id=uid).first()
    return render_template("user_profile.html, users=user")

@app.route("/users/profiles")
def list_users():
    list_of_users = Users.query.all()
    return render_template("profile_list.html", users=list_of_users)


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
    db.session.add(
        User(
            first_name=user_data.get("first_name"),
            last_name=user_data.get("last_name"),
            hobbies=user_data.get("hobbies")
        )
    )
    
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


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404
