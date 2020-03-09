import casas
from flask import Flask, render_template

app= Flask(__name__)       #instancia la clase de Flask y crea un objeto app
@app.route('/')     #esta es la raiz
def indice():
    datos = casas.casas()       #esto devuelve los datos
    #escrapeamos desde casas.py
    return render_template('index.html',datos=datos )

if __name__ =="__main__":
    app.run()