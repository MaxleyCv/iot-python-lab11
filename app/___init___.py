from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from flask_migrate import Migrate

from app.models.Arm import Arm
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class RestArm(Arm, db.Model):

    __tablename__ = 'flasksqlalchemy-tutorial-users'
    id = Column(Integer, primary_key=True)
    _count_in_stack = Column(Integer, unique=False)
    _country_of_origin = Column(String, unique=False)
    _serial_number = Column(String, unique=True)
    _operation_crew_count = Column(Integer, unique=False)

    def __init__(self, serial_number="AA11", country_of_origin="Ukraine", count_in_stack=1, operation_crew_count=1):
        super().__init__(serial_number, country_of_origin, count_in_stack, operation_crew_count)



