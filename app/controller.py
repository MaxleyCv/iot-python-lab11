from flask import Flask, jsonify, abort, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
import json
import copy

from models.Arm import Arm
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)


class RestArm(Arm, db.Model):
    id = Column(Integer, primary_key=True)
    _count_in_stack = Column(Integer, unique=False)
    _country_of_origin = Column(String, unique=False)
    _serial_number = Column(String, unique=True)
    _operation_crew_count = Column(Integer, unique=False)

    def __init__(self, serial_number="AA11", country_of_origin="Ukraine", count_in_stack=1, operation_crew_count=1):
        super().__init__(serial_number, country_of_origin, count_in_stack, operation_crew_count)


class RestArmScheme(ma.Schema):
    class Meta:
        fields = ('_count_in_stack', '_country_of_origin', '_serial_number', '_operation_crew_count')


arm_scheme = RestArmScheme()
arms_scheme = RestArmScheme(many=True)


@app.route("/arms", methods=["GET"])
def get_all_arms():
    arms = RestArm.query.all()
    return arms_scheme.jsonify(arms)


@app.route("/arm", methods=["POST"])
def add_arm():
    stack_count = request.json["count_in_stack"]
    origin = request.json["country_of_origin"]
    serial = request.json["serial_number"]
    crew = request.json["operation_crew_count"]
    arm = RestArm(serial, origin, stack_count, crew)
    db.session.add(arm)
    db.session.commit()
    return arm_scheme.jsonify(arm)


@app.route("/arms/<id>", methods=["GET"])
def get_arm(id):
    arm = RestArm.query.get(id)
    if not arm:
        abort(404)
    return arm_scheme.jsonify(arm)


@app.route("/arm/<id>", methods=["put"])
def upd_arm(id):
    arm1 = RestArm.query.get(id)
    if not arm1:
        abort(404)
    old_arm = copy.deepcopy(arm1)
    arm1._count_in_stack = request.json["count_in_stack"]
    arm1._country_of_origin = request.json["country_of_origin"]
    arm1._serial_number = request.json["serial_number"]
    arm1._operation_crew_count = request.json["operation_crew_count"]
    db.session.commit()
    return arm_scheme.jsonify(old_arm)


@app.route("/arm/<id>", methods=["DELETE"])
def delete_arm(id):
    arm = RestArm.query.get(id)
    if not arm:
        abort(404)
    db.session.delete(arm)
    db.session.commit()
    return arm_scheme.jsonify(arm)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)