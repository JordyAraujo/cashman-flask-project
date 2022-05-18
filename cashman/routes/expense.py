from flask import Blueprint, Response, jsonify, request

from cashman.models import expense

bp = Blueprint("expense", __name__)


@bp.route("/expenses", methods=["GET"])
def get_all():
    return jsonify(expense.get_all())


@bp.route("/expense", methods=["POST"])
def add():
    expense_id = expense.add(request.json["value"])
    resp = Response(status=201, content_type="application/json")
    resp.headers["Location"] = "/expense/" + str(expense_id)
    return resp


@bp.route("/expense/<int:id>", methods=["GET"])
def get_one(expense_id):
    return jsonify(expense.get_one(expense_id))


@bp.route("/expense/<int:expense_id>", methods=["PATCH"])
def update(expense_id):
    expense.update(expense_id, request.json["value"])
    return Response(status=204, content_type="application/json")


@bp.route("/expense/<int:expense_id>", methods=["DELETE"])
def delete(expense_id):
    expense.delete(expense_id)
    return Response(status=204, content_type="application/json")
