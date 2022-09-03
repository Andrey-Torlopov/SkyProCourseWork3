from flask import Blueprint, request, render_template
from app.modules.app_dao import AppDAO
from app.models.post import Post
from app.models.comment import Comment

post_blueprint = Blueprint('post_blueprint', __name__, template_folder='templates')

appDAO = AppDAO()

@post_blueprint.route('/post/<int:id>')
def page_index(id):
    post = appDAO.get_post_by(id)
    if post is None:
        return ""
    
    return render_template("post.html", post=post.get_dict)