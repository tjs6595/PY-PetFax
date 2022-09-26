from flask import ( Blueprint, render_template )
import json

pets = json.load(open('pets.json'))
print(pets)

bp = Blueprint('pet', __name__, url_prefix="/pets")

#Pets Index Route
@bp.route('/')
def index():
    return render_template('pets/index.html', pets=pets)
    
#Pets Show Route
@bp.route('/<int:id>')
def show(id):
    pet = pets[id-1]
    return render_template('pets/show.html', pet=pet)