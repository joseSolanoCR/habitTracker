import os
from flask import Flask
from routes import pages
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

#for venv
#def create_app():
#    app = Flask(__name__)
#    app.register_blueprint(pages)

#    if __name__ == "__main__":
#        app.run(host='localhost', debug=True)

#    return app

#for pycharm direct
app = Flask(__name__)
client = MongoClient(os.environ.get("MONGODB_URI"))
app.db = client.get_default_database()
app.register_blueprint(pages)

if __name__ == "__main__":
    app.run(host='localhost', debug=True)
