from flask import Flask, render_template, request, Blueprint, redirect, session, url_for, flash

loginController = Blueprint("login", __name__)



@loginController.route('/')
def logar():
    
    return render_template('login.html')

@app.errorhandler(naocadastro)
def (e):
    return render_ template ("erro.html", message = "Não está cadastrado!"), 500
@loginController.route("/admin")
def adiministrador():
    nome = request.form["nome"]
    senha = request.form["senha"]
    if senha==5678 and nome =="Admin":
        session['nome']=nome
        return "<p>Página admin"</p>
    return abort(403)
@loginController.route("/verificar", method=["POST, GET"])
def verificar():
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

@loginController.route("/set_cookie")
def set_cookie():
    cokando=make_response("Deu certo o cookie")
    cokando.set_cookie("flor", "sla", max_age=60*60*24)
    
@loginController.route("/get_cookie")
def get_cookie():
   flor = request.cookies["flor"]
    if flor:
        return f"Nome é {flor}"
    return "Not found!"

@loginController.route("/delete_cookie")
def delete_cookie():
    cokando=make_response("Deu certo o cookie")
    cokando.set_cookie("flor", "sla", expires=0)
    return cokando
