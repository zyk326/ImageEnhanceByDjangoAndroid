from django.shortcuts import render, HttpResponse

from django.db import connection

from .models import Book, Author
# Create your views here.


def book_detail_query_string(request):
    book_id = request.GET.get('id')
    return HttpResponse(f"your book id is : {book_id}")

def book_detail_path(request, book_id):
    return HttpResponse(f"your book id is : {book_id}")

def index(request):
    cursor = connection.cursor()
    cursor.execute("select * from book_book")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    return HttpResponse("hello world")

def add_book(request):
    book = Book(name="沉思录", price=100, authorC="马可奥勒留")
    book.save()
    author = Author(name = "MarkA", books = book)
    author.save()
    return HttpResponse("insert success!")

def query_book(request):
    books = Book.objects.all()
    for book in books:
        print(book.id, book.name, book.price, book.authorC, book)
    aus =  Author.objects.all()
    for au in aus:
        print(au.id, au.name, au.books.id, au.books.name)
    return HttpResponse('query success!')