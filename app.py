import os
from flask import Flask
from database import db
from routes import routes

app = Flask(__name__)

# =========================
# DATABASE (SQLite)
# =========================
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
instance_path = os.path.join(BASE_DIR, "instance")
os.makedirs(instance_path, exist_ok=True)

db_path = os.path.join(instance_path, "fitness.db")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + db_path
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# Register routes
app.register_blueprint(routes)


def init_db():
    with app.app_context():
        db.create_all()
        print("DB created")


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=True)