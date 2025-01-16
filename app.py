from flask import Flask
from flask_pymongo import PyMongo
from dotenv import load_dotenv
import os

load_dotenv()

mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    app.config["MONGO_URI"] = os.getenv("MONGO_URI")

    try:
        mongo.init_app(app)
        mongo.cx.admin.command('ping')
        print("Connection with MongoDB established with success.")
    except Exception as e:
        print(f"Error trying to connect to MongoDB: {e}")
        raise SystemExit("End process.")

    return app
