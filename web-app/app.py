import os
from flask import Flask, render_template, make_response, request, redirect, url_for
from pymongo import MongoClient

def create_app():

    app = Flask(__name__)

    MONGO_URI = os.getenv("MONGO_URI")

    if MONGO_URI is None:
        raise ValueError("Error with URI")
    
    try:
        client = MongoClient(MONGO_URI)
        db = client.get_database("ASL-DB")
        collection = db["entries"]
        print("Connected")
    except Exception as e:
        print(f"Error: {e}")

    @app.route("/")
    def home():
        # returns rendered html
        return render_template("index.html")
    
    @app.route("/upload_video", methods=["POST"])
    def upload_video():
        
        # TO DO

        return
    
    def get_data():

        # TO DO
        
        return
    

if __name__ == "__main__":
    FLASK_PORT = os.getenv("FLASK_PORT", "5000")
    app = create_app()
    app.run(port=FLASK_PORT)