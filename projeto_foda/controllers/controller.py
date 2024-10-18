from flask import Blueprint,render_template
from models.model import Musicas, musics

any_controller = Blueprint('sol',__name__)

@any_controller.route('/dtdtd')
def index():
    return render_template("hestia.html", musicas=musics)
