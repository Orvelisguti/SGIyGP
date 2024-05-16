from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///finances.db'
db = SQLAlchemy(app)

# Definición de las entidades

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    ingresos = db.relationship('Ingreso', backref='usuario', lazy=True)
    gastos = db.relationship('Gasto', backref='usuario', lazy=True)

class Ingreso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(200), nullable=False)
    monto = db.Column(db.Float, nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)

class Gasto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(200), nullable=False)
    monto = db.Column(db.Float, nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)

# Rutas CRUD para Usuario
@app.route('/usuarios', methods=['POST'])
def crear_usuario():
    data = request.get_json()
    nuevo_usuario = Usuario(nombre=data['nombre'], email=data['email'])
    db.session.add(nuevo_usuario)
    db.session.commit()
    return jsonify({'id': nuevo_usuario.id, 'nombre': nuevo_usuario.nombre, 'email': nuevo_usuario.email}), 201

@app.route('/usuarios/<int:id>', methods=['GET'])
def obtener_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    return jsonify({'id': usuario.id, 'nombre': usuario.nombre, 'email': usuario.email})

@app.route('/usuarios/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    data = request.get_json()
    usuario.nombre = data['nombre']
    usuario.email = data['email']
    db.session.commit()
    return jsonify({'id': usuario.id, 'nombre': usuario.nombre, 'email': usuario.email})

@app.route('/usuarios/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    return jsonify({'mensaje': 'El usuario ha sido eliminado'}), 200

# Rutas CRUD para Ingreso
@app.route('/ingresos', methods=['POST'])
def crear_ingreso():
    data = request.get_json()
    nuevo_ingreso = Ingreso(descripcion=data['descripcion'], monto=data['monto'], usuario_id=data['usuario_id'])
    db.session.add(nuevo_ingreso)
    db.session.commit()
    return jsonify({'id': nuevo_ingreso.id, 'descripcion': nuevo_ingreso.descripcion, 'monto': nuevo_ingreso.monto, 'usuario_id': nuevo_ingreso.usuario_id}), 201

@app.route('/ingresos/<int:id>', methods=['GET'])
def obtener_ingreso(id):
    ingreso = Ingreso.query.get_or_404(id)
    return jsonify({'id': ingreso.id, 'descripcion': ingreso.descripcion, 'monto': ingreso.monto, 'usuario_id': ingreso.usuario_id})

@app.route('/ingresos/<int:id>', methods=['PUT'])
def actualizar_ingreso(id):
    ingreso = Ingreso.query.get_or_404(id)
    data = request.get_json()
    ingreso.descripcion = data['descripcion']
    ingreso.monto = data['monto']
    db.session.commit()
    return jsonify({'id': ingreso.id, 'descripcion': ingreso.descripcion, 'monto': ingreso.monto, 'usuario_id': ingreso.usuario_id})

@app.route('/ingresos/<int:id>', methods=['DELETE'])
def eliminar_ingreso(id):
    ingreso = Ingreso.query.get_or_404(id)
    db.session.delete(ingreso)
    db.session.commit()
    return jsonify({'mensaje': 'El ingreso ha sido eliminado'}), 200

# Rutas CRUD para Gasto
@app.route('/gastos', methods=['POST'])
def crear_gasto():
    data = request.get_json()
    nuevo_gasto = Gasto(descripcion=data['descripcion'], monto=data['monto'], usuario_id=data['usuario_id'])
    db.session.add(nuevo_gasto)
    db.session.commit()
    return jsonify({'id': nuevo_gasto.id, 'descripcion': nuevo_gasto.descripcion, 'monto': nuevo_gasto.monto, 'usuario_id': nuevo_gasto.usuario_id}), 201

@app.route('/gastos/<int:id>', methods=['GET'])
def obtener_gasto(id):
    gasto = Gasto.query.get_or_404(id)
    return jsonify({'id': gasto.id, 'descripcion': gasto.descripcion, 'monto': gasto.monto, 'usuario_id': gasto.usuario_id})

@app.route('/gastos/<int:id>', methods=['PUT'])
def actualizar_gasto(id):
    gasto = Gasto.query.get_or_404(id)
    data = request.get_json()
    gasto.descripcion = data['descripcion']
    gasto.monto = data['monto']
    db.session.commit()
    return jsonify({'id': gasto.id, 'descripcion': gasto.descripcion, 'monto': gasto.monto, 'usuario_id': gasto.usuario_id})

@app.route('/gastos/<int:id>', methods=['DELETE'])
def eliminar_gasto(id):
    gasto = Gasto.query.get_or_404(id)
    db.session.delete(gasto)
    db.session.commit()
    return jsonify({'mensaje': 'El gasto ha sido eliminado'}), 200
