from flask import Flask, render_template, request, Blueprint, redirect, session, url_for, flash

loginController = Blueprint("login", __name__)



@loginController.route('/')
def logar():
    
    return render_template('login.html')

@app.errorhandler(naocadastro)
def (e):
    return render_ template ("erro.html", message = "Não está cadastrado!"), 500
    
@loginController.route("/verificar", method=["POST, GET"])
def verificar():
    nome = request.form["nome"]
    senha = request.form["senha"]
    if senha==1234 and nome =="Any":
        session['nome']=nome
        flash.sucess("Login de sucesso!")
        return render_template('logarr.html')
    flash.error("Algo deu errado!")
    abort(401)
    return 'Usuário não cadastrado'

@loginController.route('/login')
def logar():
        return redirect(url_for("login.logarr"))
    
@loginController.route('/logout')
def deslogar():
    session.pop("nome", None)
    return redirect(url_for("login.login"))
