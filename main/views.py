from django.shortcuts import render, redirect, get_object_or_404
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
    if request.method == "POST":
        Student.objects.create(
            name = request.POST.get('ism'),
            course = request.POST.get('kurs'),
            group = request.POST.get('guruh'),
            book_quantity = request.POST.get('kitob_soni')
        )
        return redirect('students')
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


def create_author(request):
    if request.method == "POST":
        Author.objects.create(
            name = request.POST.get('ism'),
            gender = request.POST.get('jins'),
            date = request.POST.get('date'),
            book_quantity = None if request.POST.get('kitob_soni') == '' else request.POST.get('kitob_soni'),
            alive_or_dead =True if request.POST.get('tirik') == 'on' else False,
        )
        return redirect('authors')
    return render(request, "create_author.html")

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

def student_delete_confirm(request, student_id):
    student = Student.objects.get(id=student_id)
    context = {'student': student}
    return render(request, 'student_delete_confirm.html', context)

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

def create_record(request):
    if request.method == "POST":
        Record.objects.create(
            student = Student.objects.get(id = request.POST.get('talaba_id')),
            book = Book.objects.get(id = request.POST.get('kitob_id')),
            admin = LibraryAdmin.objects.get(id = request.POST.get('admin_id')),
            date_received = None if request.POST.get('topshirildi') == '' else request.POST.get('topshirildi'),
            return_date = None if request.POST.get('qaytarish') == '' else request.POST.get('topshirildi'),
        )
        return redirect('records')
    context = {
        'admins' : LibraryAdmin.objects.all(),
        'talabalar': Student.objects.all(),
        'kitoblar': Book.objects.all()
    }
    return render (request, "create_record.html", context)


def create_admin(request):
    if request.method == "POST":
        LibraryAdmin.objects.create(
            name = request.POST.get('ism'),
            working_hours = request.POST.get('ish_vaqti'),
        )
        return redirect('lib_admin')
    return render(request, "create_admin.html")


def student_update(request, student_id) :
        student = get_object_or_404(Student, id = student_id)
        if request.method == "POST":
            student.name = request.POST.get('ism')
            student.course = request.POST.get('kurs')
            student.group = request.POST.get('guruh')
            student.book_quantity = None if request.POST.get('kitob_soni') == '' else request.POST.get('kitob_soni')
            student.save()
            return redirect('students')
        context = {'student': student}
        return render(request, 'student_update.html', context)