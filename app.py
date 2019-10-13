from flask import Flask
from flask_restplus import Api, Resource, fields, marshal_with

application = Flask(__name__)
app = Api(app=application,
          version='1.0',
          title='Apartment Rental Api',
          description='Flask Swagger Apartment Rental Api',
          )

apartments = app.namespace('apartments', description='Api Operations Tour!')

model = app.model('Apartment Model', {
    'rent': fields.Integer(description='Monthly Rental Cost'),
    'address': fields.String(description='Location - Address'),
    'city': fields.String(description='Location - City'),
    'state': fields.String(description='Location - State'),
    'zip code': fields.Integer(description='Location - Zip Code'),
})


@apartments.route('/')
class ApartmentsList(Resource):
    @apartments.marshal_with(model)
    def get(self):
        return {'hello': 'world'}

    @apartments.expect(model, validate=True)
    @apartments.marshal_with(model)
    def post(self):
        return {"status": "Posted new data"}


@apartments.route('/<int:id>')
class Apartments(Resource):
    def get(self):
        return {'hello': 'world'}

    def put(self):
        return {'status': 'something got updated'}

    def delete(self):
        return {'status': 'something got deleted'}


if __name__ == '__main__':
    app.run(debug=True)
