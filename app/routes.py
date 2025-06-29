from flask import Blueprint, request, jsonify
from .models import Sesion
from . import db

main = Blueprint('main', __name__)

@main.route('/sesiones', methods=['GET'])
def get_sesiones():
    sesiones = Sesion.query.all()
    result = []
    for s in sesiones:
        result.append({
            "numeroSesion": s.numero_sesion,
            "fecha": s.fecha,
            "tipoDia": s.tipo_dia,
            "duracion": s.duracion,
            "jugadoresDisponibles": s.jugadores_disponibles,
            "modulos": s.modulos,
            "observaciones": s.observaciones
        })
    return jsonify(result)

@main.route('/sesiones/<numero>', methods=['GET'])
def get_sesion(numero):
    sesion = Sesion.query.filter_by(numero_sesion=numero).first()
    if sesion:
        return jsonify({"exists": True})
    return jsonify({"exists": False})

@main.route('/sesiones', methods=['POST'])
def create_sesion():
    data = request.get_json()
    if Sesion.query.filter_by(numero_sesion=data["numeroSesion"]).first():
        return jsonify({"error": "Sesión ya existe"}), 400
    nueva = Sesion(
        numero_sesion=data["numeroSesion"],
        fecha=data["fecha"],
        tipo_dia=data["tipoDia"],
        duracion=data["duracion"],
        jugadores_disponibles=data["jugadoresDisponibles"],
        modulos=data["modulos"],
        observaciones=data["observaciones"]
    )
    db.session.add(nueva)
    db.session.commit()
    return jsonify({"message": "Sesión guardada exitosamente"}), 201