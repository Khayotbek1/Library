from django.contrib import admin

from .models import *

admin.site.register(Student)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(LibraryAdmin)
admin.site.register(Record)
