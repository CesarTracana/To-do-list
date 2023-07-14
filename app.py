from flask import Flask, render_template, request, redirect

app=Flask(__name__)

nombre="Cesar"
lista_tareas=[]
#ruta
@app.route('/')
#vista
def home():
    return render_template('home.html', nombre=nombre, lista_tareas=lista_tareas)

#ruta
@app.route('/agregar', methods=['GET', 'POST'])
#vista
def agregar():
        if request.method=='POST':
              nueva_tarea=request.form.get('tarea')
              lista_tareas.append(nueva_tarea)
        return redirect('/')

#ruta para eliminar
@app.route('/delete/<int:id>')
#vista
def borrar(id):
      lista_tareas.pop(id)
      return redirect('/')

@app.route('/about/<nombre>')
def about(nombre):
      return f'¡hola, yo soy {nombre} y estudia ingenieria en computacion'