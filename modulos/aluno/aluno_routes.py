from flask import Blueprint, render_template
from util.security import permission

aluno_bp = Blueprint("aluno", __name__, url_prefix="/aluno")

@aluno_bp.route("/")
@permission(['ALUNO'])
def home_aluno():
    return render_template("Menu_F.html")