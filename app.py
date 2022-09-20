import logging
import os

from flask import Flask, Blueprint
from flask_restx import Api

from controller.user import user_namespace

app = Flask(__name__)


def setup_logging() -> None:
    pass


def initialize_app(flask_app: Flask) -> None:
    api = Api(version='1.0', title='User Management Service',
              description='REST endpoints for user management service')

    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(flask_app)
    api.add_namespace(user_namespace)
    flask_app.register_blueprint(blueprint)


def main() -> None:
    initialize_app(app)
    logging.info('>>>>> Starting development server on port {} <<<<<'.format(os.environ.get('PORT')))
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT'))


if __name__ == "__main__":
    main()
