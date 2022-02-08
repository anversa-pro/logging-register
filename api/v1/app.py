#!/usr/bin/python3
"""
   App module with instance of Flask
   blueprint registration and error handlers
"""
from flask import Flask, jsonify
from api.v1.views import app_views
from flask_cors import CORS
from flask_jwt_extended import JWTManager


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})
app.config["JWT_SECRET_KEY"] = "Holberton0621"
jwt = JWTManager(app)


app.register_blueprint(app_views)



@app.errorhandler(404)
def error_handler_404(self):
    """Method that returns a JSON-formatted
       404 status code
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(400)
def error_handler_400(self):
    """Method that returns a JSON-formatted
       400 status code
    """
    return jsonify({"error": self}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0",
            port=5000,
            threaded=True)
