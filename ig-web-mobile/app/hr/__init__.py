from flask import Blueprint
hr=Blueprint('hr',__name__)
from app.hr import routes
