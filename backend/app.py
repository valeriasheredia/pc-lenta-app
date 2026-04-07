from flask import Flask, jsonify
from flask_cors import CORS
from actions import (
    vaciar_papelera,
    abrir_limpieza_disco,
    abrir_administrador_tareas,
    abrir_config_inicio,
)

app = Flask(__name__)
CORS(app)


@app.route("/vaciar-papelera", methods=["POST"])
def ruta_vaciar_papelera():
    try:
        vaciar_papelera()
        return jsonify({"ok": True, "mensaje": "Papelera vaciada correctamente."})
    except Exception as e:
        return jsonify({"ok": False, "mensaje": f"Error al vaciar la papelera: {e}"}), 500


@app.route("/abrir-limpieza", methods=["POST"])
def ruta_abrir_limpieza():
    try:
        abrir_limpieza_disco()
        return jsonify({"ok": True, "mensaje": "Se abrió la limpieza de disco."})
    except Exception as e:
        return jsonify({"ok": False, "mensaje": f"Error al abrir la limpieza de disco: {e}"}), 500


@app.route("/abrir-admin-tareas", methods=["POST"])
def ruta_abrir_admin_tareas():
    try:
        abrir_administrador_tareas()
        return jsonify({"ok": True, "mensaje": "Se abrió el Administrador de tareas."})
    except Exception as e:
        return jsonify({"ok": False, "mensaje": f"Error al abrir el Administrador de tareas: {e}"}), 500


@app.route("/abrir-inicio", methods=["POST"])
def ruta_abrir_inicio():
    try:
        abrir_config_inicio()
        return jsonify({"ok": True, "mensaje": "Se abrió la configuración de programas de inicio."})
    except Exception as e:
        return jsonify({"ok": False, "mensaje": f"Error al abrir la configuración de inicio: {e}"}), 500


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"ok": True, "mensaje": "Backend funcionando correctamente."})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
