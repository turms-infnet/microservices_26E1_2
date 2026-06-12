from flask import Blueprint, request, jsonify
from services.BookService import BookService
from services.grpc_client import validate_token

book_bp = Blueprint('book_bp', __name__)


@book_bp.before_request
def check_auth():
    if request.path == "/status":
        return None

    authorization_header = request.headers.get('Authorization')
    if authorization_header is None:
        return jsonify({"detail": "Você precisa passar um token"}), 401

    token_split = authorization_header.split(" ")
    token_type = token_split[0]
    token_str = token_split[1]
    
    if token_type != "Bearer":
        return jsonify({"detail": "Token de tipo inválido"}), 401

    user_response = validate_token(token_str)

    if not user_response or not user_response.is_valid:
        return jsonify({"detail": "Token inválido ou expirado"}), 401
    
    request.user = user_response


@book_bp.route("/status", methods=['GET'])
def get_status():
    return jsonify({"status": "API de livros rodando"}), 200

@book_bp.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book, status = BookService.get_book(book_id, request.user.id)
    return jsonify(book), status

@book_bp.route("/books", methods=["GET"])
def list_books():
    books = BookService.get_books(request.user.id)
    return jsonify(books), 200

@book_bp.route("/books", methods=["POST"])
def create_book():
    response, status = BookService.create_book(request.json, request.user.id)

    return jsonify(response), status

@book_bp.route("/books/<int:book_id>", methods=["PUT"])
def edit_book(book_id):
    status = BookService.update_book(book_id, request.json, request.user.id)
    return jsonify({}), status

@book_bp.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    status = BookService.delete_book(book_id, request.user.id)
    return jsonify({}), status