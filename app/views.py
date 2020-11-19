from . import app
from flask import jsonify, request
from .services.users import Users
from .services.data import IDMdata
from .services.ingest import IngestService
from .settings import APP_NAME, APP_VERSION


@app.route('/')
def index():
    return jsonify({"node": APP_NAME, "version": APP_VERSION}), 200


@app.route('/users', methods=['POST'])
def user_data():
    request_data = request.get_json()
    if request_data is None:
        return "", 400
    request_data['user_id'] = request.headers.get('user_id')
    users = Users(request_data)
    data = users.get_user_data()
    if data is None:
        return "", 204
    ingest = IngestService()
    try:
        ingest.ingest_user(data)
        ingest.ingest_log(data)
    except Exception as err:
        return err, 400
    return jsonify(data=data), 200


@app.route('/users/distance/min', methods=['GET'])
def distance_min_data():
    idm_data = IDMdata()
    data = idm_data.get_min_distance()
    return jsonify(min=data), 200


@app.route('/users/distance/max', methods=['GET'])
def distance_max_data():
    idm_data = IDMdata()
    data = idm_data.get_max_distance()
    return jsonify(max=data), 200


@app.route('/logs/requests/<string:iso_code>/avg', methods=['GET'])
def requests_avg_data(iso_code):
    idm_data = IDMdata()
    data = idm_data.requests_avg_data(iso_code)
    return jsonify(avg=data), 200
