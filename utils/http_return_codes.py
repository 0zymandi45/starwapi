from flask import jsonify

class HttpReturnCodes:
    @staticmethod
    def success(data=None, message="Success"):
        response = {"message": message}
        if data is not None:
            response["data"] = data
        return jsonify(response), 200

    @staticmethod
    def created(data=None, message="Resource created successfully"):
        response = {"message": message}
        if data is not None:
            response["data"] = data
        return jsonify(response), 201

    @staticmethod
    def bad_request(message="Bad request"):
        response = {"message": message}
        return jsonify(response), 400

    @staticmethod
    def not_found(message="Resource not found"):
        response = {"message": message}
        return jsonify(response), 404

    @staticmethod
    def internal_error(message="Internal server error"):
        response = {"message": message}
        return jsonify(response), 500