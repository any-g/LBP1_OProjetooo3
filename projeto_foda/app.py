from flask import Flask, render_template, redirect, url_for, request, session
from controllers.login import login_control
from controllers.controller import any_controller
app = Flask(__name__)
app.secret_key = 'chave_screta'
app.register_blueprint(login_control)

if __name__ == "__main__":
    app.run()
