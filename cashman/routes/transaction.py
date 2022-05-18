from flask import (
    Blueprint,
    jsonify
)

from cashman.models.transaction import (
    get_all_transactions
)

bp = Blueprint('transaction', __name__)

@bp.route('/transactions')
def get_all():
    return jsonify(get_all_transactions())