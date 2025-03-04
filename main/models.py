from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=50)
    group = models.CharField(max_length=50)
    book_quantity = models.PositiveSmallIntegerField(null=True)

    def __str__(self):
        return f"Name: {self.name}\n Course: {self.course}\n Group: {self.group}"

class Author(models.Model):
    name = models.CharField(max_length=100)
    gender_choice = (('male', 'Male'), ('female', 'Female'))
    gender = models.CharField(max_length=10, choices=gender_choice)
    date = models.DateField()
    book_quantity = models.PositiveSmallIntegerField()
    alive_or_dead = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    page = models.PositiveSmallIntegerField()
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.name} | {self.author}"

class LibraryAdmin (models.Model):
    name = models.CharField(max_length=100)
    working_hours = models.DateTimeField()

    def __str__(self):
        return self.name

class Record(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    admin = models.ForeignKey(LibraryAdmin, on_delete=models.CASCADE)
    date_received = models.DateField(auto_now_add=True)
    return_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"Student: {self.student}\n Book: {self.book}\nDate received: {self.date_received}\n Return date: {self.return_date}"