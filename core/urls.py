
from django.contrib import admin
from django.urls import path
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('students/', students_view, name='students'),
    path('authors/', authors_view, name='authors'),
    path('author/<int:author_id>/', author_detail, name='author_detail'),
    path('books/', book_view, name='book_view'),
    path('books/<int:book_id>/', book_detail, name='book_detail'),
    path('records/', record_view),
    path('alive_authors/', alive_authors),
    path('top_3_books/', top_3_books),
    path('oxirgi3ta_records/', last_3_records),
    path('fiction_books/', fiction_books),
    path('lib_admin/', library_admin),
    path('lib_detail/<int:admin_id>/', admin_detail, name='admin_detail'),
    path('students/<int:student_id>/', student_detail),
    path('students/<int:student_id>/delete/', student_delete),
    path('authors/<int:author_id>/delete-confirm/', author_delete_confirm, name='author_delete_confirm'),
    path('authors/<int:author_id>/delete/', author_delete)
]
