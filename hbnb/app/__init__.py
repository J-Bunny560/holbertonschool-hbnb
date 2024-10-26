from flask import Flask
from flask_restx import Api
from .api.v1.users import ns as users_ns  # Ensure these modules exist
from .api.v1.amenities import api as amenities_api
import logging

# Function to set up logging
def setup_logging():
    if not logging.getLogger().hasHandlers():  # Check if logging is already set up
        logging.basicConfig(level=logging.INFO)

def create_app():
    setup_logging()  # Call the logging setup once
    app = Flask(__name__)
    app.config['DEBUG'] = True  # Ensure to set this to False in production
    api = Api(app, version='1.0', title='HBnB API', description='HBnB Application API', doc='/api/v1/')

    # Define base path
    base_path = '/api/v1'

    # Check if namespaces are defined before adding them
    if users_ns:
        api.add_namespace(users_ns, path=f'{base_path}/users')
    else:
        logging.warning("users_ns is not defined")

    if amenities_api:
        api.add_namespace(amenities_api, path=f'{base_path}/amenities')
    else:
        logging.warning("amenities_api is not defined")

    return app

if __name__ == '__main__':
    app = create_app()  # Simple app runner
    app.run(debug=True)  # Set debug to True for development only
