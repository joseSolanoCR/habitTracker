from flask import Flask
from routes import pages

#for venv
#def create_app():
#    app = Flask(__name__)
#    app.register_blueprint(pages)

#    if __name__ == "__main__":
#        app.run(host='localhost', debug=True)

#    return app

#for pycharm direct
app = Flask(__name__)
app.register_blueprint(pages)

if __name__ == "__main__":
    app.run(host='localhost', debug=True)
