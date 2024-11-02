from flask import Flask, render_template, session, redirect, url_for, request, flash
from aulatreino.controllers.logar import loginController

app = Flask(__name__)
app.registerBlueprint(loginController)
app.secret_key = "anyany"
#criptografar os cookies 

public_routes=["login.logar", "login.verificar"]

@app.before_request
def funcao():
    if request.endpoint == public_routes:
        return
    if 'nome' in session:
        return redirect(url_for("login.logarr"))
    return redirect(url_for('login.login'))

@app.route('/')
def hello_world():
    return render_template("index.html")
if __name__ == '__main__':
    app.run (debug=True)

#notes:
#after request --> preparação do ambiente para salvar algo, quando precisa registrar a resposta.
