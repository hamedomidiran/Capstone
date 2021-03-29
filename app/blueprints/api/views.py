from .import bp as api_bp
from flask import jsonify, request
from app.blueprints.shop.models import Product
from app import db
from datetime import datetime as dt

@api_bp.route('/shop', methods=['GET'])
def get_products():
    return jsonify([p.to_dict() for p in Product.query.all()])

@api_bp.route('/shop/product/<int:id>', methods=['GET'])
def get_product(id):
    return jsonify(Product.query.get(id).to_dict())

@api_bp.route('/shop/product/create', methods=['POST'])
def create_product():
    data = request.json
    p = Product()
    p.from_dict(data)
    p.save()
    return jsonify(p.to_dict()), 201

@api_bp.route('/shop/product/edit/<int:id>', methods=['PUT'])
def edit_product(id):
    data = request.json
    p = Product.query.get(id)
    p.from_dict(data)
    p.date_updated = dt.utcnow()
    db.session.commit()
    return jsonify(p.to_dict()), 201

@api_bp.route('/shop/product/delete/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify([p.to_dict() for p in Product.query.all()])