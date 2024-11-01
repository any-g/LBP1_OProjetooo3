from flask import Flask, render_template, request, Blueprint, redirect, session, url_for

loginController = Blueprint("login", __name__)



@loginController.route('/')
def logar():
    return render_template('login.html')

@loginController.route("/verificar", method=["POST, GET"])
def verificar():
    nome = request.form["nome"]
    senha = request.form["senha"]
    if senha==1234 and nome =="Any":
        session['nome']=nome

        return render_template('logarr.html')
    return 'Usuário não cadastrado'

@loginController.route('/login')
def logar():
        return redirect(url_for("login.logarr"))
    
@loginController.route('/logout')
def deslogar():
    session.pop("nome", None)
    return redirect(url_for("login.login"))