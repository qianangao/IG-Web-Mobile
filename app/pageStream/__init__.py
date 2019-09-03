from flask import Blueprint
stream=Blueprint('pagestream',__name__)
from app.pageStream import routes