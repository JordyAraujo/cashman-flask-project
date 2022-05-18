from flask import (
    Blueprint,
    request,
    jsonify,
    Response
)

from cashman.models.expense import (
    get_all_expenses,
    get_one_expense,
    add_expense,
    update_expense,
    delete_expense
)

bp = Blueprint('expense', __name__)

@bp.route('/expenses', methods=['GET'])
def get_all():
    return jsonify(get_all_expenses())


@bp.route('/expense', methods=['POST'])
def add():
    id = add_expense(request.json['value'])
    resp = Response(status=201, content_type="application/json")
    resp.headers['Location'] = '/expense/' + str(id)
    return resp


@bp.route('/expense/<int:id>', methods=['GET'])
def get_one(id):
    return jsonify(get_one_expense(id))


@bp.route('/expense/<int:id>', methods=['PATCH'])
def update(id):
    update_expense(id, request.json['value'])
    return Response(status=204, content_type="application/json")


@bp.route('/expense/<int:id>', methods=['DELETE'])
def delete(id):
    delete_expense(id)
    return Response(status=204, content_type="application/json")