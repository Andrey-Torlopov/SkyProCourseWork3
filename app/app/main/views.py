from flask import Blueprint, request, render_template

from app.main.dao.main_dao import MainDAO

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')

main_dao = MainDAO()

@main_blueprint.route('/')
def page_index():
    posts = list(map(lambda x: x.get_dict, main_dao.load_posts()))
    return render_template("index.html", posts=posts)