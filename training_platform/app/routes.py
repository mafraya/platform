from flask import render_template, request, redirect, url_for
from . import db
from .models import Session
from flask import current_app as app

MOMENTS = {
    'Ofensivo': ['Salida corta', 'Progresión', 'Finalización'],
    'Defensivo': ['Presión alta', 'Bloque medio', 'Bloque bajo'],
}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        new_session = Session(
            date=request.form["date"],
            session_number=request.form["session_number"],
            day_type=request.form["day_type"],
            moment=request.form["moment"],
            submoment=request.form["submoment"],
            content=request.form["content"],
            players=request.form["players"]
        )
        db.session.add(new_session)
        db.session.commit()
        return redirect(url_for("index"))

    sessions = Session.query.all()
    return render_template("index.html", sessions=sessions, moments=MOMENTS)