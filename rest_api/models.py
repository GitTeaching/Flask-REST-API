from rest_api import db, ma


#Product class/model
class Product(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), unique=True, nullable=False)
	descr = db.Column(db.String(200))
	price = db.Column(db.Float, nullable=False)
	qty = db.Column(db.Integer, nullable=False)

	def __init__(self, name, descr, price, qty):
		self.name = name
		self.descr = descr
		self.price = price
		self.qty = qty

	def __repr__(self):
		return f"Product('{self.id}', '{self.name}')"


# Product schema
class ProductSchema(ma.Schema):
	class Meta:
		fields = ('id', 'name', 'descr', 'price', 'qty')

# Init schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)