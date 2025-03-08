from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def home_view(request):
    return  render(request, 'index.html')


def students_view(request):
    students = Student.objects.all()
    context = {
        'students': students,
    }
    return render (request, 'students.html', context)

def authors_view(request):
    authors = Author.objects.all()
    contex = {
        'authors': authors,
    }

    return render(request, 'authors.html', contex)

def author_detail(request, author_id):
    author = Author.objects.get(id=author_id)
    contex = {'author': author}
    return render(request, 'author_detail.html', contex)

def book_view(request):
    books = Book.objects.all()
    return render(request, 'books.html', {'books': books})


def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'book_detail.html', {'book': book})

def record_view(request):
    records = Record.objects.all()
    contex = {'records': records}
    return render(request, 'records.html', contex )

def alive_authors(request):
    authors = Author.objects.filter(alive_or_dead=True)
    contex = {'authors': authors}
    return render(request, 'alive_authors.html', contex)
