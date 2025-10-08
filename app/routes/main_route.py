from flask import Blueprint, render_template # importação do blueprint e render_templates do flask


main_bp = Blueprint('index', __name__)# Neste arquivo o blueprint vai se chamar main_bp

# route index criado a função e uma route para index
@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route("/cadastros")
def cadastros():
    return render_template('cadastros/index.html')
