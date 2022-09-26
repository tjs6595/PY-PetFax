#Config
from flask import Flask

#Factory
def create_app():
    app = Flask(__name__)

    #Home Route
    @app.route('/')
    def hello():
        return 'Hello, PetFax from Factory.'

    #Register the PET blueprint.
    from . import pet
    app.register_blueprint(pet.bp)

    #Register the FACT blueprint.
    from . import fact
    app.register_blueprint(fact.bp)

    return app

