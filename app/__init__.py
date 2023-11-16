from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    from app.models.user import User
    return User.query.get(int(user_id))

from .routes.auth import auth
from .routes.posts import posts
from .routes.index import main
from app.models.user import User
from app.models.post import Post

app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(posts, url_prefix='/posts')
app.register_blueprint(main, url_prefix='/')

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
