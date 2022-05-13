from flask import (
    Blueprint,
    request,
    jsonify,
    Response
)

from cashman.models.enum import TransactionType
from cashman.db import get_db
from cashman.models.transaction import (
    get_one_transaction,
    get_all_transactions,
    add_transaction,
    update_transaction,
    delete_transaction,
    get_all_incomes
)

bp = Blueprint('transaction', __name__)

@bp.route('/transactions')
def get_all():
    return jsonify(get_all_transactions())


@bp.route('/incomes', methods=['GET'])
def get_incomes():
    return jsonify(get_all_incomes())


@bp.route('/income', methods=['POST'])
def add_income():
    id = add_transaction(TransactionType.INCOME.name, request.json['value'])
    resp = Response(status=201, content_type="application/json")
    resp.headers['Location'] = '/income/' + str(id)
    return resp


@bp.route('/income/<int:id>', methods=['GET'])
def get_income(id):
    return jsonify(get_one_transaction(id))


@bp.route('/income/<int:id>', methods=['PATCH'])
def update_income(id):
    update_transaction(id, TransactionType.INCOME.name, request.json['value'])
    return Response(status=204, content_type="application/json")


@bp.route('/income/<int:id>', methods=['DELETE'])
def delete_income(id):
    delete_transaction(id)
    return Response(status=204, content_type="application/json")