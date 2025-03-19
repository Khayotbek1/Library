from django.contrib import admin

from .models import *

# admin.site.register(Student)
# admin.site.register(Author)
# admin.site.register(Book)
# admin.site.register(LibraryAdmin)
# admin.site.register(Record)

class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'page')
    list_display_links = ('name', 'author')
    list_filter = ('author', 'genre')
    list_per_page = 5
    list_editable = ('page',)
    search_fields = ('name', 'author__name')
    search_help_text = 'Kitob nomi yoki muallif ismini kiriting.'



class BookInline(admin.TabularInline):
    model = Book
    extra = 3


class AuthorAdmin(admin.ModelAdmin):
    inlines = (BookInline,)

admin.site.register(Book,BookAdmin)
admin.site.register(Author, AuthorAdmin)



