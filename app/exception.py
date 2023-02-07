from flask import jsonify


def success(data=None, message=None):
    resp = {}
    if data:
        resp["data"] = data
    if message:
        resp["message"] = message
    return jsonify(resp), 200


def too_many_request(message='操作频繁'):
    return jsonify({"message": message}), 429


def bad_request(errors):
    return jsonify({"errors": errors}), 400


def conflict_error(message="已存在该记录"):
    return jsonify({"message": message}), 409


def error_with_message(message):
    return jsonify({"message": message}), 400


def auth_error():
    return jsonify({"message": '未登录'}), 401


def forbidden_error(message='未授权'):
    return jsonify({"message": message}), 403


def not_found(message='不存在该记录'):
    return jsonify({"message": message}), 404
