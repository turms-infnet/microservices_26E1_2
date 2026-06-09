from models.Book import Book, db

class BookService:
    @staticmethod
    def get_book(book_id):
        book = Book.query.filter_by(id=book_id).first()
        
        if not book:
            return {}, 404
        
        return book.to_dict(), 200
    
    @staticmethod
    def get_books():
        books =  Book.query.all()
        books_dict = []

        for book in books:
            books_dict.append(book.to_dict())

        return books_dict
    
    @staticmethod
    def create_book(data):
        pass
    
    @staticmethod
    def delete_book(book_id):
        book = Book.query.filter_by(id=book_id).first()
        if not book:
            return 404
        
        db.session.delete(book)
        db.session.commit()

        return 204
    
    @staticmethod
    def update_book(book_id, data):
        book = Book.query.filter_by(id=book_id).first()

        if not book:
            return 404
        
        protected = ["id", "user_id"]

        for key, value in data.items():
            if key not in protected and hasattr(book, key):
                setattr(book, key, value)

        db.session.commit()

        return 204