from flask_restx import Namespace, Resource, fields
from app.services.facade import HBnBFacade

api = Namespace('amenities', description='Amenity operations')

# Define the amenity model for input validation and documentation
amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='Name of the amenity')
})

facade = HBnBFacade()

# TESTING - POST
# curl -X POST http://localhost:5000/api/v1/amenities/ \
# -H "Content-Type: application/json" \
# -d '{"name": "Pool"}'
# or
# curl -X POST http://localhost:5000/api/v1/amenities/ -H "Content-Type: application/json" -d '{"name": "Pool"}'

# TESTING - GET
# curl -X GET http://localhost:5000/api/v1/amenities/<amenity_id>

# TESTING - PUT(UPDATE)
# curl -X PUT http://localhost:5000/api/v1/amenities/<amenity_id> -H "Content-Type: application/json" -d '{"name": "Wifi"}'

@api.route('/')
class AmenityList(Resource):
    @api.expect(amenity_model)
    @api.response(201, 'Amenity successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        amenity_data = api.payload
        existing_amenity = facade.get_amenity_by_name(amenity_data['name'])
        if existing_amenity:
            return {'error': 'Amenity already exists'}, 400

        new_amenity = facade.create_amenity(amenity_data)
        return {'id': new_amenity.id, 'name': new_amenity.name}, 201

    @api.response(200, 'List of amenities retrieved successfully')
    @api.response(404, 'Amenites not found')
    def get(self):
        amenities = facade.get_all_amenities()
        if not amenities:
            return {'error': 'Amenities not found'}, 404
        return [{'id': amenity.id, 'name': amenity.name} for amenity in amenities], 200

@api.route('/<amenity_id>')
class AmenityResource(Resource):
    @api.response(200, 'Amenity retrieved successfully')
    @api.response(404, 'Amenity not found')
    # GET method
    def get(self, amenity_id):
        amenity = facade.get_amenity(amenity_id)
        if amenity is None:
            return {'error': 'Amenity not found'}, 404
        return {'id': amenity.id, 'name': amenity.name}, 200

    # PUT method
    @api.expect(amenity_model)
    @api.response(200, 'Amenity updated successfully')
    @api.response(404, 'Amenity not found')
    @api.response(400, 'Invalid input data')
    def put(self, amenity_id):
        """Update an amenity's information"""
        amenity_data = api.payload
        existing_amenity = facade.get_amenity(amenity_id)
        if not existing_amenity:
            return {'error': 'Amenity not found'}, 404

        updated_amenity = facade.update_amenity(amenity_id, amenity_data)
        return {'id': updated_amenity.id, 'name': updated_amenity.name}, 200