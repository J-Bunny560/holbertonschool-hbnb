from flask_restx import Namespace, Resource, fields
from ...services.facade import HBnBFacade
from ...models.amenity import Amenity
import logging

api = Namespace('amenities', description='Amenity operations')
facade = HBnBFacade()
logger = logging.getLogger(__name__)

amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='Amenity name')
})

@api.route('/')
class AmenityList(Resource):
    @api.expect(amenity_model)
    @api.response(201, 'Amenity successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new amenity"""
        data = api.payload
        if data is None:
            return {'message': 'Invalid input data'}, 400
            
        try:
            new_amenity = facade.create_amenity(data)
            return new_amenity, 201
        except ValueError as e:
            return {'message': str(e)}, 400
        except Exception as e:
            logger.error(f"Error creating amenity: {str(e)}")
            return {'message': 'An error occurred while creating the amenity'}, 500

@api.route('/<amenity_id>')
class AmenityResource(Resource):
    @api.expect(amenity_model)
    @api.response(200, 'Amenity updated successfully')
    @api.response(404, 'Amenity not found')
    @api.response(400, 'Invalid input data')
    def put(self, amenity_id):
        """Update an amenity's information"""
        data = api.payload
        if data is None:
            api.abort(400, "Invalid input data")
    
        existing_amenity = facade.get_amenity(amenity_id)
        if not existing_amenity:
            api.abort(404, "Amenity not found")
    
        try:
            updated_amenity = facade.update_amenity(amenity_id, data)
            return updated_amenity.to_dict(), 200
        except ValueError as e:
            return {'message': str(e)}, 400
        except Exception as e:
            logger.error(f"Error updating amenity: {str(e)}")
            return {'message': 'An error occurred while updating the amenity'}, 500

    @api.response(204, "Amenity deleted successfully")
    @api.response(404, "Amenity not found")
    def delete(self, amenity_id):
        """Delete an amenity by ID"""
        existing_amenity = facade.get_amenity(amenity_id)
        if not existing_amenity:
            api.abort(404, "Amenity not found")
        
        facade.delete_amenity(amenity_id)
        return '', 204  # No content to return
from flask_restx import Namespace, Resource, fields
from ...services.facade import HBnBFacade
from ...models.amenity import Amenity
import logging

api = Namespace('amenities', description='Amenity operations')
facade = HBnBFacade()
logger = logging.getLogger(__name__)

amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='Amenity name')
})

@api.route('/')
class AmenityList(Resource):
    @api.expect(amenity_model)
    @api.response(201, 'Amenity successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new amenity"""
        data = api.payload
        if data is None:
            return {'message': 'Invalid input data'}, 400
            
        try:
            new_amenity = facade.create_amenity(data)
            return new_amenity, 201
        except ValueError as e:
            return {'message': str(e)}, 400
        except Exception as e:
            logger.error(f"Error creating amenity: {str(e)}")
            return {'message': 'An error occurred while creating the amenity'}, 500

@api.route('/<amenity_id>')
class AmenityResource(Resource):
    @api.expect(amenity_model)
    @api.response(200, 'Amenity updated successfully')
    @api.response(404, 'Amenity not found')
    @api.response(400, 'Invalid input data')
    def put(self, amenity_id):
        """Update an amenity's information"""
        data = api.payload
        if data is None:
            api.abort(400, "Invalid input data")
    
        existing_amenity = facade.get_amenity(amenity_id)
        if not existing_amenity:
            api.abort(404, "Amenity not found")
    
        try:
            updated_amenity = facade.update_amenity(amenity_id, data)
            return updated_amenity.to_dict(), 200
        except ValueError as e:
            return {'message': str(e)}, 400
        except Exception as e:
            logger.error(f"Error updating amenity: {str(e)}")
            return {'message': 'An error occurred while updating the amenity'}, 500

    @api.response(204, "Amenity deleted successfully")
    @api.response(404, "Amenity not found")
    def delete(self, amenity_id):
        """Delete an amenity by ID"""
        existing_amenity = facade.get_amenity(amenity_id)
        if not existing_amenity:
            api.abort(404, "Amenity not found")
        
        facade.delete_amenity(amenity_id)
        return '', 204  # No content to return
