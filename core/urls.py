
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
    path('records/', record_view, name='records'),
    path('alive_authors/', alive_authors),
    path('top_3_books/', top_3_books),
    path('oxirgi3ta_records/', last_3_records),
    path('fiction_books/', fiction_books),
    path('lib_admin/', library_admin, name='lib_admin'),
    path('lib_detail/<int:admin_id>/', admin_detail, name='admin_detail'),
    path('students/<int:student_id>/', student_detail),
    path('students/<int:student_id>/delete-confirm/', student_delete_confirm, name='student_delete_confirm'),
    path('students/<int:student_id>/delete/', student_delete),
    path('authors/<int:author_id>/delete-confirm/', author_delete_confirm, name='author_delete_confirm'),
    path('authors/<int:author_id>/delete/', author_delete),
    path('authors/create_author/', create_author),
    path('records/create_record/', create_record),
    path('lib_admin/create_admin/', create_admin),
    path('students/<int:student_id>/update/', student_update),
    path('lib_admin/<int:admin_id>/update/', library_admin_update, name= 'lib_admin_update'),
    path('lib_admin/<int:admin_id>/delete-confirm/', lib_admin_delete_confirm, name='lib_admin_delete_confirm'),
    path('lib_admin/<int:admin_id>/delete/', lib_admin_delete, name='lib_admin_delete'),
    path('authors/<int:author_id>/update/', author_update, name='author_update'),
    path('records/<int:record_id>/record_detail/', record_detail, name='record_detail'),
    path('records/<int:record_id>/delete-confirm/', record_delete_confirm, name='record_delete_confirm'),
    path('records/<int:record_id>/delete/', record_delete,  name='record_delete'),
    path('records/<int:pk>/update/', record_update, name='record_update'),
]
