
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:admin@localhost:3306/solucionaurb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.config['SECRET_KEY'] = '9393w@#&83545*&dj2'
app.config['UPLOAD_FILES'] = r'static/data'

from app.views import cadastro_usuario,login_usuario,registrar_ocorrencia,listar_ocorrencias,index,sobre,sair
from app.models import Usuario,Ocorrencia











