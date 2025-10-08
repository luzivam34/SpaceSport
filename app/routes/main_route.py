from flask import Blueprint, render_template


main_bp = Blueprint('index', __name__)


@main_bp.route('/')
def index():
    return render_template('index.html')
