#!/usr/bin/python3
"""Blueprint and routes to principals route system"""
from api.v1.views import app_views
from flask import jsonify
import json


@app_views.route('/status', methods=['GET'])
def return_status():
    """Return json file with status"""
    return jsonify({
        "status": "OK"
    })
