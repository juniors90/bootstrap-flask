# Option 1
from entrypoint import app # instancia de Flask
from app import db # instancia SQLAlchemy

with app.app_context():
    db.create_all()


# Option 2
from entrypoint import app # instancia de Flask
from app import db # instancia SQLAlchemy

db.create_all(app=app)