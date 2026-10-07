from flask import Flask
import socket
import datetime
import threading

# Creamos la aplicación web
app = Flask(__name__)

# Ruta principal: lo que se ve al entrar en la URL raíz ("/")
@app.route("/")
def home():
    return """
    <h1>¡Hola desde Render!</h1>
    <p>Esta aplicación Python se está ejecutando en la nube como un servicio PaaS.</p>
    <p>Visita <a href="/status">/status</a> para ver información del servidor.</p>
    """

# Ruta secundaria: /status, útil para relacionarlo con la monitorización (UD2, punto 6)
@app.route("/status")
def status():
    info = {
        "servidor": socket.gethostname(),
        "hora_actual": datetime.datetime.now().isoformat()
    }
    return info

# Función para iniciar la app en segundo plano
def run_app():
    app.run(host="0.0.0.0", port=5000, use_reloader=False)

# Esto iniciará el servidor en un hilo secundario sin bloquear Google Colab
if __name__ == "__main__":
    threading.Thread(target=run_app).start()
    print("El servidor Flask se está ejecutando en segundo plano en http://127.0.0.1:5000")
