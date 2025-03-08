
from django.contrib import admin
from django.urls import path
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('students/', students_view),
    path('authors/', authors_view),
    path('author/<int:author_id>/', author_detail, name='author_detail'),
    path('books/', book_view, name='book_view'),
    path('books/<int:book_id>/', book_detail, name='book_detail'),
    path('records/', record_view),
    path('alive_authors/', alive_authors),
]
