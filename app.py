from flask import Flask
import socket
import datetime
# Creamos la aplicación web
app = Flask(__name__)
# Ruta principal: lo que se ve al entrar en la URL raíz ("/")
@app.route("/")
def home():
return """
<h1>¡Hola desde Render!</h1>
1
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
# Esto solo se usa si ejecutas la app en tu propio ordenador (no en Render)
if __name__ == "__main__":
app.run(host="0.0.0.0", port=5000)