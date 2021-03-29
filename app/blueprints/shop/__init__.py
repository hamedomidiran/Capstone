from flask import Blueprint

bp = Blueprint('shop', __name__, url_prefix='/shop', static_folder='./static', template_folder='./templates')

from .import views, models