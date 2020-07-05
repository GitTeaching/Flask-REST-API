from flask import Flask, request, jsonify
from rest_api import app, db
from rest_api.models import Product, product_schema, products_schema


@app.route("/")
def home():
	return 'Hello World! REST API - CRUD'


# Create product
@app.route('/api/add_product', methods=['POST'])
def add_product():
	name = request.json['name']
	descr = request.json['descr']
	price = request.json['price']
	qty = request.json['qty']

	prod = Product(name, descr, price, qty)

	db.session.add(prod)
	db.session.commit()

	return product_schema.jsonify(prod)


# Read product by ID
@app.route('/api/get_product/<id>', methods=['GET'])
def get_product(id):
	prod = Product.query.get(id)
	return product_schema.jsonify(prod)


# Read all product 
@app.route('/api/get_products/', methods=['GET'])
def get_products():
	prods = Product.query.all()
	result = products_schema.dump(prods)
	return jsonify(result)


# Update product by ID
@app.route('/api/update_product/<id>', methods=['PUT'])
def update_product(id):
	prod = Product.query.get(id)

	name = request.json['name']
	descr = request.json['descr']
	price = request.json['price']
	qty = request.json['qty']

	prod.name = name
	prod.descr = descr
	prod.price = price
	prod.qty = qty

	db.session.commit()

	return product_schema.jsonify(prod)


# Delete product by ID
@app.route('/api/delete_product/<id>', methods=['DELETE'])
def delete_product(id):
	prod = Product.query.get(id)
	db.session.delete(prod)
	db.session.commit()
	return "Product deleted!"