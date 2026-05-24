from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# =========================
# CONFIGURAÇÃO DO BANCO
# =========================

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///devops.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# =========================
# TABELA USUARIOS
# =========================

class Usuario(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nome = db.Column(
        db.String(100),
        nullable=False
    )

# =========================
# TABELA DENUNCIAS
# =========================

class Denuncia(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    descricao = db.Column(
        db.String(200),
        nullable=False
    )

    usuario_id = db.Column(
        db.Integer,
        db.ForeignKey('usuario.id')
    )

# =========================
# CRIAR BANCO
# =========================

with app.app_context():
    db.create_all()

# =========================
# ROTA PRINCIPAL
# =========================

@app.route('/')
def home():

    return "API rodando com sucesso!"

# =========================
# CRUD USUARIOS
# =========================

@app.route('/usuarios', methods=['POST'])
def criar_usuario():

    dados = request.json

    novo = Usuario(
        nome=dados['nome']
    )

    db.session.add(novo)
    db.session.commit()

    return jsonify({
        "mensagem": "Usuario criado"
    })

@app.route('/usuarios', methods=['GET'])
def listar_usuarios():

    usuarios = Usuario.query.all()

    resultado = []

    for u in usuarios:

        resultado.append({
            "id": u.id,
            "nome": u.nome
        })

    return jsonify(resultado)

# =========================
# CRUD DENUNCIAS
# =========================

@app.route('/denuncias', methods=['POST'])
def criar_denuncia():

    dados = request.json

    nova = Denuncia(
        descricao=dados['descricao'],
        usuario_id=dados['usuario_id']
    )

    db.session.add(nova)
    db.session.commit()

    return jsonify({
        "mensagem": "Denuncia criada"
    })

@app.route('/denuncias', methods=['GET'])
def listar_denuncias():

    denuncias = Denuncia.query.all()

    resultado = []

    for d in denuncias:

        resultado.append({
            "id": d.id,
            "descricao": d.descricao,
            "usuario_id": d.usuario_id
        })

    return jsonify(resultado)

# =========================
# EXECUTAR API
# =========================

if __name__ == '__main__':

    app.run(
        host='0.0.0.0',
        port=5000
    )
