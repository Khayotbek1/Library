from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *


PAGES = [
    {"name": "Students", "url": "/students"},
    {"name": "Hamma mualliflarni chiqarish", "url": "/authors"},
    {"name": "Hamma kitoblarni chiqarish", "url": "/books"},
    {"name": "Hamma recordlarni chiqarish", "url": "/records"},
    {"name": "Tirik mualliflarni chiqarish", "url": "/alive_authors"},
    {"name": "Eng katta 3 ta kitob", "url": "/top_3_books"},
    {"name": "Oxirgi 3 ta record", "url": "/oxirgi3ta_records"},
    {"name": "Badiiy kitoblar", "url": "/fiction_books"},
    {"name": "Barcha adminlar", "url": "/lib_admin"},
]

def home_view(request):
    query = request.GET.get("q", "").lower()
    results = []

    if query:
        results = [page for page in PAGES if query in page["name"].lower()]

    return render(request, 'index.html', {"results": results})


def students_view(request):
    students = Student.objects.all()
    search = request.GET.get('search')
    if search is not None:
        students = students.filter(name__contains=search)
    context = {
        'students': students,
        'search': search,
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
    search = request.GET.get('search')
    if search is not None:
        records = records.filter(student__name__contains=search)

    contex = {
        'records': records,
        'search': search,
    }
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


def student_detail(request, student_id):
    student = Student.objects.get(id = student_id)
    context = {'student': student}
    return render(request, 'student.html', context)

def student_delete(request, student_id):
    student = Student.objects.get(id = student_id)
    student.delete()
    return redirect('students')

def author_delete_confirm(request, author_id):
    author = Author.objects.get(id = author_id)
    context = {'author': author}
    return render(request, 'author_delete_confirm.html', context)

def author_delete(request, author_id):
    author = Author.objects.get(id = author_id)
    author.delete()
    return redirect('authors')

