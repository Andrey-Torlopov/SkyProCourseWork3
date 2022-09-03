from flask import Blueprint, request, render_template

from app.modules.app_dao import AppDAO

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')

appDao = AppDAO()

@main_blueprint.route('/')
def page_index():
    print("Catch!")
    posts = appDao.load_posts()
    return render_template("index.html", posts=posts)