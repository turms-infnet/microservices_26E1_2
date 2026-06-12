from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

db = SQLAlchemy()

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(20), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(200), nullable=False)
    current_page = db.Column(db.Integer, nullable=False)
    total_pages = db.Column(db.Integer, nullable=False)
    finished = db.Column(db.Boolean, default=False, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, server_default=func.now(), name="CREATED_AT")
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now(), name="UPDATED_AT")
    

    def __repr__(self):
        return f'<Book {self.title}>'

    def to_dict(self):
        return {
            'id': self.id,
            'isbn': self.isbn,
            'title': self.title,
            'author': self.author,
            'user_id': self.user_id,
            'current_page': self.current_page,
            'total_pages': self.total_pages,
            'finished': self.finished,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }