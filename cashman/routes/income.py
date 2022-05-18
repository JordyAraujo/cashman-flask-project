from flask import (
    Blueprint,
    request,
    jsonify,
    Response
)

from cashman.models import income

bp = Blueprint('income', __name__)


@bp.route('/incomes', methods=['GET'])
def get_all():
    return jsonify(income.get_all())


@bp.route('/income', methods=['POST'])
def add():
    id = income.add(request.json['value'])
    resp = Response(status=201, content_type="application/json")
    resp.headers['Location'] = '/income/' + str(id)
    return resp


@bp.route('/income/<int:id>', methods=['GET'])
def get_one(id):
    return jsonify(income.get_one(id))


@bp.route('/income/<int:id>', methods=['PATCH'])
def update(id):
    income.update(id, request.json['value'])
    return Response(status=204, content_type="application/json")


@bp.route('/income/<int:id>', methods=['DELETE'])
def delete(id):
    income.delete(id)
    return Response(status=204, content_type="application/json")