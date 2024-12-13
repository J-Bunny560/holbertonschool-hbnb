from flask_restx import Namespace, Resource, fields
from app.services.facade import HBnBFacade

api = Namespace('users', description='User operations')

# Define the user model for input validation and documentation
user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email of the user')
})

facade = HBnBFacade()

@api.route('/')
class UserList(Resource):
    @api.expect(user_model, validate=True)
    @api.response(201, 'User successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new user"""
        user_data = api.payload

        # Simulate email uniqueness check (to be replaced by real validation with persistence)
        existing_user = facade.get_user_by_email(user_data['email'])
        if existing_user:
            return {'error': 'Email already registered'}, 400

        try:
            new_user = facade.create_user(user_data)
        except ValueError as e:
            return {'error': str(e)}, 400
        return {
            'id': new_user.id,
            'first_name': new_user.first_name,
            'last_name': new_user.last_name, 
            'email': new_user.email
            }, 201

    @api.response(200, 'List of users retrieved successfully')
    @api.response(404, 'No users found')
    def get(self):
        """Retrieves a list of all users"""
        users = facade.get_all_users()
        if not users:
            return {'error': 'No users found'}, 404

        users_list = [user.toJSON() for user in users]
        return users_list, 200

@api.route('/<user_id>')
class UserResource(Resource):
    @api.response(200, 'User details retrieved successfully')
    @api.response(404, 'User not found')
    def get(self, user_id):
        """Get user details by ID"""
        user = facade.get_user(user_id)
        if user:
            return user.toJSON(), 200
        return {'error': 'User not found'}, 404

    @api.expect(user_model, validate=True)
    @api.response(200, 'User updated successfully')
    @api.response(404, 'User not found')
    @api.response(400, "Invalid input data")
    def put(self, user_id):
        "Updates information of a User by ID"

        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 400
        
        new_user = facade.update_user(user_id, api.payload)

        if not new_user:
            return {'error': 'Invalid input data'}, 400
        return new_user.toJSON()
    
    @api.response(204, "User deleted successfully")
    @api.response(404, "User not found")
    def delete(self, user_id):
        "Delete a user by ID"
        try:
            facade.delete_user(user_id)
            return {}, 204
        except ValueError as e:
            return {"Error": str(e)}, 404