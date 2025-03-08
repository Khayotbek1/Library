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

def top_3_books(request):
    books = Book.objects.order_by('-page')[:3]
    contex = {'books': books}
    return render(request, 'top_3_books.html', contex)

def last_3_records(request):
    records = Record.objects.order_by('-date_received')[:3]
    contex = {'records': records}
    return render(request, 'oxirgi3ta_records.html', contex)

def fiction_books(request):
    books = Book.objects.filter(genre='Badiiy')
    contex = {'books': books}
    return render(request, 'fiction_books.html', contex)

def library_admin(request):
    lib_admin = LibraryAdmin.objects.all()
    context = {'lib_admin': lib_admin}
    return render(request, 'lib_admin.html', context)

def admin_detail(request, admin_id):
    lib_admin = LibraryAdmin.objects.get(id=admin_id)
    context = {'lib_admin': lib_admin}
    return render(request, 'admin_detail.html', context)

