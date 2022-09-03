import os
from re import A
import dotenv
from flask import Flask
from app.modules.app_dao import AppDAO
from app.modules.main.views import main_blueprint
from app.modules.post.views import post_blueprint
import app.modules.app_dao as app_dao

app = Flask(__name__)

dotenv.load_dotenv(override=True)
if os.environ.get("APP_CONFIG") == "development":
    app.config.from_pyfile('config/development.py')
else:
    app.config.from_pyfile('config/production.py')
    
app.register_blueprint(main_blueprint)
app.register_blueprint(post_blueprint)


def debug_func():
    ...
    # appDao = AppDAO()
    # posts = appDao.load_posts()
    # print(posts[0])

if __name__ == "__main__":
    debug_func()
    app.run()


