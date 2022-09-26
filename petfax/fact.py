from flask import ( Blueprint, render_template )
import json

pets = json.load(open('pets.json'))

bp = Blueprint('fact', __name__, url_prefix="/facts")

#Facts Create Route
@bp.route('/new')
def new():
    return render_template('facts/new.html')
