# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify


api_bp = Blueprint('api', __name__)

@api_bp.route('/api/home', methods=['GET'])
def home():
        return jsonify("hello world"), 201
