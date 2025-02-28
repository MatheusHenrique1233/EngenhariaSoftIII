
from app import db
from datetime import datetime

# aplica a normalização, dividir em subtabelas menores para tr a responsa só de 2

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), unique=False, nullable=False)
    senha = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    sobrenome = db.Column(db.String(20),unique = False,nullable = False)
    endereco = db.Column(db.String(255), nullable=False)
    bairro = db.Column(db.String(50), nullable=False)  
    numero_casa = db.Column(db.String(10), nullable=False)

class Ocorrencia(db.Model):
    __tablename__ = 'ocorrencia'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    nome = db.Column(db.String(100), nullable=False) # remover  pr não causar redundancia 
    sobrenome = db.Column(db.String(100), nullable=False) # remover pr não causar redundancia 
    nome_interior = db.Column(db.String(100), nullable=True) 
    bairro = db.Column(db.String(100), nullable=False)
    tipo_problema = db.Column(db.String(100), nullable=False)  
    outro_problema = db.Column(db.String(100), nullable=True)  
    descricao = db.Column(db.Text, nullable=True) 
    imagem = db.Column(db.String(255), nullable=True,default ='default.png')  
    usuario = db.relationship('Usuario', backref=db.backref('ocorrencias', lazy=True))

    


