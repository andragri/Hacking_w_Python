from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://eventuser:Heute000@127.0.0.1/eventdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'f1c50cdf58a5ac7024799454' #mit selenium raus kriegen 

db = SQLAlchemy(app) # Klasse mit zugriff auf db also mit app instanzieren

from event import routes

#github hochladne und den cookie encrypten 