from flask import Blueprint, jsonify

from cashman.models import transaction

bp = Blueprint("transaction", __name__)


@bp.route("/transactions", methods=["GET"])
def get_all():
    return jsonify(transaction.get_all())
