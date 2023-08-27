from flask import Blueprint, render_template
from util.security import permission

professor_bp = Blueprint("professor", __name__, url_prefix="/professor")

@professor_bp.route("/")
@permission(['PROFESSOR'])
def home_professor():
    return render_template("Menu_F.html")