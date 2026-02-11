from flask import Flask, render_template, request, redirect, url_for
from datetime import date, timedelta
import json
import os

app = Flask(__name__)

# =========================
# CONFIGURACIÓN DE FECHAS (PROTOTIPO)
# =========================
# Para pruebas, configuramos las fechas cercanas a hoy
HOY = date.today()
FASE_1_DATE = date (2026, 2, 11)  # Disponible mañana
FASE_2_DATE = date (2026, 2, 12)  # Disponible pasado mañana
FASE_3_DATE = HOY + timedelta(days=1)  # Disponible mañana (para probar bloqueo)

# =========================
# UTILIDADES
# =========================
DATA_PATH = "data/progreso.json"

def hoy():
    return date.today()

def fase_disponible(fase):
    today = hoy()
    if fase == 1:
        return today >= FASE_1_DATE
    if fase == 2:
        return today >= FASE_2_DATE
    if fase == 3:
        return FASE_3_DATE is not None and today >= FASE_3_DATE
    return False

def cargar_progreso():
    if not os.path.exists(DATA_PATH):
        return {"fase1": False, "fase2": False, "fase3": False}
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def guardar_progreso(data):
    os.makedirs("data", exist_ok=True)
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def validar_flexible(respuesta, claves):
    respuesta = respuesta.lower().strip()
    return any(clave in respuesta for clave in claves)

# =========================
# RUTAS
# =========================
@app.route("/")
def index():
    progreso = cargar_progreso()
    return render_template(
        "index.html",
        progreso=progreso,
        fase1_ok=fase_disponible(1),
        fase2_ok=fase_disponible(2),
        fase3_ok=fase_disponible(3)
    )

# =========================
# FASE 1 - DATOS DE PRUEBA
# =========================
@app.route("/fase1", methods=["GET", "POST"])
def fase1():
    if not fase_disponible(1):
        return render_template("bloqueado.html", mensaje="Esta fase aún no está disponible ⏰")

    progreso = cargar_progreso()

    error = None
    if request.method == "POST":
        respuesta = request.form.get("respuesta", "")
        # Respuesta de prueba: palabras relacionadas con "café"
        claves = ["helado", "centro comercial"]

        if validar_flexible(respuesta, claves):
            progreso["fase1"] = True
            guardar_progreso(progreso)
            return redirect(url_for("index"))
        else:
            error = "Mmm... no es la respuesta correcta. ¡Piensa en nuestra primera cita! ☕"

    return render_template("fase1.html", error=error)

# =========================
# FASE 2 - DATOS DE PRUEBA
# =========================
@app.route("/fase2", methods=["GET", "POST"])
def fase2():
    if not fase_disponible(2):
        return render_template("bloqueado.html", mensaje="Aún cargando... ⏳")

    progreso = cargar_progreso()
    if not progreso["fase1"]:
        return redirect(url_for("index"))

    error = None
    if request.method == "POST":
        respuesta = request.form.get("respuesta", "")
        # Respuesta de prueba: palabras relacionadas con "películas"
        claves = ["pelicula", "película", "netflix", "cine", "movie"]

        if validar_flexible(respuesta, claves):
            progreso["fase2"] = True
            guardar_progreso(progreso)
            return redirect(url_for("index"))
        else:
            error = "Error 404: Respuesta no encontrada... ¡piensa en nuestras noches! 🎬"

    return render_template("fase2.html", error=error)

# =========================
# FASE 3 - DATOS DE PRUEBA
# =========================
@app.route("/fase3", methods=["GET", "POST"])
def fase3():
    if not fase_disponible(3):
        return render_template(
            "bloqueado.html",
            mensaje="Esta fase se desbloqueará pronto... ten paciencia ✨"
        )

    progreso = cargar_progreso()
    if not progreso["fase2"]:
        return redirect(url_for("index"))

    error = None
    if request.method == "POST":
        respuesta = request.form.get("respuesta", "")
        # Respuesta de prueba: palabras sobre futuro
        claves = ["siempre", "forever", "juntos", "amor", "futuro"]

        if validar_flexible(respuesta, claves):
            progreso["fase3"] = True
            guardar_progreso(progreso)
            return render_template("final.html")
        else:
            error = "Casi... pero no del todo. ¡Habla desde el corazón! ❤️"

    return render_template("fase3.html", error=error)

# =========================
# MAIN
# =========================
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)