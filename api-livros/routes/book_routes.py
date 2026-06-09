from flask import Blueprint, request, jsonify
from services.BookService import BookService

book_bp = Blueprint('book_bp', __name__)


@book_bp.before_request
def check_auth():
    print("Teste")
    if request.path == "/status":
        return None

    # TODO: Validar TOKEN
    return None


@book_bp.route("/status", methods=['GET'])
def get_status():
    return jsonify({"status": "API de livros rodando"}), 200

@book_bp.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book, status = BookService.get_book(book_id)
    return jsonify(book), status

@book_bp.route("/books", methods=["GET"])
def list_books():
    books = BookService.get_books()
    return jsonify(books), 200

@book_bp.route("/books", methods=["POST"])
def create_book():
    return jsonify({"message": "Livro criado"}), 201

@book_bp.route("/books/<int:book_id>", methods=["PUT"])
def edit_book(book_id):
    status = BookService.update_book(book_id, request.json)
    return jsonify({}), status

@book_bp.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    status = BookService.delete_book(book_id)
    return jsonify({}), status