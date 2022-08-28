import os
import dotenv
from flask import Flask
from app.main.dao.main_dao import MainDAO
from app.main.views import main_blueprint


app = Flask(__name__)

dotenv.load_dotenv(override=True)
if os.environ.get("APP_CONFIG") == "development":
    app.config.from_pyfile('config/development.py')
else:
    app.config.from_pyfile('config/production.py')
    
app.register_blueprint(main_blueprint)


from app.main.dao.main_dao import MainDAO

if __name__ == "__main__":
    # a = MainDAO()
    # b = a.load_posts()
    # print(b[0])
    app.run()
