
import os
from app import app
from app import app,db
from app.models import Usuario,Ocorrencia
from werkzeug.utils import secure_filename
from flask import render_template,url_for,request,redirect,flash,session
from werkzeug.security import generate_password_hash, check_password_hash



# PRINCIPAL 

# teste
@app.route('/')
def teste():
    return render_template('teste.html')

@app.route('/index/')
def index():
    return render_template('index.html')


@app.route('/sobre/')
def sobre():
    return render_template('sobre.html')

# LOGIN USUARIO 

@app.route('/login/', methods=['GET', 'POST'])
def login_usuario():
    if request.method == 'POST':
        nome = request.form.get('nome')
        senha = request.form.get('senha')
        user = Usuario.query.filter_by(nome=nome).first()
        
        if user and check_password_hash(user.senha, senha):
            session['nome'] = nome
            session['sobrenome'] = user.sobrenome  # Adiciona o sobrenome à sessão
            session['usuario_id'] = user.id
            flash('Login bem-sucedido!', 'success')
            return redirect(url_for('sobre')) 
        else:
            flash('Nome de usuário ou senha incorretos. Tente novamente.', 'error')
    return render_template('login.html')

# SAIR
@app.route('/logout/')
def sair():
    session.pop('nome', None)
    session.pop('usuario_id', None)
    flash('Logout realizado com sucesso!', 'success')
    return redirect(url_for('login_usuario'))


#CADASTRO USUARIO

@app.route('/cadastro/', methods=['GET', 'POST'])
def cadastro_usuario():
    if request.method == 'POST':
        nome = request.form.get('nome')  
        senha = request.form.get('senha')
        confirma_senha = request.form.get('confirma_senha')
        email = request.form.get('email')
        cpf = request.form.get('cpf')
        sobrenome = request.form.get("sobrenome")
        endereco = request.form.get('endereco')
        numero_casa = request.form.get("numero_casa")
        bairro = request.form.get("bairro")

        if senha != confirma_senha:
            flash('As senhas não coincidem. Tente novamente.', 'danger')
            return redirect(url_for('cadastro_usuario'))
        
       # validações aqui


       ##################

        cripto_senha = generate_password_hash(senha)
        novo_usuario = Usuario (
            nome=nome,
            senha=cripto_senha,
            email=email, 
            cpf=cpf,
            sobrenome = sobrenome,
            endereco = endereco,
            numero_casa = numero_casa,
            bairro = bairro
            )

        db.session.add(novo_usuario)
        db.session.commit()

        flash('Cadastro realizado com sucesso! Faça login agora.', 'success')
        return redirect(url_for('login_usuario'))
    return render_template('cadastro.html')


#REGISTRA OCORRENCIA 

@app.route('/registrar_ocorrencia/', methods=['GET', 'POST'])
def registrar_ocorrencia():
    if request.method == 'POST':
        usuario_id = session.get('usuario_id')
        nome = session.get('nome')
        sobrenome = session.get('sobrenome')
        bairro = request.form.get('bairro')
        tipo_problema = request.form.get('tipo_problema')
        outro_problema = request.form.get('outro-problema') if tipo_problema == 'outro' else None
        nome_interior = request.form.get('nome_interior')
        descricao = request.form.get('descricao')
        imagem = request.files['imagem'] 
        nome_seguro = secure_filename(imagem.filename)
        
        nova_ocorrencia = Ocorrencia(
            usuario_id=usuario_id,
            tipo_problema=tipo_problema,
            descricao=descricao,
            imagem=nome_seguro,
            sobrenome = sobrenome,
            bairro = bairro,
            nome = nome,
            
            nome_interior = nome_interior,
            outro_problema = outro_problema
        )

        caminho = os.path.join(
            os.path.abspath(os.path.dirname(__file__)),
            app.config['UPLOAD_FILES'],
            'imagens_ocorrencia',
            nome_seguro 
        )
         
        imagem.save(caminho)
        db.session.add(nova_ocorrencia)
        db.session.commit()
        
        flash('Ocorrência registrada com sucesso!', 'success')
        return redirect(url_for('index'))
    return render_template('ocorrencia.html')

# LISTA OCORRENCIA

@app.route('/ocorrencias/', methods=['GET'])
def listar_ocorrencias():
    ocorrencias = db.session.query(Ocorrencia, Usuario).join(Usuario, Ocorrencia.usuario_id == Usuario.id).all()
    return render_template('listar_ocorrencias.html', ocorrencias=ocorrencias)


