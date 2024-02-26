#!/usr/bin/python3
"""
Index file for the views
"""


from flask import jsonify, make_response
from api.v1.views import app_views
from models import storage


@app_views.app_errorhandler(404)
def err_404(e):
    """
    Error handler for 404
    """
    resp = make_response(jsonify({'error': 'Not found'}))
    resp.status_code = 404
    return resp


@app_views.app_errorhandler(400)
def err_400(e):
    """
    Error handler for 400
    """
    resp = make_response(jsonify({'error': 'Not a JSON'}))
    resp.status_code = 400
    return resp


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def show_status():
    """
    Returns the api status
    """
    resp = make_response(jsonify({'status': 'OK'}))
    resp.status_code = 200
    return resp


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    """
    Retrieves the number of each objects by type
    """
    objs = storage.all().values()
    obdict = {}
    for obj in objs:
        cls = obj.__class__
        clsname = obj.__class__.__name__
        obdict[clsname] = storage.count(cls)

    resp = make_response(jsonify(obdict), 200)
    return resp
