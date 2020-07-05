from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


# Init app
app = Flask(__name__)

# Init database
app.config['SECRET_KEY'] = '4c99e0361905b9f941f17729187afdb9'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restapi.db'
db = SQLAlchemy(app)

# Init ma
ma = Marshmallow(app)


from rest_api import routes