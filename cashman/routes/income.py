from flask import Blueprint, Response, jsonify, request

from cashman.models import income

bp = Blueprint("income", __name__)


@bp.route("/incomes", methods=["GET"])
def get_all():
    return jsonify(income.get_all())


@bp.route("/income", methods=["POST"])
def add():
    income_id = income.add(request.json["value"])
    resp = Response(status=201, content_type="application/json")
    resp.headers["Location"] = "/income/" + str(income_id)
    return resp


@bp.route("/income/<int:income_id>", methods=["GET"])
def get_one(income_id):
    return jsonify(income.get_one(income_id))


@bp.route("/income/<int:income_id>", methods=["PATCH"])
def update(income_id):
    income.update(income_id, request.json["value"])
    return Response(status=204, content_type="application/json")


@bp.route("/income/<int:income_id>", methods=["DELETE"])
def delete(income_id):
    income.delete(income_id)
    return Response(status=204, content_type="application/json")
