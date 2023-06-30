from flask import Flask, render_template

app=Flask(__name__)

nombre="Cesar"
lista_nombres=['Brhadaran', 'Yako', 'Panisha', 'Dviveka', 'Chudamani', 'Erreh']
#ruta
@app.route('/')
#vista
def home():
    return render_template('home.html', nombre=nombre, lista_nombres=lista_nombres)

""" @app.route('/about')
def about(nombre):
    return f' !hols, yo soy {nombre} y estudio ingenieria en computacion
"""