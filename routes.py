from flask import Blueprint, render_template, request, jsonify
from database import db
from models import Client
from utils import PROGRAMS, calculate_bmi, get_bmi_category

routes = Blueprint('routes', __name__)


@routes.route("/")
def home():
    return render_template("AddClient.html", programs=PROGRAMS.keys())


@routes.route("/program", methods=["POST"])
def program_details():
    data = request.json

    program = data.get("program")
    weight = float(data.get("weight", 0))

    program_data = PROGRAMS.get(program)

    if not program_data:
        return jsonify({"error": "Invalid program"}), 400

    calories = int(weight * program_data["factor"])

    return jsonify({
        "workout": program_data["workout"],
        "diet": program_data["diet"],
        "color": program_data["color"],
        "calories": calories
    })


@routes.route("/save_client", methods=["POST"])
def save_client():
    try:
        data = request.form   
        client = Client.query.filter_by(name=data['name']).first()

        factor = PROGRAMS.get(data.get('program'), {}).get('factor', 0)
        weight = float(data.get('weight', 0))
        calories = int(weight * factor)

        if client:
            client.age = data.get('age')
            client.height = data.get('height')
            client.weight = weight
            client.program = data.get('program')
            client.calories = calories
        else:
            client = Client(
                name=data.get('name'),
                age=data.get('age'),
                height=data.get('height'),
                weight=weight,
                program=data.get('program'),
                calories=calories
            )
            db.session.add(client)

        db.session.commit()

        return jsonify({
            "status": "success",
            "message": "Client saved successfully"
        })

    except Exception as e:
        db.session.rollback()
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


@routes.route("/bmi/<name>")
def bmi(name):
    client = Client.query.filter_by(name=name).first_or_404()

    bmi = calculate_bmi(client)

    if not bmi:
        return jsonify({"error": "Missing height/weight"}), 400

    category, risk = get_bmi_category(bmi)

    return jsonify({
        "bmi": bmi,
        "category": category,
        "risk": risk
    })