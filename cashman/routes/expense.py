from flask import (
    Blueprint,
    request,
    jsonify,
    Response
)

from cashman.models import expense

bp = Blueprint('expense', __name__)

@bp.route('/expenses', methods=['GET'])
def get_all():
    return jsonify(expense.get_all())


@bp.route('/expense', methods=['POST'])
def add():
    id = expense.add(request.json['value'])
    resp = Response(status=201, content_type="application/json")
    resp.headers['Location'] = '/expense/' + str(id)
    return resp


@bp.route('/expense/<int:id>', methods=['GET'])
def get_one(id):
    return jsonify(expense.get_one(id))


@bp.route('/expense/<int:id>', methods=['PATCH'])
def update(id):
    expense.update(id, request.json['value'])
    return Response(status=204, content_type="application/json")


@bp.route('/expense/<int:id>', methods=['DELETE'])
def delete(id):
    expense.delete(id)
    return Response(status=204, content_type="application/json")