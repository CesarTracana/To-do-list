from flask import Flask, render_template

app=Flask(__name__)

#ruta
@app.route('/')
#vista
def index():
    return render_template('base.html')
