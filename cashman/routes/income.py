from flask import (
    Blueprint,
    request,
    jsonify,
    Response
)

from cashman.models.income import (
    get_all_incomes,
    get_one_income,
    add_income,
    update_income,
    delete_income
)

bp = Blueprint('income', __name__)


@bp.route('/incomes', methods=['GET'])
def get_all():
    return jsonify(get_all_incomes())


@bp.route('/income', methods=['POST'])
def add():
    id = add_income(request.json['value'])
    resp = Response(status=201, content_type="application/json")
    resp.headers['Location'] = '/income/' + str(id)
    return resp


@bp.route('/income/<int:id>', methods=['GET'])
def get_one(id):
    return jsonify(get_one_income(id))


@bp.route('/income/<int:id>', methods=['PATCH'])
def update(id):
    update_income(id, request.json['value'])
    return Response(status=204, content_type="application/json")


@bp.route('/income/<int:id>', methods=['DELETE'])
def delete(id):
    delete_income(id)
    return Response(status=204, content_type="application/json")