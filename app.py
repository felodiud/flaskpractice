from flask import Flask, request, jsonify
from models import db, User
#instanceas aplicacion de flask

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)



print(__name__)
@app.route("/")
def home():
    return "hello world"

@app.route("/user", methods = ["POST"])
def create_user():
    user = User()
    data = request.get_json()
    user.name = data["name"]
    user.username = data["username"]
    user.password = data["password"]

    db.session.add(user)
    db.session.commit()

    return jsonify ({
        "mensaje" : "usuario guardado"
    }), 200


with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(host="localhost", port = 8000)