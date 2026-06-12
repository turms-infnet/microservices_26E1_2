from models.Book import Book, db
from utils.validators import validate_fields

class BookService:
    @staticmethod
    def get_book(book_id, user_id):
        book = Book.query.filter_by(id=book_id, user_id=user_id).first()
        
        if not book:
            return {}, 404
        
        return book.to_dict(), 200
    
    @staticmethod
    def get_books(user_id):
        books =  Book.query.filter_by(user_id=user_id).all()
        books_dict = []

        for book in books:
            books_dict.append(book.to_dict())

        return books_dict
    
    @staticmethod
    def create_book(data, user_id):
        isbn = data.get("isbn", None)
        title = data.get("title", None)
        author = data.get("author", None)
        current_page = data.get("current_page", 0)
        total_pages = data.get("total_pages", None)
        finished = data.get("finished", False)

        required_fields = [
            'isbn',
            'title',
            'author',
            'total_pages'
        ]

        response, status = validate_fields(data, required_fields)

        if status == 400:
            return response, status

        
        new_book = Book(
            isbn=isbn,
            title=title,
            author=author,
            current_page=current_page,
            total_pages=total_pages,
            finished=finished,
            user_id=user_id
        )
        
        db.session.add(new_book)
        db.session.commit()

        return response, status
    
    @staticmethod
    def delete_book(book_id, user_id):
        book = Book.query.filter_by(id=book_id, user_id=user_id).first()
        if not book:
            return 404
        
        db.session.delete(book)
        db.session.commit()

        return 204
    
    @staticmethod
    def update_book(book_id, data, user_id):
        book = Book.query.filter_by(id=book_id, user_id=user_id).first()

        if not book:
            return 404
        
        protected = ["id", "user_id"]

        for key, value in data.items():
            if key not in protected and hasattr(book, key):
                setattr(book, key, value)

        db.session.commit()

        return 204