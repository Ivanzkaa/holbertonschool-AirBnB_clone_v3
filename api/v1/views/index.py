#!/usr/bin/python3
"""the route and the status"""


from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status')
def status():
    """returning the status"""
    obj_stat = {
        "status": "OK"
    }

    return (jsonify(obj_stat))
