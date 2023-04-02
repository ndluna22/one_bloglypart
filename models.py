from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


# MODELS GO BELOW!


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)

    first_name = db.Column(db.Text,
                           nullable=False,
                           unique=True)

    last_name = db.Column(db.Text, nullable=False, unique=True)

    image_url = db.Column(db.Text, nullable=False,
                          default="https://www.iconpacks.net/icons/2/free-user-icon-3296-thumb.png")

    @property
    def full_name(self):
        """Return full name of user."""

        return f"{self.first_name} {self.last_name}"
