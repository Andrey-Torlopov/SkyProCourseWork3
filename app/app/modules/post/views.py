from flask import Blueprint, request, render_template

# from app.post.dao.main_dao import MainDAO

post_blueprint = Blueprint('post_blueprint', __name__, template_folder='templates')

# main_dao = MainDAO()

@post_blueprint.route('/post/<int:id>')
def page_index(id ):
    print(f'post id: {id}')
    # posts = list(map(lambda x: x.get_dict, main_dao.load_posts()))
    # return render_template("index.html", posts=posts)
    return "oK"