from flask import *
import conexion
from Models.persona import modelPersona

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Corriendo servidor Flask</h1>"

@app.route('/crear', methods=['GET', 'POST'])
def crear():
    
    if request.method == 'POST':
        nombre = request.form['name']
        apellido = request.form['last_name']
        modelPersona.create(conexion.obtener_conexion(),nombre,apellido)
        return render_template('crear.html')
    else:    
        return render_template('crear.html')


@app.route('/index', methods=['GET', 'POST'])
def persona_index():
    listado=modelPersona.personas(conexion.obtener_conexion())
    return render_template('index.html',listado=listado)
    
    
    
if __name__ == '__main__':
    app.run(debug=True)
