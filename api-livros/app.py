from flask import Flask
from models.Book import db, Book
from routes.book_routes import book_bp
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
    app.config['SECRET_KEY'] = 'D/BsKXfFusBPeq2E+jLEDhpvi5lhgzMdL6e4l4RsGzo='

    db.init_app(app)
    with app.app_context():
        db.create_all()

    app.register_blueprint(book_bp)

    # Configuração do Flask-Admin
    admin = Admin(app, name='Área de Administração')
    admin.add_view(ModelView(Book, db.session))

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(port=5000, debug=True)