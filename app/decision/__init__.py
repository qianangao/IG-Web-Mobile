from flask import Blueprint
decision=Blueprint('decision',__name__)
from app.decision import routes
